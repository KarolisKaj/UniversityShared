namespace VoiceRecognition.Services
{
    using System.Threading.Tasks;
    public interface IProvider
    {
        Task<string> TextFromAudioSample(string audioPath);
    }
}
