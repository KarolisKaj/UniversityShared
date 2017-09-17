using System.Windows;
using VoiceRecognition.Services;
using VoiceRecognition.View;

namespace VoiceRecognition
{
    /// <summary>
    /// Interaction logic for App.xaml
    /// </summary>
    public partial class App : Application
    {
        protected override void OnStartup(StartupEventArgs e)
        {
            base.OnStartup(e);
            SetupMVVMP();
        }

        private void SetupMVVMP()
        {
            var vm = new MainViewModel();

            var presenter = new MainPresenter(vm, new ServiceProvider());
            var view = new MainWindow();
            view.DataContext = vm;
            view.Show();
        }
    }
}
