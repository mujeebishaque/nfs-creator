'''
nfs_creator.open_permissions
============================

This module contains functions to open permissions on the nfs export directory.
'''
from nfs_creator.cmd_executor import BashExecutor
import sys

def nobody_permissions(export_dir: str):
    ''' A function to open permissions on the nfs export directory. '''
    
    
    print('ℹ : Opening permissions on the export directory...')
    _, error = BashExecutor.execute_cmd(f'sudo chmod -R 777 {export_dir}')
    if error.decode('utf-8'):
        sys.exit(f'❌ : An error occurred while setting permissions on the export directory!. {error.decode("utf-8")}')
    
    _, error = BashExecutor.execute_cmd(f'sudo chown -R nobody:nogroup {export_dir}')
    if error.decode('utf-8'):
        sys.exit(f'❌ : An error occurred while changing owner to nobody:nogroup on the export directory!. {error.decode("utf-8")}')
    
    print('✅ : Permissions for NFS export dir set successfully!')
    
    return True