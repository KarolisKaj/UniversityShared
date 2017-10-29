using System;
using System.Collections.Generic;
using System.IO;

namespace VoiceRecognition.Extensions
{
    public static class TextRecognitionHelper
    {
        private static string[] _splitters = new[] { Environment.NewLine, " ", ".", ",", "-" };
        public static int GetMismatches(this string correct, string recognized)
        {
            var correctWords = new HashSet<string>(correct.Split(_splitters, StringSplitOptions.RemoveEmptyEntries), StringComparer.OrdinalIgnoreCase);
            var recognizedWords = recognized.Split(_splitters, StringSplitOptions.RemoveEmptyEntries);
            correctWords.ExceptWith(recognizedWords);
            return correctWords.Count;
        }

        public static string GetFileContent(this string path) => File.ReadAllText(path);
    }
}
