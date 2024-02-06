'''
nfs_creator.check_running
==========================

This module contains functions to check if the nfs service is running.
'''
import subprocess

class NFSServiceChecker:
    ''' A class to check if the nfs service is running. '''
    
    @staticmethod
    def is_running():
        out, _ = subprocess.Popen(['systemctl', 'is-active', 'nfs'], stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True).communicate()
        
        if 'inactive' in str(out):
            print("❌ : nfs service is not running!")
            return False
        return True