namespace VoiceRecognition.View
{
    using System.Collections.ObjectModel;
    using System.Windows.Input;
    using VoiceRecognition.View.ViewElements;

    public class MainViewModel  : ObservableViewModel
    {
        public ObservableCollection<VoiceServiceProviderViewModel> Providers { get; set; }
        public ICommand AudioPathCommand { get; set; }
        public ICommand ResultPathCommand { get; set; }

        private string _audioPath;
        public string AudioPath
        {
            get { return _audioPath; }
            set { _audioPath = value; OnPropertyChanged(); }
        }

        private string _resultPath;
        public string ResultPath
        {
            get { return _resultPath; }
            set { _resultPath = value; OnPropertyChanged(); }
        }
    }
}
