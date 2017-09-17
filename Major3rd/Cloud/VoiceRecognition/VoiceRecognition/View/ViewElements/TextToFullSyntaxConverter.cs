using System;
using System.Globalization;
using System.Windows.Data;

namespace VoiceRecognition.View.ViewElements
{
    class TextToFullSyntaxConverter : IValueConverter
    {
        public object Convert(object value, Type targetType, object parameter, CultureInfo culture)
        {
            var actualValue = value as int?;
            return actualValue.HasValue ? $"Error count : {actualValue.Value}" : null;
        }

        public object ConvertBack(object value, Type targetType, object parameter, CultureInfo culture)
        {
            throw new NotImplementedException();
        }
    }
}
