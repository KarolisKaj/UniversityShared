using System;
using System.Threading.Tasks;

namespace VoiceRecognition.Services.Amazon
{
    public class AmazonProvider : IProvider
    {
        public void Dispose()
        {
            throw new NotImplementedException();
        }

        public Task<string> TextFromAudioSample(string audioPath)
        {
            return Task.Delay(2000).ContinueWith(x => "");
        }
    }
}
