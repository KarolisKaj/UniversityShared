using System.ComponentModel;
using System.Runtime.CompilerServices;
using System.Windows.Input;

namespace VoiceRecognition.View
{
    public class VoiceServiceProviderViewModel : INotifyPropertyChanged
    {
        private string _providerImagePath;
        public string ProviderImagePath
        {
            get { return _providerImagePath; }
            set { _providerImagePath = value; OnPropertyChanged(); }
        }

        public ICommand EvaluateCommand { get; set; }

        private void OnPropertyChanged([CallerMemberName]string name = null) => PropertyChanged?.Invoke(this, new PropertyChangedEventArgs(name));
        public event PropertyChangedEventHandler PropertyChanged;
    }
}
