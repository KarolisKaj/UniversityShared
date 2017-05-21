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
            //var typeBuilder = new TypeBuilder(,);
        }

        public IPrintable GetInstance()
        {
            return (IPrintable)Activator.CreateInstance(_printType);
            //_printType.InvokeMember("Write",
            //    BindingFlags.Default | BindingFlags.InvokeMethod,
            //    null,
            //    obj,
            //    new object[] { "Hello World" });

            return (IPrintable)_printType.GetConstructor(new Type[0]).Invoke(new object[0]);

        }
    }
}
