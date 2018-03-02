

PROJETO DESAFIO GLOBO.COM

#Pre-requisitos

Baixar e instalar a imagem do CENTOS 7 disponível em um máquina virtual

http://centos.brnet.net.br/centos/7/isos/x86_64/CentOS-7-x86_64-Minimal-1708.iso


#Instruções de instalação
1) Iniciar a maquina virtual com o Centos 7 devidamente instalado

2) Abrir o TERMINAL e logar como root 
comando - sudo -i

3) Com o terminal aberto criar o script "install.sh" copiando todo o campo abaixo e colando no terminal

---------------------------------------------------------

echo "#/bin/bash

yum update -y
yum install  git curl wget unzip zip python27  -y

curl "https://bootstrap.pypa.io/get-pip.py" -o "get-pip.py" && python get-pip.py

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

----------------------------------------------------------
executar o comando abaixo :

chmod +x install.sh && ./install.sh

4) Esperar todos os pacotes serem instalados e a subida de todos os serviços.

-----------------------------------------------------------------------

REALIZANDO TESTES NA API

1) Abra o Postman com o comando - 
 postman

2) Importe o arquivo python-cv.postman_collection.json para o postman e visualize os endpoints

#Para aunternticar

1) Crie uma conta em POST - /register com o corpo {username:nome, password:pass}
2) Receba seu token POST - /auth {username:nome, password:pass} com o seu login e senha criados


Obs:
 Header para autenticar > Authorization JWT <token>
 Somente o endpoint /artigo/:id está com autenticação com o objetivo de facilitar os testes.
  

 


