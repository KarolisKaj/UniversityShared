namespace VoiceRecognition.Services.Google
{
    using global::Google.Cloud.Speech.V1;
    using System.Threading.Tasks;
    using VoiceRecognition.Extensions;
    using Grpc.Core;
    using System.Linq;

    public class AzureProvider : IProvider
    {
        private readonly Channel _channel;
        public AzureProvider()
        {
            _channel = new CredentialProvider().Create(DefaultProvider.DefaultGoogleAuthFilePath);
        }

        public void Dispose()
        {
        }

        public Task<string> TextFromAudioSample(string audioPath)
        {
            return Task.Run(() =>
            {
                // TODO: remove mock.
                //return "careless opposite";

                var speech = SpeechClient.Create(_channel);
                var response = speech.Recognize(new RecognitionConfig()
                {
                    LanguageCode = "en",
                }, RecognitionAudio.FromFile(audioPath));
                return response.Results.Single().Alternatives.Single().Transcript;
            });
        }
    }
}
