#Criar um dominio

import os
from java.io import File
from java.util import Properties
from java.io import FileInputStream
import ConfigParser

# Ler variaveis 
wl_home = os.getenv('WL_HOME')
domain_home = os.getenv('DM_HOME')
domain_name = os.getenv('DM_NAME')
domain_path =os.getenv('DM_PATH')
dirConf = os.getenv('DIR_CONF_APP')

config = ConfigParser.ConfigParser()

config.read(dirConf + '/' + 'domain.properties')

# Configurações do servidor
user_adm = config.get('server','admin_user')
pass_adm = config.get('server','admin_password')
admin_port = config.getint('server','port')

# Iniciando a criação do domínio
template_path = wl_home+'/common/templates/domains/wls.jar'
readTemplate(template_path)

# Configurando o nome do domínio
cd('Servers/AdminServer')
set('ListenAddress', '')
set('ListenPort', admin_port)

# Configurando as credenciais do administrador
cd('/Security/base_domain/User/weblogic')
cmo.setName(user_adm)
cmo.setPassword(pass_adm)
# Definindo modo de operação para PRODUÇÃO
cd('/')
cmo.setProductionModeEnabled(true)

# Criando o domínio
setOption('OverwriteDomain', 'true')

writeDomain(domain_path)
closeTemplate()

print('Domínio ' + domain_name + ' criado com sucesso em ' + domain_path)

exit()


