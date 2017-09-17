using System.IO;

namespace VoiceRecognition.Extensions
{
    public static class DefaultProvider
    {
        public static string DefaultResultFilePath
        {
            get
            {
                var path = Path.GetFullPath(Path.Combine(System.Reflection.Assembly.GetExecutingAssembly().Location, @"..\..\..\..\..\")) + "1000RandomWords.txt";
                return File.Exists(path) ? path : null;
            }
        }
        public static string DefaultAudioFilePath
        {
            get
            {
                var path = Path.GetFullPath(Path.Combine(System.Reflection.Assembly.GetExecutingAssembly().Location, @"..\..\..\..\..\")) + "WordsRecording.mp5";
                return File.Exists(path) ? path : null;
            }
        }
    }
}
