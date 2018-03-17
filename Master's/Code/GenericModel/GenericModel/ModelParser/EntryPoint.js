function runParsing() {
    console.log('[JS] Creating Mermaid Instance...');
    var mermaid = require('./mermaid');
    mermaid.initialize({ theme: 'forest' });
    console.log('[JS] Mermaid Instance Created!');
    console.log("");

    console.log('[JS] Reading Model From File...');
    const fs = require('fs');
    var contents = fs.readFileSync('../Systems.Diagrams/sut.txt', 'utf8');
    console.log('[JS] Model read!');
    console.log("");

    console.log("-----------------MODEL--------------------");
    console.log(contents);
    console.log("-----------------MODEL--------------------");
    console.log("");

    console.log('[JS] Parsing Model...');
    var parsedGraph = mermaid.parse(contents);
    var vertices = JSON.stringify(parsedGraph.parser.yy.getVertices());
    var edges = JSON.stringify(parsedGraph.parser.yy.getEdges());
    var subGraphs = JSON.stringify(parsedGraph.parser.yy.getSubGraphs());
    console.log('[JS] Model Parsed!');

    var path = require("path");
    pythonEntryPoint = path.join(__dirname, '..', 'EntryPoint.py');

    console.log('[JS] Running Python Generic Model...');
    const { execFile } = require('child_process');
    execFile('C:/Program Files (x86)/Microsoft Visual Studio/Shared/Python36_64/python.exe', [pythonEntryPoint, vertices, edges, subGraphs], { maxBuffer: 1024 * 500 }, (error, stdout, stderr) => {
        if (error) {
            console.log('Failed to run python file.');
            throw error;
        }
        console.log(stdout);
        console.log("[JS] Simulation ended successfully!");
    });
}

runParsing();