'''
utils.cmd_executor
===================

This module contains the static class responsible for executing bash commands and returning the output and error. 
Return Type: Tuple
'''

import subprocess

class BashExecutor:

    @staticmethod
    def execute_cmd(_cmd):
        _p = subprocess.Popen(_cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
        
        # returns output, error tuple
        return _p.communicate()
        

if __name__ == '__main__':
    b = BashExecutor()
