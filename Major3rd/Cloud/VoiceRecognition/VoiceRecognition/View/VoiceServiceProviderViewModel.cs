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

        private Result _result;
        public Result Result
        {
            get { return _result; }
            set { _result = value; OnPropertyChanged(); }
        }

    }
    public class Result : ObservableViewModel
    {
        private int? _errorEntries;
        public int? ErrorEntries
        {
            get { return _errorEntries; }
            set { _errorEntries = value; OnPropertyChanged(); }
        }

        private int? _totalEntries;
        public int? TotalEntries
        {
            get { return _totalEntries; }
            set { _totalEntries = value; OnPropertyChanged(); }
        }

        private double? _errorPercentage;
        public double? ErrorPercentage
        {
            get { return _errorPercentage; }
            set { _errorPercentage = value; OnPropertyChanged(); }
        }
    }
}
