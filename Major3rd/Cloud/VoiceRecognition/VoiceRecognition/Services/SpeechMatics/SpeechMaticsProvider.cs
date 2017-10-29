using Newtonsoft.Json.Linq;
using System;
using System.IO;
using System.Linq;
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
                requestContent.Add(new StringContent("none"), "notification");
                requestContent.Add(new StreamContent(new MemoryStream(File.ReadAllBytes(audioPath))), "data_file", "audio.wav");


                using (HttpResponseMessage response = await _client.Value.PostAsync(VoiceRecognitionEndPoint, requestContent))
                {
                    using (HttpContent responseContent = response.Content)
                    {
                        if (response.StatusCode == System.Net.HttpStatusCode.OK)
                        {
                            using (var reader = new StreamReader(await responseContent.ReadAsStreamAsync()))
                            {
                                string id = (string)JObject.Parse(await reader.ReadToEndAsync())["id"];
                                sb.Append(await ObtainTextRec(UriForJobId(id), id));
                            }
                        }
                    }
                }
            }

            return sb.ToString();
        }

        private async Task<string> ObtainTextRec(Uri uri, string id)
        {
            var response = await _client.Value.GetAsync(uri);
            using (HttpContent responseContent = response.Content)
            {
                if (response.StatusCode == System.Net.HttpStatusCode.OK)
                {
                    using (var reader = new StreamReader(await responseContent.ReadAsStreamAsync()))
                    {
                        var results = reader.ReadToEnd();
                        var status = JObject.Parse(results).GetValue("job").Value<string>("job_status");
                        if (status == "done")
                        {
                            return await ObtainText(id);
                        }
                        else
                        {
                            await Task.Delay(500);
                            return await ObtainTextRec(uri, id);
                        }
                    }
                }
            }
            return "";
        }

        private async Task<string> ObtainText(string id)
        {
            var uri = UriForTranscriptId(id);
            var response = await _client.Value.GetAsync(uri);
            using (HttpContent responseContent = response.Content)
            {
                if (response.StatusCode == System.Net.HttpStatusCode.OK)
                {
                    using (var reader = new StreamReader(await responseContent.ReadAsStreamAsync()))
                    {
                        var o = JObject.Parse(reader.ReadToEnd());
                        var result = string.Join(" ", o.SelectToken("words").Select(jt => jt.Value<string>("name").Replace(".", "")));
                        return String.IsNullOrWhiteSpace(result) ? await ObtainText(id) : result;
                    }
                }
            }
            return "";
        }

        private Uri UriForJobId(string id) => new Uri($"https://api.speechmatics.com/v1.0/user/30421/jobs/{id}/?auth_token={DefaultProvider.DefaultSpeechMaticsAuthFilePath.Create()}");
        private Uri UriForTranscriptId(string id) => new Uri($"https://api.speechmatics.com/v1.0/user/30421/jobs/{id}/transcript?auth_token={DefaultProvider.DefaultSpeechMaticsAuthFilePath.Create()}");
    }
}

