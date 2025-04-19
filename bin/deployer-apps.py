#Deployar uma app

import os
import sys
from java.io import File
from java.util import Properties
from java.io import FileInputStream
import ConfigParser

# Ler variaveis
dir_conf = os.getenv('DIR_CONF_APP')

sys.path.insert(0,dir_conf)
from libsServer import getAppName
from libsServer import statusAsString

appPath=sys.argv[1]
nomeApp = getAppName(appPath)

config = ConfigParser.ConfigParser()
config.read(dir_conf + '/' + 'domain.properties')
user_adm = config.get('server','admin_user')
pass_adm = config.get('server','admin_password')
port_adm = config.get('server','port')
url_adm = 't3://localhost:' + port_adm
target_server = config.get('server','admin_server')
connect(user_adm,pass_adm,url_adm)

try:
   try:
      appExists = False
      domainConfig()
      apps = cmo.getAppDeployments()
      for app in apps:
          if app.getName() == nomeApp:
              print('Aplicacao ' +  nomeApp+ ' encontrada!')
              appExists = True
              break

      if appExists:
           domainRuntime()
           appRuntime = getMBean('/AppRuntimeStateRuntime/AppRuntimeStateRuntime')
           state = appRuntime.getCurrentState(nomeApp, target_server)

           print 'Realizando undeploy da aplicação ' + nomeApp + '...'
           if state == 0:
              print 'Parando aplicação ' + nomeApp + '...'
              stopApplication(nomeApp)

           serverConfig()
           undeploy(nomeApp, timeout=60000)
           print 'Undeploy realizado com sucesso!'

      serverConfig()
      progress = deploy(appName=nomeApp,
                        path=appPath,
                        targets=target_server,
                        block='true',
                        upload='false',
                        libraryModule='false',
                        timeout=60000)
      if progress.isCompleted():
         print 'Deploy realizado com sucesso!'
      else:
         print 'Erro no deploy: ' + progress.getMessage()
   except Exception, e:
      print 'Erro durante o deploy: ' + str(e)
      dumpStack()
finally:
    disconnect()
    exit()

