using System;
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
            SetupDefaults();
            SetupViewModel();
            SetupCommands();
        }

        private void SetupDefaults()
        {
            _vm.ResultPath = DefaultProvider.DefaultResultFilePath;
            _vm.AudioPath = DefaultProvider.DefaultAudioFilePath;
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

        private void SetupCommands()
        {
            _vm.AudioPathCommand = new BasicCommand(() =>
            {
                Microsoft.Win32.OpenFileDialog dlg = new Microsoft.Win32.OpenFileDialog();
                dlg.DefaultExt = ".mp3";
                dlg.Filter = "MP3 Files (*.mp3)|*.mp3";
                var result = dlg.ShowDialog();

                if (result.HasValue && result.Value)
                    _vm.AudioPath = dlg.FileName;
            });

            _vm.ResultPathCommand = new BasicCommand(() =>
            {
                Microsoft.Win32.OpenFileDialog dlg = new Microsoft.Win32.OpenFileDialog();
                dlg.DefaultExt = ".txt";
                dlg.Filter = "Text Files (*.txt)|*.txt";
                var result = dlg.ShowDialog();

                if (result.HasValue && result.Value)
                    _vm.ResultPath = dlg.FileName;
            });
        }

    }
}
