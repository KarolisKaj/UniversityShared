using VoiceRecognition.Values;
using System;

namespace VoiceRecognition.Extensions
{
    public static class Mapper
    {
        public static string ProviderToImageUrl(this Provider provider)
        {

            var assemblyName = System.Diagnostics.Process.GetCurrentProcess().MainModule.ModuleName.Split('.')[0];
            var baseUrl = $"/{assemblyName};component/Resources/";
            switch (provider)
            {
                case Provider.Google:
                    return baseUrl + "Google.png";
                case Provider.Amazon:
                    return baseUrl + "Amazon.png";
                case Provider.Azure:
                    return baseUrl + "MSAzure.png";
                default:
                    throw new ArgumentException("Provided argument was not found.");
            }
        }
    }
}
