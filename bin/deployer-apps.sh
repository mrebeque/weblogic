#!/bin/bash
# Script para deploy no WebLogic 10.3.6
# Uso: ./deploy_weblogic.sh <ARQUIVO_DEPLOY> <NOME_APLICACAO>

. ${WL_HOME}/server/bin/setWLSEnv.sh > /dev/null

pathAPP="$DIR_DEPLOY"/"$APP"
while true; do
    mapfile -t ARQUIVOS_INICIAIS < <(find $pathAPP -maxdepth 1   -type f  \( -iname "*.ear" -o -iname "*.war" \))
    qtde=${#ARQUIVOS_INICIAIS[@]}
    echo "Info: Deploy de $qtde apps ....."
		for arquivo in "${ARQUIVOS_INICIAIS[@]}"; do
  
        echo "Info: Iniciando o deply de $arquivo ....."
        arqUpload=$DIR_UPLOAD/$(basename "$arquivo")
        mv $arquivo $arqUpload

        $WL_HOME/common/bin/wlst.sh $DIR_CONF_APP/deployer-apps.py "$arqUpload"

        echo "Info: Deploy de "$(basename "$arquivo")" concluído!"

		done        
    sleep 10 
done
exit 0
