'''
nfs_creator.check_install
==========================

This module contains functions to check if the nfs-utils is installed.
'''

import sys, subprocess
from nfs_creator.package_installer import (
    CURRENT_OS, RHEL_BASED_OS, DEBIAN_BASED_OS
    )

class NFSInstallChecker:
    ''' A class to check if the nfs-utils package is installed. '''
    
    @staticmethod
    def is_installed():
        
        if CURRENT_OS in RHEL_BASED_OS:
    
            out, _ = subprocess.Popen(['rpm -q nfs-utils'], stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True).communicate()
    
            if 'not' in str(out):
                print("❌ : nfs-utils is not installed on this system!")
                return False
            return True
            
        elif CURRENT_OS in DEBIAN_BASED_OS:
    
            out, _ = subprocess.Popen(['dpkg -s nfs-common | grep Status'], stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True).communicate()

            if 'not installed' in str(out):
                print("❌ : nfs-common not installed on this system!")
                return False
            return True
        
        else:
            sys.exit('This script is only compatible with RPM-based and Debian-based Linux distributions.')
                    
