#/bin/bash

yum update -y
yum install  git curl wget unzip zip python27  -y

curl "https://bootstrap.pypa.io/get-pip.py" -o "get-pip.py" && python get-pip.py


#Descomentar a linha abaixo caso a instalação seja a versão minima

#yum groupinstall "X Window System" -y && yum groupinstall "Fonts" -y && yum install kde-workspace -y && yum install gdm -y && unlink /etc/systemd/system/default.target && ln -sf /lib/systemd/system/graphical.target /etc/systemd/system/default.target && reboot -n

#Baixando e descompactando arquivos do GIT

mkdir /opt/projeto
cd /opt/projeto
wget https://github.com/magnobrasil/desafio/archive/master.zip
unzip master.zip 
cd desafio-master

chmod +x install_full.sh

/opt/projeto/desafio-master/install_full.sh
