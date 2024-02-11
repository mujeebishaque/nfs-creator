'''
nfs_creator.firewall_settings
=============================

This module contains functions to configure the firewall settings for the nfs service.
'''

import sys
from nfs_creator.cmd_executor import BashExecutor


def configure_firewall_nfs():
    ''' A function to configure the firewall settings for the nfs service. '''
    
    print('⚠ : Attemping to install firewalld ...')
    
    _, _ = BashExecutor.execute_cmd('sudo apt install firewalld -y')
    
    
    print('⚠ : Configuring firewall settings...')
    
    
    _, _ = BashExecutor.execute_cmd('sudo firewall-cmd --add-service=nfs --permanent')
    _, _ = BashExecutor.execute_cmd('sudo firewall-cmd --add-service=mountd --permanent')
    _, _ = BashExecutor.execute_cmd('sudo firewall-cmd --add-service=rpc-bind --permanent')
    _, error = BashExecutor.execute_cmd('sudo firewall-cmd --reload')
    
    if error.decode('utf-8'):
        sys.exit(f'❌ : An error occurred while adding the nfs service to the firewall!. {error.decode("utf-8")}')
    
    _, error = BashExecutor.execute_cmd('sudo firewall-cmd --reload')
    if error.decode('utf-8'):
        sys.exit(f'❌ : An error occurred while reloading the firewall!. {error.decode("utf-8")}')
    
    print('✅ : Firewall settings configured successfully!')