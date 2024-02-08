'''
nfs_creator.nfs_installer
==========================

This module contains functions to install the nfs-utils package.
'''
import subprocess

class NFSInstaller:
    
    @staticmethod
    def install_nfs(operating_system: str):
        ''' Install the nfs-utils package on the system. '''
        
        if operating_system in ('CentOS Linux', 'Red Hat Enterprise Linux', 'Fedora'):
            print('Installing nfs-utils package...')
            out, _ = subprocess.Popen(['sudo', 'yum', 'install', 'nfs-utils', '-y'], stdout=subprocess.PIPE, stderr=subprocess.PIPE).communicate()
            print(out.decode('utf-8'))
            print('nfs-utils package installed successfully!')
            
        elif operating_system in ('Ubuntu', 'Debian', 'Linux Mint'):
            print('Installing nfs-common package...')
            out, _ = subprocess.Popen(['sudo', 'apt-get', 'install', 'nfs-common', '-y'], stdout=subprocess.PIPE, stderr=subprocess.PIPE).communicate()
            print(out.decode('utf-8'))
            print('nfs-common package installed successfully!')
            
        else:
            print('This script is only compatible with RPM-based and Debian-based Linux distributions.')
            return None