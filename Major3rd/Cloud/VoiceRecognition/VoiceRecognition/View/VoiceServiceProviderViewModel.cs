using System.ComponentModel;
using System.Runtime.CompilerServices;
using System.Windows.Input;
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

        public ICommand EvaluateCommand { get; set; }


    }
}
