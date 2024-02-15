# wimex-nfs

## Name
WIMEX NFS creator.

## Test and Deploy

❌ : exportfs failed!. exportfs: duplicated export entries:
exportfs:       *:/var/data
exportfs:       *:/var/data

To fix the above error, edit this file and remove the newly added entries: 
```sudo vi /etc/exports```
Remove the lines added at the bottom. Both of the duplicate entries.

Tested on Ubuntu and CentOS Stream 8.

## Description
Wimex NFS creator is a utility package that can be installed via pip. It's used to test the host system of installation of nfs utility tools and check if the services are running. It's responsible to install NFS if it's not already installed. It's also responsible to create an NFS export.

## Installation
```sudo pip3 install nfs-creator```

## Usage
Use examples liberally, and show the expected output if you can. It's helpful to have inline the smallest example of usage that you can demonstrate, while providing links to more sophisticated examples if they are too long to reasonably include in the README.

## Authors and acknowledgment
Show your appreciation to those who have contributed to the project.

## License
For open source projects, say how it is licensed.

## Project status
Complete - Open for improvements.