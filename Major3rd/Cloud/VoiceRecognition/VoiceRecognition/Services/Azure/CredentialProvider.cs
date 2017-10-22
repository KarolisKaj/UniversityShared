using System.IO;

namespace VoiceRecognition.Services.Azure
{
    public class CredentialProvider
    {
        public string Create(string authFilePath)
        {
            return File.ReadAllText(authFilePath);
        }
    }
}
