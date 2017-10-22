using Microsoft.CognitiveServices.SpeechRecognition;
using System;
using System.IO;
using System.Linq;
using System.Threading;
using System.Threading.Tasks;
using VoiceRecognition.Extensions;

namespace VoiceRecognition.Services.Azure
{
    public class AzureProvider : IProvider
    {
        private readonly Lazy<DataRecognitionClient> _speech;
        private ManualResetEvent _signal = new ManualResetEvent(false);
        private string floatingResult = "";
        public AzureProvider()
        {
            _speech = new Lazy<DataRecognitionClient>(() => SpeechRecognitionServiceFactory.CreateDataClient(
                              SpeechRecognitionMode.ShortPhrase,
                              "en-US",
                              new CredentialProvider().Create(DefaultProvider.DefaultAzureAuthFilePath)));
        }

        public void Dispose()
        {
            if (_speech.IsValueCreated)
                _speech.Value.Dispose();
        }

        public Task<string> TextFromAudioSample(string audioPath)
        {
            return Task.Run(() =>
            {
                _signal.Reset();
                _speech.Value.OnResponseReceived += Received;
                _speech.Value.OnConversationError += (o, e) => { System.Diagnostics.Debug.WriteLine("Azure acting up :)"); };
                SendAudioHelper(audioPath);
                if (_signal.WaitOne(TimeSpan.FromMinutes(10)))
                {
                    _speech.Value.OnResponseReceived -= Received;
                    return floatingResult;
                }
                else
                {
                    return String.Empty;
                }
            });
        }

        private void Received(object sender, SpeechResponseEventArgs e)
        {
            if (e.PhraseResponse.RecognitionStatus == RecognitionStatus.RecognitionSuccess)
            {
                floatingResult = e.PhraseResponse.Results.OrderBy(x => x.Confidence == Confidence.High).First().DisplayText;
            }
            _signal.Set();
        }

        private void SendAudioHelper(string audioPath)
        {
            using (FileStream fileStream = new FileStream(audioPath, FileMode.Open, FileAccess.Read))
            {
                int bytesRead = 0;
                byte[] buffer = new byte[1024];
                try
                {
                    do
                    {
                        bytesRead = fileStream.Read(buffer, 0, buffer.Length);
                        _speech.Value.SendAudio(buffer, bytesRead);
                    }
                    while (bytesRead > 0);
                }
                finally
                {
                    _speech.Value.EndAudio();
                }
            }
        }
    }
}
