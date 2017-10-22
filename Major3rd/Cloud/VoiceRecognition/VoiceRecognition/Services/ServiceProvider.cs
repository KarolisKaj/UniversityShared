namespace VoiceRecognition.Services
{
    using System.Collections.Generic;
    public class ServiceProvider
    {
        List<ServiceModel> _serviceModel = new List<ServiceModel>();
        public ServiceProvider()
        {
            _serviceModel.Add(new ServiceModel(new Azure.AzureProvider(), Values.Provider.Azure));
            _serviceModel.Add(new ServiceModel(new Google.AzureProvider(), Values.Provider.Google));
            _serviceModel.Add(new ServiceModel(new Amazon.AmazonProvider(), Values.Provider.Amazon));
        }
        public IEnumerable<ServiceModel> ServiceProviders { get { return _serviceModel; } }
    }
}
