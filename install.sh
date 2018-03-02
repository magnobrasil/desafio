#/bin/bash

yum update -y
yum install  git curl wget unzip zip python27  -y

curl "https://bootstrap.pypa.io/get-pip.py" -o "get-pip.py"

python get-pip.py


# Baixando e descompactando arquivos necessários no GIT

mkdir /opt/projeto
cd /opt/projeto
wget https://github.com/magnobrasil/desafio/archive/master.zip
unzip master.zip 
cd desafio-master

chmod +x install_full.sh

/opt/projeto/desafio-master/install_full.sh


