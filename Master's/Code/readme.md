Generic model!
===================


Project created as my **master thesis** practical part. It contains code which translates mermaid conceptual model into working simulation.

----------

How do I run it?
-------------------
Navigate ModelParser folder in the project. Then you want to run following in command line:
>`node EntryPoint.js`

You will also need Node.js installed on your machine as well as python 3.x.

Conceptual model documentation
-------------

All information about model is taken from mermaid defined model. Following information gives you an idea how you can modify model to achieve wanted results:

- Components
	- !dr - death rate i.e. `dr0.01` from 0 to 1 probability of death to occur;
	- !to - time out i.e. `to50`;
	- !cl - clone times i.e. `cl3`. That will spawn three nodes of that particular component;      
	- !rr - recovery rate i.e. `rr0.3`. Component has a chance to recover each turn;        
