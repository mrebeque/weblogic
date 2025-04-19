import os
from java.io import File
from java.util import Properties
from java.io import FileInputStream
import ConfigParser

dirConf = os.getenv('DIR_CONF_APP')
config = ConfigParser.ConfigParser()
config.read(dirConf + '/' + 'domain.properties')

# Configurações do servidor
user_adm = config.get('server','admin_user')
pass_adm = config.get('server','admin_password')
port_adm = config.get('server','port')
url_adm = 't3://localhost:' + port_adm
serverName = config.get('server','admin_server')

# Conectando ao servidor de administração
connect(user_adm, pass_adm, url_adm)

edit()
startEdit()

# Nome do servidor e target
jmsServerName = 'CDIJMSServer'
jmsModuleName = 'SystemModuleCDI'
subDeployment = 'CDISubdeployment'
connFactory   = 'FabricaConexoes'
queueName     = 'CDIQueue'
queueJndi	    = 'jms/CDI/Queue'

# Criar JMS Server
cd('/')
cmo.createJMSServer(jmsServerName)
target = getMBean('/Servers/' + serverName)
cd('/JMSServers/' + jmsServerName)
set('Targets', jarray.array([target], Class.forName('weblogic.management.configuration.TargetMBean')))

# Criar JMS Module
cd('/')
cmo.createJMSSystemResource(jmsModuleName)
cd('/JMSSystemResources/' + jmsModuleName)
target = getMBean('/Servers/' + serverName)
set('Targets', jarray.array([target], Class.forName('weblogic.management.configuration.TargetMBean')))

# Criar subdeployment
cd('/JMSSystemResources/' + jmsModuleName)
cmo.createSubDeployment(subDeployment)

# Criar Connection Factory
cd('/JMSSystemResources/' + jmsModuleName + '/JMSResource/' + jmsModuleName)
cmo.createConnectionFactory(connFactory)

cd('ConnectionFactories/' + connFactory)
cmo.setJNDIName('jms/' + connFactory)
cmo.setSubDeploymentName(subDeployment)

# Criar fila (Queue)
cd('/JMSSystemResources/' + jmsModuleName + '/JMSResource/' + jmsModuleName)
cmo.createQueue(queueName)

cd('Queues/' + queueName)
cmo.setJNDIName(queueJndi)
cmo.setSubDeploymentName(subDeployment)

# Associar o subdeployment ao JMS Server
cd('/JMSSystemResources/' + jmsModuleName + '/SubDeployments/' +subDeployment)
target = getMBean('/JMSServers/' + jmsServerName)
set('Targets', jarray.array([target], Class.forName('weblogic.management.configuration.TargetMBean')))

# Salvar e ativar as mudanças
save()
activate()

# Desconectar
disconnect()
exit()

