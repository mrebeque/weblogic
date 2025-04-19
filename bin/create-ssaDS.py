# ==============================================
# Script WLST para criar DataSource no WebLogic 10.3.6
# Uso: wlst.sh create_datasource.py
# ==============================================

import os
from java.io import File
from java.util import Properties
from java.io import FileInputStream
import ConfigParser

config = ConfigParser.ConfigParser()

dirConf = os.getenv('DIR_CONF_APP')
config.read(dirConf + '/' + 'domain.properties')

# Configurações do servidor
user_adm = config.get('server','admin_user')
pass_adm = config.get('server','admin_password')
port_adm = config.get('server','port')
url_adm = 't3://localhost:' + port_adm

# Configurações do DataSource
ds_name = 'ssaDS'
jndi_name = 'ssaDS'
driver = 'oracle.jdbc.OracleDriver'
url = 'jdbc:oracle:thin:@sef01b_scan.sefnet.rj:1521/srv_sef01b.sefnet.rj'
user = 'ssa_usr'
password = 'ssa_usr'
targets = 'AdminServer'  
# Pode ser uma lista: ['AdminServer', 'Cluster1']

# Tamanho do pool de conexões
initial_capacity = 2
max_capacity = 10
capacity_increment = 2
reserve_timeout = 10
teste_connection = True
shrink_frequency = 900
test_table = 'SQL SELECT 1 FROM DUAL' 

connect(user_adm,pass_adm,url_adm)

###
# Iniciar verificaçã da existência do DATAOURCE ssaDS
###

domainConfig()
allDS = cmo.getJDBCSystemResources()
existe = False
for ds in allDS:
    if ds.getName() == ds_name:
        existe = True
        break

if existe:
  print('DataSource "' + ds_name +'" existe.')
  disconnect()
  exit()   
else:
  print('DataSource "' + ds_name + '" não foi encontrado. Será criado!')
  
###
# Iniciar criação do DATAOURCE ssaDS
###

edit()
startEdit()
# criar o DataSource
cd('/')
cmo.createJDBCSystemResource(ds_name)

cd('/JDBCSystemResources/'+ds_name+'/JDBCResource/'+ds_name)
cmo.setName(ds_name)

# definir as propriedades principais
cd('/JDBCSystemResources/'+ds_name+'/JDBCResource/'+ds_name+'/JDBCDataSourceParams/'+ds_name)
set('JNDINames', jarray.array([ds_name], String))

# configurar a URL de conexão, driver e credenciais
cd('/JDBCSystemResources/'+ds_name+'/JDBCResource/'+ds_name+'/JDBCDriverParams/'+ds_name)
cmo.setUrl(url)
cmo.setDriverName(driver)
cmo.setPassword(password)

# propriedades do driver (usuário do banco)
cd('/JDBCSystemResources/'+ds_name+'/JDBCResource/'+ds_name+'/JDBCDriverParams/'+ds_name+'/Properties/'+ds_name)
cmo.createProperty('user')

cd('/JDBCSystemResources/'+ds_name+'/JDBCResource/'+ds_name+'/JDBCDriverParams/'+ds_name+'/Properties/'+ds_name+'/Properties/user')
cmo.setValue(user)

# configuração do pool de conexões
cd('/JDBCSystemResources/'+ds_name+'/JDBCResource/'+ds_name+'/JDBCConnectionPoolParams/'+ds_name)
# Define o número inicial de conexões
cmo.setInitialCapacity(initial_capacity)

# Define o número máximo de conexões
cmo.setMaxCapacity(max_capacity)

# Define quantas conexões o pool deve adicionar por vez quando precisar
cmo.setCapacityIncrement(capacity_increment)

# (Opcional) Configura o tempo de espera para obter uma conexão
cmo.setConnectionReserveTimeoutSeconds(reserve_timeout)

cmo.setShrinkFrequencySeconds(shrink_frequency)  # a cada 15 minutos
cmo.setTestConnectionsOnReserve(teste_connection)  # testar conexão antes de entregar pro app
cmo.setTestTableName(test_table)

# definir o target (por exemplo, AdminServer)
cd('/JDBCSystemResources/'+ds_name)
set('Targets', jarray.array([ObjectName('com.bea:Name='+targets+',Type=Server')], ObjectName))

# salvar e ativar as mudanças
save()
activate()
print('==============================================')
print('DataSource criado com sucesso!')
print('Nome: ' + ds_name)
print('JNDI: ' + jndi_name)
print('==============================================')
disconnect()
exit()

