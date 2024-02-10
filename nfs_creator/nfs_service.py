'''
nfs_creator.check_running
==========================

This module contains functions to check if the nfs service is running.
'''

import sys
from cmd_executor import BashExecutor
from package_installer import CURRENT_OS, RHEL_BASED_OS, DEBIAN_BASED_OS
from nfs_creator.nfs_installation_checker import NFSInstallChecker


class NFSService:
    ''' Enable and run the service on the system.'''
    
    debian_start_cmd = "sudo systemctl start nfs-kernel-server"
    debian_enable_cmd = "sudo systemctl enable nfs-kernel-server"
    
    rhel_start_cmd = "sudo systemctl start nfs-server"
    rhel_enable_cmd = "sudo systemctl enable nfs-server"
    
    
    @staticmethod
    def enable_start_service():
        
        if NFSInstallChecker.is_installed():
            
            if CURRENT_OS in DEBIAN_BASED_OS:
                
                output, error = BashExecutor.execute_cmd(NFSService.debian_start_cmd)
                if error.decode('utf-8'):
                    sys.exit("❌ Error starting nfs-kernel-server: ", error)
                output, error = BashExecutor.execute_cmd(NFSService.debian_enable_cmd)
                if error.decode('utf-8'):
                    sys.exit("❌  Error enabling nfs-kernel-server: ", error)
            
            elif CURRENT_OS in RHEL_BASED_OS:
                output, error = BashExecutor.execute_cmd(NFSService.rhel_start_cmd)
                if error.decode('utf-8'):
                    sys.exit("❌ Error starting nfs-server: ", error)
                output, error = BashExecutor.execute_cmd(NFSService.rhel_enable_cmd)
                if error.decode('utf-8'):
                    sys.exit("❌ Error enabling nfs-server: ", error)
            
            else:
                sys.exit("  This script is only compatible with RPM-based and Debian-based Linux distributions.")
        