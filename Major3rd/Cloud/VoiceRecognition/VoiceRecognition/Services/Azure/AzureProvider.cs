using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
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
