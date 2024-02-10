'''
nfs_creator.nfs_installer
==========================

This module contains functions to install the nfs-utils package.
'''

import sys, platform
from nfs_creator.cmd_executor import BashExecutor

RHEL_BASED_OS   = ('CentOS Linux', 'Red Hat Enterprise Linux', 'Fedora')
DEBIAN_BASED_OS = ('Ubuntu', 'Debian', 'Linux Mint')

try:
    CURRENT_OS = platform.linux_distribution()[0]
except AttributeError as e:
    sys.exit('ERROR: This script is only compatible with Linux distributions.')
    
class NFSInstaller:
    
    rhel_installation_cmd = 'sudo yum install nfs-utils -y'
    debain_installation_cmd = 'sudo apt-get install nfs-common -y'
    
    @staticmethod
    def install_nfs_package():
        ''' A function to install the nfs-utils/common package. '''
        
        if platform.system() == 'Linux':
            
            if CURRENT_OS in RHEL_BASED_OS:
                
                output, error = BashExecutor.execute_cmd(NFSInstaller.rhel_installation_cmd)
                if error.decode('utf-8'):
                    sys.exit(f'❌ : An error occurred while installing nfs-utils!. {error.decode("utf-8")}')
                print('✅ : nfs-utils has been installed successfully!')
                
            elif CURRENT_OS in DEBIAN_BASED_OS:
                
                output, error = BashExecutor.execute_cmd(NFSInstaller.debain_installation_cmd)
                if error.decode('utf-8'):
                    sys.exit(f'❌ : An error occurred while installing nfs-common!. {error.decode("utf-8")}')
                print('✅ : nfs-common has been installed successfully!')
                
            else:
                sys.exit('This script is only compatible with RPM-based and Debian-based Linux distributions.')
        
        else:
            sys.exit('Please run this script on a Linux machine.')