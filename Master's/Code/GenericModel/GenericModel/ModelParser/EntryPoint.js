function runParsing() {
    console.log('Creating Mermaid Instance...');
    var mermaid = require('./mermaid');
    mermaid.initialize({ theme: 'forest' });
    console.log('Mermaid Instance Created!');


    console.log('Reading Model From File...');
    const fs = require('fs');
    var contents = fs.readFileSync('../Systems.Diagrams/MapReduce/SimplifiedExample.txt', 'utf8');
    console.log('Model read!');
    console.log("-----------------MODEL--------------------");
    console.log(contents);
    console.log("-----------------MODEL--------------------");

    console.log('Parsing Model...');
    var parsedGraph = mermaid.parse(contents);
    var vertices = JSON.stringify(parsedGraph.parser.yy.getVertices());
    var edges = JSON.stringify(parsedGraph.parser.yy.getEdges());
    var subGraphs = JSON.stringify(parsedGraph.parser.yy.getSubGraphs());
    console.log('Model Parsed!');

    console.log('Running Python Generic Model...');
    const { execFile } = require('child_process');
    execFile('C:/Program Files (x86)/Microsoft Visual Studio/Shared/Python36_64/python.exe', ['C:/Users/WarHorse/SourceControl/UniversityShared/Master\'s/Code/GenericModel/GenericModel/EntryPoint.py', vertices, edges, subGraphs], (error, stdout, stderr) => {
        if (error) {
            console.log('Failed to run python file.');
            throw error;
        }
        console.log(stdout);
        console.log("Simulation ended successfully!");
    });
}

runParsing();