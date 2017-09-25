namespace VoiceRecognition.Services.Google
{
    using global::Google.Cloud.Speech.V1;
    using System;
    using System.Threading.Tasks;
    public class GoogleProvider : IProvider
    {
        public GoogleProvider()
        {
           // var credentials = new CredentialProvider().Create().Result;
        }
        public Task<string> TextFromAudioSample(string audioPath)
        {
            return Task.Run(() =>
            {
                var speech = SpeechClient.Create();
                var response = speech.Recognize(new RecognitionConfig()
                {
                    Encoding = RecognitionConfig.Types.AudioEncoding.Flac,
                    SampleRateHertz = 16000,
                    LanguageCode = "en",
                }, RecognitionAudio.FetchFromUri(new Uri("https://drive.google.com/file/d/0B_yUi-B_c-_YMVVMZ3JSUW9jN1E/view?usp=sharing")));
                foreach (var result in response.Results)
                {
                    foreach (var alternative in result.Alternatives)
                    {
                        //Console.WriteLine(alternative.Transcript);
                    }
                }
                return "";

            });
        }
    }
}
