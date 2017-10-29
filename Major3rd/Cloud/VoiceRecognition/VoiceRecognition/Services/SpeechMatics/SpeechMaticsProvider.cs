using System;
using System.Collections.Generic;
using System.IO;
using System.Net.Http;
using System.Text;
using System.Threading.Tasks;
using VoiceRecognition.Extensions;

namespace VoiceRecognition.Services.SpeechMatics
{
    public class SpeechMaticsProvider : IProvider
    {
        private readonly Lazy<HttpClient> _client;
        private string VoiceRecognitionEndPoint { get; }
        /// <summary>
        /// curl -F data_file=@my_audio_file.mp3 -F model=en-US "https://api.speechmatics.com/v1.0/user/30421/jobs/?auth_token={id}" # transcription
        /// </summary>
        public SpeechMaticsProvider()
        {
            _client = new Lazy<HttpClient>(() => new HttpClient(), true);
            VoiceRecognitionEndPoint = $"https://api.speechmatics.com/v1.0/user/30421/jobs/?auth_token={DefaultProvider.DefaultSpeechMaticsAuthFilePath.Create()}";
        }

        public void Dispose()
        {
            if (_client.IsValueCreated)
                _client.Value.Dispose();
        }

        public async Task<string> TextFromAudioSample(string audioPath)
        {
            var sb = new StringBuilder();

            using (var requestContent = new MultipartFormDataContent())
            {
                requestContent.Add(new StringContent("en-US"), "model");
                requestContent.Add(new StreamContent(new MemoryStream(File.ReadAllBytes(audioPath))), "data_file", "audio.wav");

                
                using (HttpResponseMessage response = await _client.Value.PostAsync(VoiceRecognitionEndPoint, requestContent))
                {
                    using (HttpContent responseContent = response.Content)
                    using (var reader = new StreamReader(await responseContent.ReadAsStreamAsync()))
                        sb.Append(await reader.ReadToEndAsync());
                }
            }

            return sb.ToString();
        }
    }
}

