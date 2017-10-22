namespace VoiceRecognition.Services
{
    using System;
    using System.Collections.Generic;
    public class ServiceProvider : IDisposable
    {
        List<ServiceModel> _serviceModel = new List<ServiceModel>();
        public ServiceProvider()
        {
            _serviceModel.Add(new ServiceModel(new Azure.AzureProvider(), Values.Provider.Azure));
            _serviceModel.Add(new ServiceModel(new Google.AzureProvider(), Values.Provider.Google));
            _serviceModel.Add(new ServiceModel(new Amazon.AmazonProvider(), Values.Provider.Amazon));
        }
        public IEnumerable<ServiceModel> ServiceProviders { get { return _serviceModel; } }

        public void Dispose()
        {
            foreach (var provider in _serviceModel)
                provider.Provider.Dispose();
        }
    }
}
