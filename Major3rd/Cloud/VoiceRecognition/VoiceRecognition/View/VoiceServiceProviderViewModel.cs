using VoiceRecognition.View.ViewElements;

namespace VoiceRecognition.View
{
    public class VoiceServiceProviderViewModel : ObservableViewModel
    {
        private string _providerImagePath;
        public string ProviderImagePath
        {
            get { return _providerImagePath; }
            set { _providerImagePath = value; OnPropertyChanged(); }
        }

        public BasicCommand EvaluateCommand { get; set; }


        private bool _isRequestInProgress;

        public bool IsRequestInProgress
        {
            get { return _isRequestInProgress; }
            set { _isRequestInProgress = value; OnPropertyChanged(); }
        }



    }
}
