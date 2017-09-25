using Google.Apis.Auth.OAuth2;
using Google.Apis.Services;
using System.Threading.Tasks;

namespace VoiceRecognition.Services.Google
{
    public class CredentialProvider
    {
        public CredentialProvider()
        {
          
        }

        public async Task<GoogleCredential> Create()
        {
            GoogleCredential credential = await GoogleCredential.GetApplicationDefaultAsync();
            return credential;
            //var compute = new ComputeService(new BaseClientService.Initializer()
            //{
            //    HttpClientInitializer = credential
            //});
        
        }
    }
}
