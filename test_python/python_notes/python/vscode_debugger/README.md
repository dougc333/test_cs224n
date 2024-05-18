vscode debugger launch.json doesnt work unless you reference the launch file installed by pip under venv/bin/yourscipts instead of the yourscripts.py file vscode is editing. 

test using command in args:[] and debug open file

${workspaceFolder}/venv_vscode/bin/yourscripts
args:['train']

This does not work:
   {
      "name": "Python: Current File (Integrated Terminal)",
      "type": "python",
      "request": "launch",
      "program": "${workspaceFolder}/subcommands/y.py",
      "console": "integratedTerminal"
    },

This does not work:
args:['train']
but this does:
args:["--console-file", "aaaa", "train"]
Note how the argument for the first command is before the subcommand train

Note: the first command only executes if the subcommand is also correct and is not in error. 

set breakpoint in main() of y.py
when we run teh commnnd normally >y without the train subcommand we dont get the print
statemnt in main() and the train subcommand. We just get teh help menu: 

(venv_vscode) dougchang@Dougs-MacBook-Pro:~/TDS/python/vscode_debugger/subcommands$ y
Usage: y [OPTIONS] COMMAND [ARGS]...

Options:
  --config-file TEXT
  --config-json TEXT
  --config-module TEXT  python module that contains the config object
  --help                Show this message and exit.

Commands:
  train

But when we run >y train awe get the correct output and the functions execute>
  train
(venv_vscode) dougchang@Dougs-MacBook-Pro:~/TDS/python/vscode_debugger/subcommands$ y train
main
init running
train subcommand a_option: 

so this means we need to get the subcommand train correct for the debugger to execute the main() and train() functions
and if train() doesnt execute then main() doesnt execute eiteher. 


One way to solve this which is not on websearch sites is to modify y. click() and setuptools copys y which is a python program 
to an executable under venv/bin/y so modify this by adding "train" or the 
subcommand to the sys.argv list. Cant rely on args in vscode to append to 
sys.argv since it cant do so when the process is under control of click and setuptools
