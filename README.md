# Usage #
* For each puzzle, download the puzzle input from the following website ```http://adventofcode.com/2017/day/<Puzzle No>/input``` where ```<Puzzle No>``` is the day the puzzle was released (1 to 25)
    
* Save the input as "input.txt" in the same folder as the day. You now should have 2 files in the folder:
            ```<puzzlename>.py```, which is the python file, and ```input.txt```
            
* Next, open your command prompt in the folder, and run the following command:
```Batchfile
python <puzzlename>.py
```         
    
* The answer should appear in the following format:
```Batchfile
Part 1: <answer>
Part 2: <answer>
```
for days 1 - 24, and:
```Batchfile        
Answer: <answer>
```
for day 25.
            
Some puzzles have runtimes which are super long, but if nothing happens after 5 minutes or so, there's probably a problem with the code.
        
# Known Issues #
    1)  Because of the somewhat customised nature of puzzle inputs, the solutions here work 100% for my set of inputs, but may not work for other inputs.
        If the solutions break on some inputs, add is as an issue and I will find some time to solve it if I can
    2)  Because of the verbose nature of Day 25, it only works for the input that I received.
    
# TODO List #
    1)  Automate Day 25
    2)  Create a main python file to run all the solutions from, and add runtime documentation
    3)  Include the runtime for each solution in this README
    4)  Start working on AoC 2016 and earlier.