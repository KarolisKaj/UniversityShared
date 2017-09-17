namespace VoiceRecognition.View
{
    using System.Collections.ObjectModel;
    public class ViewModel
    {
        public ObservableCollection<VoiceServiceProviderViewModel> Providers { get; set; }
    }
}
