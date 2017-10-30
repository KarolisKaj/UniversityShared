using System;
using System.Globalization;
using System.Windows.Data;
using System.Windows.Media;

namespace VoiceRecognition.View.ViewElements
{
    public class TextToColorConverter : IValueConverter
    {
        public object Convert(object value, Type targetType, object parameter, CultureInfo culture)
        {
            var actualValue = value as Result;
            return actualValue!= null && actualValue.ErrorEntries.HasValue && actualValue.ErrorEntries.Value > 0 ? new SolidColorBrush(Colors.Red) : new SolidColorBrush(Colors.Green);
        }

        public object ConvertBack(object value, Type targetType, object parameter, CultureInfo culture)
        {
            throw new NotImplementedException();
        }
    }
}
