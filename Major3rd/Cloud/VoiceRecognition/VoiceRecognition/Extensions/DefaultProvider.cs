using System.IO;

namespace VoiceRecognition.Extensions
{
    public static class DefaultProvider
    {

        // TODO: perform lookup on relative dir for files with extension.
        public static string DefaultResultFilePath
        {
            get
            {
                var path = Path.GetFullPath(Path.Combine(System.Reflection.Assembly.GetExecutingAssembly().Location, @"..\..\..\..\..\")) + "1000RandomWords.txt";
                return File.Exists(path) ? path : null;
            }
        }
        // TODO: perform lookup on relative dir for files with extension.
        public static string DefaultAudioFilePath
        {
            get
            {
                var path = Path.GetFullPath(Path.Combine(System.Reflection.Assembly.GetExecutingAssembly().Location, @"..\..\..\..\..\")) + "WordsRecording.mp3";
                return File.Exists(path) ? path : null;
            }
        }
    }
}
