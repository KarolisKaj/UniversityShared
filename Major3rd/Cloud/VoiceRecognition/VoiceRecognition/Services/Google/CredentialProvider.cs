using Google.Apis.Auth.OAuth2;
using Google.Cloud.Speech.V1;
using Grpc.Auth;
using Grpc.Core;

namespace VoiceRecognition.Services.Google
{
    public class CredentialProvider
    {
        public CredentialProvider()
        {

        }

        public Channel Create(string authFilePath)
        {
            GoogleCredential googleCredential = GoogleCredential.FromFile(authFilePath);
            return new Channel(SpeechClient.DefaultEndpoint.Host, googleCredential.ToChannelCredentials());
        }
    }
}
