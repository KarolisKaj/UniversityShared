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
            _serviceModel.Add(new ServiceModel(new Google.GoogleProvider(), Values.Provider.Google));
            _serviceModel.Add(new ServiceModel(new SpeechMatics.SpeechMaticsProvider(), Values.Provider.SpeechMatics));
        }
        public IEnumerable<ServiceModel> ServiceProviders { get { return _serviceModel; } }

        public void Dispose()
        {
            foreach (var provider in _serviceModel)
                provider.Provider.Dispose();
        }
    }
}
