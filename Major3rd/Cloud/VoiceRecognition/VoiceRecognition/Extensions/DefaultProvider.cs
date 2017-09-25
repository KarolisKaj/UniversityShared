using System.Configuration;
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
                var path = Path.GetFullPath(Path.Combine(System.Reflection.Assembly.GetExecutingAssembly().Location, ConfigurationManager.AppSettings["defaultWordPath"]));
                return File.Exists(path) ? path : null;
            }
        }
        // TODO: perform lookup on relative dir for files with extension.
        public static string DefaultAudioFilePath
        {
            get
            {
                var path = Path.GetFullPath(Path.Combine(System.Reflection.Assembly.GetExecutingAssembly().Location, ConfigurationManager.AppSettings["defaultAudioPath"]));
                return File.Exists(path) ? path : null;
            }
        }
    }
}
