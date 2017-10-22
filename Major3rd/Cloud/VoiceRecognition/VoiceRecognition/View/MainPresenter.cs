using System;
using VoiceRecognition.Extensions;
using VoiceRecognition.Services;
using VoiceRecognition.View.ViewElements;

namespace VoiceRecognition.View
{
    public class MainPresenter
    {
        private readonly MainViewModel _vm;
        private readonly ServiceProvider _service;

        public MainPresenter(MainViewModel vm, ServiceProvider service)
        {
            _vm = vm;
            _service = service;
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
            _vm.Providers = new System.Collections.ObjectModel.ObservableCollection<VoiceServiceProviderViewModel>();
            foreach (var provider in _service.ServiceProviders)
            {
                var providerVM = new VoiceServiceProviderViewModel() { ProviderImagePath = provider.ProviderType.ProviderToImageUrl() };
                providerVM.EvaluateCommand = new BasicCommand(
                            () => !String.IsNullOrWhiteSpace(_vm.AudioPath) && !providerVM.IsRequestInProgress,
                            () => ExecuteAudioToText(providerVM, provider));

                _vm.Providers.Add(providerVM);
            }
        }

        private void SetupCommands()
        {
            _vm.AudioPathCommand = new BasicCommand(() =>
            {
                Microsoft.Win32.OpenFileDialog dlg = new Microsoft.Win32.OpenFileDialog();
                dlg.DefaultExt = ".wav";
                dlg.Filter = "WAV Files (*.wav)|*.wav";
                var result = dlg.ShowDialog();

                if (result.HasValue && result.Value)
                {
                    _vm.AudioPath = dlg.FileName;
                    CheckCanExecute();
                }
            });

            _vm.ResultPathCommand = new BasicCommand(() =>
            {
                Microsoft.Win32.OpenFileDialog dlg = new Microsoft.Win32.OpenFileDialog();
                dlg.DefaultExt = ".txt";
                dlg.Filter = "Text Files (*.txt)|*.txt";
                var result = dlg.ShowDialog();

                if (result.HasValue && result.Value)
                {
                    _vm.ResultPath = dlg.FileName;
                    CheckCanExecute();
                }
            });
        }

        private void CheckCanExecute()
        {
            foreach (var command in _vm.Providers)
                command.EvaluateCommand.RaiseCanExecute();
        }

        private async void ExecuteAudioToText(VoiceServiceProviderViewModel providerVM, ServiceModel provider)
        {
            try
            {
                providerVM.IsRequestInProgress = true;
                CheckCanExecute();
                var results = await provider.Provider.TextFromAudioSample(_vm.AudioPath);
                providerVM.ErrorCount = _vm.ResultPath.GetFileContent().GetMismatches(results);
                providerVM.IsRequestInProgress = false;
                CheckCanExecute();
            }
            catch (Exception ex)
            {
                _vm.ErrorText = ex.Message;
            }
        }
    }
}
