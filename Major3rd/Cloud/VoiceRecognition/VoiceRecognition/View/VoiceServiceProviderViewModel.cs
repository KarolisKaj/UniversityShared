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

        private int? _errorCount;
        public int? ErrorCount
        {
            get { return _errorCount; }
            set { _errorCount = value; OnPropertyChanged(); }
        }

        private int? _totalCount;
        public int? TotalCount
        {
            get { return _totalCount; }
            set { _totalCount = value; OnPropertyChanged(); }
        }

        private double? _percentage;
        public double? Percentage
        {
            get { return _percentage; }
            set { _percentage = value; OnPropertyChanged(); }
        }
    }
}
