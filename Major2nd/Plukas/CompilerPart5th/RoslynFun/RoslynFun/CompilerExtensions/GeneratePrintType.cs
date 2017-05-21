using Microsoft.CodeAnalysis;
using Microsoft.CodeAnalysis.CSharp;
using Microsoft.CodeAnalysis.Emit;
using System;
using System.Collections.Generic;
using System.IO;
using System.Linq;
using System.Reflection;

namespace RoslynFun.CompilerExtensions
{
    public static class GenerationHelpers
    {
        public static Type GeneratePrintType(this Type originClass, Type printableInterface)
        {
            SyntaxTree tree = CSharpSyntaxTree.ParseText(
            $"using System; using System.Linq;" +
            $" public class {originClass.Name}Print : {originClass.FullName}, {printableInterface.FullName}"
            + @"{
                    public void Print()
                    {" +
                        "var members = AppDomain.CurrentDomain.GetAssemblies().Where(x => x.FullName == \"" + originClass.Assembly.FullName + "\").FirstOrDefault().GetType(\"" + originClass.FullName + "\").GetMembers();" +
                        "foreach(var member in members)" +
                        "{" +
                            "Console.WriteLine(member);" +
                        "}" +
                    "}" +
            "}"
            );

            MetadataReference[] references = new MetadataReference[]
            {
               MetadataReference.CreateFromFile(originClass.Assembly.Location),
               MetadataReference.CreateFromFile(typeof(Enumerable).Assembly.Location),
               MetadataReference.CreateFromFile(typeof(Console).Assembly.Location),
            };

            CSharpCompilation compilation = CSharpCompilation.Create(
                $"{originClass.FullName}.PrintModule",
                syntaxTrees: new[] { tree },
                references: references,
                options: new CSharpCompilationOptions(OutputKind.DynamicallyLinkedLibrary));


            using (var ms = new MemoryStream())
            {
                EmitResult result = compilation.Emit(ms);

                if (!result.Success)
                {
                    IEnumerable<Diagnostic> failures = result.Diagnostics.Where(diagnostic =>
                        diagnostic.IsWarningAsError ||
                        diagnostic.Severity == DiagnosticSeverity.Error);

                    foreach (Diagnostic diagnostic in failures)
                    {
                        Console.Error.WriteLine("{0}: {1}", diagnostic.Id, diagnostic.GetMessage());
                    }
                    return null;
                }
                else
                {
                    ms.Seek(0, SeekOrigin.Begin);
                    Assembly assembly = Assembly.Load(ms.ToArray());
                    return assembly.GetType($"{originClass.Name}Print");
                }
            }
        }

    }
}
