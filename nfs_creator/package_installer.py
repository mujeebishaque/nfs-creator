'''
nfs_creator.nfs_installer
==========================

This module contains functions to install the nfs-utils package.
'''

import sys, platform
from nfs_creator.cmd_executor import BashExecutor

class NFSInstaller:
    
    rhel_based = ('CentOS Linux', 'Red Hat Enterprise Linux', 'Fedora')
    rhel_installation_cmd = 'sudo yum install nfs-utils -y'
    
    debian_based = ('Ubuntu', 'Debian', 'Linux Mint')
    debain_installation_cmd = 'sudo apt-get install nfs-common -y'
    
    @staticmethod
    def install_nfs_package():
        ''' A function to install the nfs-utils/common package. '''
        
        if platform.system() == 'Linux':
            
            if platform.linux_distribution()[0] in NFSInstaller.rhel_based:
                
                output, error = BashExecutor.execute_cmd(NFSInstaller.rhel_installation_cmd)
                if 'Complete!' in output.decode('utf-8'):
                    print('✅ : nfs-utils has been installed successfully!')
                if error.decode('utf-8'):
                    sys.exit(f'❌ : An error occurred while installing nfs-utils!. {error.decode("utf-8")}')
                    
                    
            elif platform.linux_distribution()[0] in NFSInstaller.debian_based:
                
                output, error = BashExecutor.execute_cmd(NFSInstaller.debain_installation_cmd)
                if error.decode('utf-8'):
                    sys.exit(f'❌ : An error occurred while installing nfs-common!. {error.decode("utf-8")}')
                print('✅ : nfs-common has been installed successfully!')
                
            else:
                sys.exit('This script is only compatible with RPM-based and Debian-based Linux distributions.')
        
        else:
            sys.exit('Please run this script on a Linux machine.')