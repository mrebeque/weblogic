## /bin/bash
## create-domain.sh

#Carregar variaveis de ambiente do weblogic.
. $MW_HOME/wlserver_10.3/common/bin/commEnv.sh

#Executar script de criação do dominio
$WL_HOME/common/bin/wlst.sh $DIR_CONF_APP/create-domain.py 

#Copiar bibliotecas customizadas.
mkdir -p $DM_HOME/$DM_NAME/servers/AdminServer/upload/
cp $WORKDIR/libs/*  $DM_HOME/$DM_NAME/lib/



