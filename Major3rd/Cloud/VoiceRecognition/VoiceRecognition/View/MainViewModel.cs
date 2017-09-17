namespace VoiceRecognition.View
{
    using System.Collections.ObjectModel;
    public class MainViewModel
    {
        public ObservableCollection<VoiceServiceProviderViewModel> Providers { get; set; }
    }
}
