CLI exercise
------------

1. Run the given `cli_exercise.py` script with different command line options and arguments. Observe the output printed by the script and study how the options and arguments are represented in the opts and args variables. 

2. Uncomment the rest of the script (remove the two """ lines), and study how options and arguments are processed.

3. Run the script by executing the following commands:

`python3 cli_exercise.py`
`python3 cli_exercise.py -h`
`python3 cli_exercise.py i.txt 1234`
`python3 cli_exercise.py -o o.txt i.txt 1234`
`python3 cli_exercise.py -o o.txt i.txt` 
`python3 cli_exercise.py -e o.txt i.txt`
`python3 cli_exercise.py -o -o o.txt i.txt 1234`

Is the behavior of the script consistent with what you inferred from the code?

4. Solve the task given at the end of the script under the comment marked as TASK.

5. Extend the script with a new option `-d` (and `--decode`), which would tell the program that instead of encrypting (which sould be the default operation), it should perform a decryption. 

These are the steps you have to do:

- define a variable called `operation` to store whether the program should 'encode' or 'decode'
- as the default should be 'encode', set variable `operation` to `'encode'` and change it to `'decode'` if option `-d` (or `--decode`) is present in the command line
- update the processing of the options in the `for` loop to implement the above described behavior 
- add the new option to the parameters of function `getopt`
- update the usage strings printed as a help
- print out the value of variable `operation` at the end of the script
