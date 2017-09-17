using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace VoiceRecognition.Services.Amazon
{
    public class AmazonProvider : IProvider
    {
        public Task<string> TextFromAudioSample(string audioPath)
        {
            throw new NotImplementedException();
        }
    }
}
