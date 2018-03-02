#/bin/bash

echo "#################################"
echo "#                 							#"
echo "#	  Script de configuração		  #"
echo "#               								#"
echo "#   Criado por Magno Brasil		  #"
echo "#					                			#"
echo "#################################"


#Verificar o usuário root

if [ $USER == root ];
then 
echo "#############################################"
echo "########## INICIANDO SCRIPT #################"
echo "#############################################"

else 

echo "#############################################"
echo "######### ERROR ! ERROR ! ERROR ! ###########"
echo "#### EXECUTE O SCRIPT COM O USUÁRIO ROOT ####"
echo "#############################################"

fi


echo "#############################################"
echo "#												                    #"
echo "#	1º Responder ao endereço avaliacao.com		#"
echo "#												                    #"
echo "#############################################"

mv /etc/hosts /etc/hosts.bkp
echo "127.0.0.1 avaliacao.com localhost" > /etc/hosts


echo "#############################################"
echo "#                   												#"
echo "#	          2º Instalar o DCOCKER						#"
echo "#                   												#"
echo "#############################################"


#Script Instalação do DOCKER.

curl -fsSL https://get.docker.com/ | sh 


#Iniciando

sudo systemctl start docker 

sudo systemctl enable docker  


docker build -t siteprojeto .

docker run --name apacheubuntu01 -p 80:80 -p 443:443 -d siteprojeto

cd /opt/projeto/desafio-master/

pip install -r requirements.txt

python main.py &


chmod +x postman.sh

/opt/projeto/desafio-master/postman.sh

postman &


