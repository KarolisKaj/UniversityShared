using RoslynFun.CompilerExtensions;
using RoslynFun.Dependencies;
using RoslynFun.Factory;
using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace RoslynFun
{
    class Program
    {
        static void Main(string[] args)
        {
            var factory = new PrintExtensionFactory(typeof(MemberfulClass).FullName);
            factory.GetInstance().Print();

            Console.Read();
        }
    }
}
