#!/bin/bash
# Script para deploy no WebLogic 10.3.6
# Uso: ./deploy_weblogic.sh <ARQUIVO_DEPLOY> <NOME_APLICACAO>

. ${WL_HOME}/server/bin/setWLSEnv.sh > /dev/null

arquivo_apps="$DIR_CONF_APP/bibliotecas.csv"

if [ -f "$arquivo_apps" ]; then
    total_linhas=$(wc -l < "$arquivo_apps")
else
    total_linhas=0
fi

if [ "$total_linhas" -gt 0 ]; then 
   #Executar script de deploy
   echo "##"
   echo "Info: Iniciando o deply de $total_linhas bibliotecas "
   echo "##"
   $WL_HOME/common/bin/wlst.sh $DIR_CONF_APP/deployer-libs.py "$arquivo_apps"
else
    echo "Warn: Não há bibliotecas registradas para deploy no arquivo $arquivo_apps"
fi
exit 0
