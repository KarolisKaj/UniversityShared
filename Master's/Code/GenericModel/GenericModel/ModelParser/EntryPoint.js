function runParsing()
{
    console.log('Obtaining mermaid.');
    var mermaid = require('./mermaid');
	mermaid.initialize({ theme: 'forest' });

    console.log('Parsing given model.');
    console.log(JSON.stringify(mermaid.parse('graph TB\ngamintojas--10-->buferis1\nsubgraph komponentas\nbuferis1[buferis]-->procesorius1[procesorius]\nprocesorius1[procesorius]--50-->procesorius1[procesorius]\nend\nprocesorius1--15-->agregatorius\n')));
	console.log(mermaid.parse('graph TB\ngamintojas-->buferis1\nsubgraph komponentas\nbuferis1[buferis]-->procesorius1[procesorius]\nprocesorius1[procesorius]--50-->procesorius1[procesorius]\nend\nprocesorius1--15-->agregatorius\n').parser.yy.getEdges());
    console.log(mermaid);
}

runParsing();