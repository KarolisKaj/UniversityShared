using System;
using System.Collections.Generic;
using System.IO;
using VoiceRecognition.View;

namespace VoiceRecognition.Extensions
{
    public static class TextRecognitionHelper
    {
        private static string[] _splitters = new[] { Environment.NewLine, " ", ".", ",", "-" };
        public static Result CalculateResult(this string correct, string recognized)
        {
            var result = new Result();
            var correctWords = new HashSet<string>(correct.Split(_splitters, StringSplitOptions.RemoveEmptyEntries), StringComparer.OrdinalIgnoreCase);
            var recognizedWords = recognized.Split(_splitters, StringSplitOptions.RemoveEmptyEntries);
            result.TotalEntries = correctWords.Count;
            correctWords.ExceptWith(recognizedWords);
            result.ErrorEntries = correctWords.Count;
            result.ErrorPercentage = (double)result.ErrorEntries / (double)result.TotalEntries * 100;
            return result;
        }

        public static string GetFileContent(this string path) => File.ReadAllText(path);
    }
}
