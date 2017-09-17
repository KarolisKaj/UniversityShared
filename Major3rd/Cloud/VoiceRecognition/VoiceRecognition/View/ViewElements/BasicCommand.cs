namespace VoiceRecognition.View.ViewElements
{
    using System;
    using System.Windows.Input;
    public class BasicCommand : ICommand
    {
        private readonly Func<bool> _canExecute;
        private readonly Action _execute;

        public BasicCommand(Func<bool> canExecute, Action execute)
        {
            _canExecute = canExecute;
            _execute = execute;
        }

        public BasicCommand(Action execute) : this(() => true, execute)
        {
        }
        public event EventHandler CanExecuteChanged;

        public void RaiseCanExecute()
        {
            CanExecuteChanged?.Invoke(this, null);
        }
        public bool CanExecute(object parameter)
        {
            return _canExecute();
        }

        public void Execute(object parameter)
        {
            _execute();
        }
    }
}
