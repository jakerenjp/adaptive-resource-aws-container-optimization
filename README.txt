Adaptive Resource AWS Container Optimization
See "Term Project" PDF for more info.

How to build/run.

Our code requires download of a few Python modules. These Python modules include scipy, matplotlib, and pulp. These can be installed via the command line with the command:
python -m pip install --user scipy matplotlib pulp
If this command does not work due to the version of python, use:
python3 -m pip install --user scipy matplotlib pulp
To run our simulation, navigate to the simulation folder and run this command in the terminal:
python simulation.py <file located in inputfiles/conatinerDeployment> <file located in inputfiles/conatinerStats> <output file>
where the output file should be located in the output folder. Note that each file must be located in the specific folder.
In addition, if this command does not work due to the version of python, use: 
python3 simulation.py <file located in inputfiles/conatinerDeployment> <file located in inputfiles/conatinerStats> <output file>
In the main program, the input file of Schedule.json must be located in the folder path:
simulation/inputFiles/ContatinerDeployment/
and the input file of Containers.json must be located in the folder path:
simulation/inputFiles/ContatinerStats/
which is where our code reads.

For our test data, we directly created test sample data in a file called testdata.json
In order to test for other data, this json file must be directly editted, and the file must be located in the same path folder.

Note that the files should already be saved in the correct locations.
