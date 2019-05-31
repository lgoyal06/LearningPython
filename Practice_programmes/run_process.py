import sys
import os
import subprocess
import inspect



# Complete the function below.

def run_process(cmd_args):
    with subprocess.Popen(cmd_args, 
                          stdout=subprocess.PIPE) as process:
        print(process.communicate()[0])

run_process(['python','-c','print("Hello")'])
             
