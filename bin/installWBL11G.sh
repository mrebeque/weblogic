#!/bin/bash
# Rebeque
# 17/04/2025
# Instalador do weblogic 11g

userInstall=$1
pwdUser=$2

yum update
yum install libnsl -y
yum install -y sshpass


DIR_JAVA=/opt/java
HOST_INSTALL=drhel8labplat001v.sefnet.rj

./adicionarHostInstall.sh "$HOST_INSTALL"
groupadd --gid 1013 oinstall
useradd  --uid 1010 -m -g oinstall -s /bin/bash oracle -p oracle
mkdir -p /opt/oracle/middleware/user_projects/domains
chown -R oracle:oinstall /opt/oracle 
chmod -R 775 /opt/oracle

# Download dos binários do weblogic 11c (10.3.6)
export ORACLE_HOME=/opt/oracle
sshpass -p $pwdUser scp -r $userInstall@$HOST_INSTALL:/var/binarios/weblogic/11g  $ORACLE_HOME/ &&
 chown -R oracle:oinstall $ORACLE_HOME && \
 chmod -R 775 $ORACLE_HOME
 
# Download / Instalar o JAVA JDK 1.6 default do weblogic 11c (10.3.6)
mkdir -p $DIR_JAVA && \
 sshpass -p $pwdUser scp $userInstall@d@$HOST_INSTALL:/var/binarios/jdk/jdk1.6.0_45/jdk-6u45-linux-x64.bin $DIR_JAVA/ && \
 cd $javaInstall && \
 ./jdk-6u45-linux-x64.bin && \
 rm -f jdk-6u45-linux-x64.bin 

export JAVA_HOME=$javaInstall/$(ls -1)
export PATH=$JAVA_HOME/bin:$PATH

echo "export ORACLE_HOME=$ORACLE_HOME" >> /home/oracle/.bashrc
echo "export JAVA_HOME=$JAVA_HOME" >> /home/oracle/.bashrc
echo "export MW_HOME=$ORACLE_HOME/middleware" >> /home/oracle/.bashrc
echo "export PATH=$JAVA_HOME/bin:$PATH" >> /home/oracle/.bashrc
echo "export CMD_WLST='$JAVA_HOME/bin/java $JAVA_OPTIONS -Xmx2048m -XX:MaxPermSize=1024m weblogic.WLST'" >> /home/oracle/.bashrc

su - oracle -c "java -jar $ORACLE_HOME/11g/10.3.6/wls1036_generic.jar -mode=silent -silent_xml=$ORACLE_HOME/11g/install.xml" 

