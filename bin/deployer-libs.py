# Deplayar um lista de bibliotecas
import os
import sys
from java.io import File
from java.util import Properties
from java.io import FileInputStream
import ConfigParser

if len(sys.argv) < 1:
    print("É necessário informar o arquivo qe possui a lista das libs para deployer")
    exit()
arquivo_libs=sys.argv[1]

dirConf = os.getenv('DIR_CONF_APP')
dirLibsApp = os.getenv('DIR_LIBS_APP')


config = ConfigParser.ConfigParser()
config.read(dirConf + '/' + 'domain.properties')

# Configurações do servidor
user_adm = config.get('server','admin_user')
pass_adm = config.get('server','admin_password')
port_adm = config.get('server','port')
url_adm = 't3://localhost:' + port_adm
server_adm = config.get('server','admin_server')
connect(user_adm,pass_adm,url_adm)

# Abre o arquivo para leitura
arquivo = open(arquivo_libs, 'r')  # sem 'with', sem encoding
try:
    for linha in arquivo:
        linha = linha.strip()
        campos = linha.split(',')
        if len(campos) == 2:
            arquivo_lib, nome_lib = campos
            deploy(appName=nome_lib,
                   path=dirLibsApp + '/'+ arquivo_lib,
                   targets=server_adm,
                   block='true', 
                   upload='false',
                   libraryModule='true')

        else:
            print("Linha inválida:", linha)
except Exception, e:
    print 'Erro durante o deploy: ' + str(e)
    dumpStack()            

arquivo.close()  # fecha o arquivo manualmente
disconnect()
exit()

