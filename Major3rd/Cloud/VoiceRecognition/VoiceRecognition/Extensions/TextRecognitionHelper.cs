using System;
using System.Collections.Generic;
using System.IO;

namespace VoiceRecognition.Extensions
{
    public static class TextRecognitionHelper
    {
        public static int GetMismatches(this string correct, string recognized)
        {
            var correctWords = new HashSet<string>(correct.Split(new[] { Environment.NewLine, " " }, StringSplitOptions.RemoveEmptyEntries), StringComparer.OrdinalIgnoreCase);
            var recognizedWords = recognized.Split(new[] { Environment.NewLine, " " }, StringSplitOptions.RemoveEmptyEntries);
            correctWords.ExceptWith(recognizedWords);
            return correctWords.Count;
        }

        public static string GetFileContent(this string path) => File.ReadAllText(path);
    }
}
