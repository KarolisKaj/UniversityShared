using System.IO;

namespace VoiceRecognition.Services.SpeechMatics
{
    public static class CredentialsProvider
    {
        public static string Create(this string authFilePath)
        {
            return File.ReadAllText(authFilePath);
        }
    }
}
