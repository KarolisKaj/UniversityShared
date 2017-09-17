namespace VoiceRecognition.Services
{
    using VoiceRecognition.Values;
    public class ServiceModel
    {
        public ServiceModel(IProvider provider, Provider providerType)
        {
            Provider = provider;
            ProviderType = providerType;
        }
        public IProvider Provider { get; }
        public Provider ProviderType { get; }
    }
}
