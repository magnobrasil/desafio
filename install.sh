#/bin/bash

yum update -y
yum install  git curl wget unzip zip python27  -y

curl "https://bootstrap.pypa.io/get-pip.py" -o "get-pip.py" && python get-pip.py


# Ambiente Gráfico
yum groupinstall "X Window System" && yum groupinstall "Fonts" && yum install kde-workspace && yum install gdm && unlink /etc/systemd/system/default.target && ln -sf /lib/systemd/system/graphical.target /etc/systemd/system/default.target

reboot -n


#Baixando e descompactando arquivos do GIT

mkdir /opt/projeto
cd /opt/projeto
wget https://github.com/magnobrasil/desafio/archive/master.zip
unzip master.zip 
cd desafio-master

chmod +x install_full.sh

/opt/projeto/desafio-master/install_full.sh" > install.sh
