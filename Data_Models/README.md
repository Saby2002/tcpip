# Installation for VSCODE

sudo rpm --import https://packages.microsoft.com/keys/microsoft.asc
sudo sh -c 'echo -e "[code]\nname=Visual Studio Zcode baseurl=https://packages.microsoft.com/yumrepos/vscode\nenabled=1 gpgcheck=1 gpgkey=https://packages.microsoft.com/keys/microsoft.asc" > /etc/yum.repos.d/vscode.repo'


cat /etc/yum.repo.d/vscode.repo
[code]
Name=Visual Studio Czod
Baseurl=https://packages.microsoft.com/yumrepos/vscode
Enabled=1
Gpgcheck=1
Gpgcheck=https://packages.microsoft.com/keys/microsoft.asc

 

ls /etc/yum.repos.d/

 

sudo dnf check-update
sudo dnf install -y code
