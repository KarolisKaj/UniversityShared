using RoslynFun.CompilerExtensions;
using System;
using System.Reflection;

namespace RoslynFun.Factory
{
    public class PrintExtensionFactory
    {
        private readonly Type _printType;

        public PrintExtensionFactory(string className)
        {
            _printType = Type.GetType(className).GeneratePrintType(typeof(IPrintable));
        }

        public IPrintable GetInstance()
        {
            return (IPrintable)Activator.CreateInstance(_printType);

        }
    }
}
