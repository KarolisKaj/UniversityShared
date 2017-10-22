namespace VoiceRecognition.Services
{
    using System;
    using System.Threading.Tasks;
    public interface IProvider : IDisposable
    {
        Task<string> TextFromAudioSample(string audioPath);
    }
}
