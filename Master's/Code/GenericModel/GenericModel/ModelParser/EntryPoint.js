function runParsing()
{
    //var mermaid = require('./CoreParse/mermaid.min');
    //console.log(mermaid.parse('graph TB'+
    //'gamintojas--10--> buferis1'+
    //'subgraph komponentas'+
    //'buferis1[buferis]--> procesorius1[procesorius]'+
    //'procesorius1[procesorius]--50--> procesorius1[procesorius]'+
    //'end'+
    //'procesorius1--15--> agregatorius'));
    console.log('die');

    var graph = require('./graphDb');
    var flow = require('./flow');
    //flow.parser.yy = graph;

    //console.log('die');
    //flow.parser.parse("");
}

runParsing();
