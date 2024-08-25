## Description
NFS creator (creates an NFS export/share/dir) is a utility package that can be installed via pip. it is used to install NFS tools/server, create, test, export NFS disk. All by using a single command mentioned above. 

## Installation
```pip install nfs-creator```

## Usage
```
from nfs_creator import nfs_creator
nfs_creator() # by default the nfs export would be created at /var/data/

# provide a custom path
nfs_creator('/var/application')
```


## Test and Deploy

#### A common error:


❌ : exportfs failed!. exportfs: duplicated export entries:

```
exportfs:       *:/var/data
exportfs:       *:/var/data
```

To fix the above error, edit this file and remove the newly added entries: 
```
sudo vi /etc/exports
```

Tested on Ubuntu and CentOS Stream 8.


## Authors and acknowledgment
@mujeebishaque 

## License
General Public Only. No commercial or company use.

## Project status
Complete - Open for improvements.
