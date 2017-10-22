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
            var serviceProvider = new ServiceProvider();
            Application.Current.Exit += (o, arg) => serviceProvider.Dispose();

            var presenter = new MainPresenter(vm, serviceProvider);
            var view = new MainWindow();
            view.DataContext = vm;
            view.Show();
        }
    }
}
