using System;
using System.Threading.Tasks;

namespace VoiceRecognition.Services.Azure
{
    public class AzureProvider : IProvider
    {
        public Task<string> TextFromAudioSample(string audioPath)
        {
            throw new NotImplementedException();
        }
    }
}
