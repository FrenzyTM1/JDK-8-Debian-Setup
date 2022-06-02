import os
import shutil

os.system('sudo mkdir /usr/lib/jvm')
os.system('cd /usr/lib/jvm')

os.system('cp -r jdk1.8.0_321 /usr/lib/jvm')
os.system('cp environment /etc')

os.system('sudo update-alternatives --install "/usr/bin/java" "java" "/usr/lib/jvm/jdk1.8.0_321/bin/java" 0')

os.system('sudo update-alternatives --install "/usr/bin/javac" "javac" "/usr/lib/jvm/jdk1.8.0_321/bin/javac" 0')

os.system('sudo update-alternatives --set java /usr/lib/jvm/jdk1.8.0_321/bin/java')

os.system('sudo update-alternatives --set javac /usr/lib/jvm/jdk1.8.0_321/bin/javac')

os.system('update-alternatives --list java')

os.system('update-alternatives --list javac')

os.system('java -version')
