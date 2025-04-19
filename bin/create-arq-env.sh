
import os
from java.io import File
from java.util import Properties
from java.io import FileInputStream
import ConfigParser

[java]
JAVA_VENDOR="Sun"
JAVA_INSTALL=/opt/java
JAVA_HOME=/opt/java/jdk1.6.0_45


config = ConfigParser.ConfigParser()

config.read(dirConf + '/' + 'domain.properties')

# Variaveis do weblogic
ORACLE_HOME = config.get('weblogic','ORACLE_HOME')
MDW_HOME = config.get('weblogic','MDW_HOME')
WBL_HOME = config.get('weblogic','WBL_HOME')
WBL_LOGS = config.getint('weblogic','WBL_LOGS')
CMD_WLST = config.getint('weblogic','CMD_WLST')

# Variaveis do DOMAIN
DM_HOME = config.get('domain','DM_HOME')
DM_NAME = config.get('domain','DM_NAME')
DIR_LIBS_CLASSPATH = config.get('domain','DIR_LIBS_CLASSPATH')

# Variaveis do DOMAIN
JAVA_VENDOR = config.get('java','JAVA_VENDOR')
DM_NAME = config.get('JAVA_INSTALL','JAVA_INSTALL')
JAVA_HOME = config.get('java','JAVA_HOME')

# Cria (ou sobrescreve) um arquivo chamado "exemplo.txt"
arquivo = open("~/env_weblogic", "w")
# Escreve algo no arquivo
arquivo.write("export ORACLE_HOME=" + ORACLE_HOME + "\n")
arquivo.write("export MDW_HOME=" + MDW_HOME + "\n")
arquivo.write("export WBL_HOME=" + WBL_HOME + "\n")
arquivo.write("export WBL_LOGS=" + WBL_LOGS + "\n")
arquivo.write("export CMD_WLST=" + CMD_WLST + "\n")
arquivo.write("export MDW_HOME=" + MDW_HOME + "\n")
arquivo.write("export DM_HOME=" + DM_HOME + "\n")
arquivo.write("export DM_NAME=" + DM_NAME + "\n")
arquivo.write("export DM_PATH=" + DM_HOME + "/" DM_NAME + "\n")
arquivo.write("export DIR_LIBS_CLASSPATH=" + DIR_LIBS_CLASSPATH + "\n")
arquivo.write("export JAVA_VENDOR=" + JAVA_VENDOR + "\n")
arquivo.write("export JAVA_HOME=" + JAVA_HOME + "\n")
# Fecha o arquivo
arquivo.close()

profile = open("~/.bashrc", "a")
profile.write(". env_weblogic /n")
profile.close()

