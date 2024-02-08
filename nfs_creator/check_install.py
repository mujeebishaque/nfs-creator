'''
nfs_creator.check_install
==========================

This module contains functions to check if the nfs-utils is installed.
'''

import platform, subprocess

class NFSInstallChecker:
    ''' A class to check if the nfs-utils package is installed. '''
    
    @staticmethod
    def is_linux():
        return platform.system() == 'Linux'
    
    @staticmethod
    def is_installed():
        if NFSInstallChecker.is_linux():
            if platform.linux_distribution()[0] in ('CentOS Linux', 'Red Hat Enterprise Linux', 'Fedora'):
        
                out, _ = subprocess.Popen(['rpm -q nfs-utils'], stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True).communicate()
        
                if 'not' in str(out):
                    print("❌ : nfs-utils is not installed on this system!")
                    return False
                return True
                
            elif platform.linux_distribution()[0] in ('Ubuntu', 'Debian', 'Linux Mint'):
        
                out, _ = subprocess.Popen(['dpkg -s nfs-common | grep Status'], stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True).communicate()

                if 'not installed' in str(out):
                    print("❌ : nfs-common not installed on this system!")
                    return False
                return True
            
            else:
                print('This script is only compatible with RPM-based and Debian-based Linux distributions.')
                return None
        
        return None
        
