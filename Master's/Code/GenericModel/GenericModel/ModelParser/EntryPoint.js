function runParsing()
{
    alert('die');
    var graph = require('./graphDb');
    var flow = require('./flow');
    flow.parser.yy = graph;
    alert('die');

    flow.parser.parse(text);
    alert('die');
}

