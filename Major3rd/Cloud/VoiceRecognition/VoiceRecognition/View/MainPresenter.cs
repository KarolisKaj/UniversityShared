using VoiceRecognition.Extensions;
using VoiceRecognition.Values;
using VoiceRecognition.View.ViewElements;

namespace VoiceRecognition.View
{
    public class MainPresenter
    {
        private readonly MainViewModel _vm;

        public MainPresenter(MainViewModel vm)
        {
            _vm = vm;
            SetupViewModel();
        }

        private void SetupViewModel()
        {
            _vm.Providers = new System.Collections.ObjectModel.ObservableCollection<VoiceServiceProviderViewModel>()
            {
                new VoiceServiceProviderViewModel(){EvaluateCommand = new BasicCommand(() => true, () =>{ }), ProviderImagePath = Provider.Amazon.ProviderToImageUrl()},
                new VoiceServiceProviderViewModel(){EvaluateCommand = new BasicCommand(() => true, () =>{ }), ProviderImagePath = Provider.Google.ProviderToImageUrl()},
                new VoiceServiceProviderViewModel(){EvaluateCommand = new BasicCommand(() => true, () =>{ }), ProviderImagePath = Provider.Azure.ProviderToImageUrl()},
            };
        }
    }
}
