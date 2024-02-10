'''
main.nfs_creator
=========================

This module contains the main functions for the nfs-creator package.
'''

import sys
from nfs_service import NFSService
from cmd_executor import BashExecutor
from package_installer import NFSInstaller
from nfs_installation_checker import NFSInstallChecker

class NFSCreator:
    
    def __init__(self, export_dir: str = '/var/data/'):
        self.export_dir = export_dir
    
    def init_nfs(self):
        ''' A function to create an nfs share. '''
        
        if NFSInstallChecker.is_installed():
            print('✅ : NFS package is already installed!')
        else:
            print('✅ : Installing nfs package...')
            NFSInstaller.install_nfs_package()
        
        NFSService.enable_start_service()
        
        print('✅ : NFS server installed and services enabled/started!')
    
    def create_nfs(self):
        ''' A function to create an nfs share. '''
        
        self.init_nfs()
        
        print('✅ : Creating an nfs share...')
        _, error = BashExecutor.execute_cmd(f'sudo mkdir -p {self.export_dir}')
        if error.decode('utf-8'):
            sys.exit(f'❌ : An error occurred while creating the export directory!. {error.decode("utf-8")}')
        
        _, error = BashExecutor.execute_cmd(f'sudo chmod -R 777 {self.export_dir}')
        if error.decode('utf-8'):
            sys.exit(f'❌ : An error occurred while setting permissions on the export directory!. {error.decode("utf-8")}')
        
        print('✅ : NFS share created successfully!')
    

if __name__ == "__main__":
    pass