import paramiko
import paramiko.client

def __runCommand(self, command: str, sudo: bool = False):

    # host = "192.168.0.230"
    # username = "thiago-freire"
    # password = "Gilmara071327"

    host = "192.168.200.116"
    username = "viplab"
    password = "viplab321"

    client = paramiko.client.SSHClient()

    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    client.connect(host, username=username, password=password)
    
    

    if sudo:
        _stdin, _stdout, _stderr = client.exec_command("sudo -S -p '' %s" % command)
        print("EXECUTANDO SUDO COMMAND")
        _stdin.write(password + "\n")
        _stdin.flush()
    else:
        _stdin, _stdout, _stderr = client.exec_command(command)
    
    print(_stdout.read().decode(), _stderr.read().decode())

    client.close()

def createServiceInfo(self):

    print("========================================= CLONING PROJECT =========================================")
    command = "git clone https://github.com/thiago-freire/DockerLab-SystemInfo.git;"
    self.__runCommand(command)


    print("========================================= INSTALLING PROJECT =========================================")
    command = "cd DockerLab-SystemInfo;/bin/python3 -m venv .env;source .env/bin/activate;" \
              "pip install -r requirements.txt"
    self.__runCommand(command)

    print("========================================= CREATE SERVICE =========================================")
    command = "cp DockerLab-SystemInfo/system-info.service /etc/systemd/system/"
    self.__runCommand(command, True)

    print("========================================= RELOAD DAEMON =========================================")
    command = "systemctl daemon-reload"
    self.__runCommand(command, True)

    print("========================================= ENABLE SERVICE =========================================")
    command = "systemctl enable system-info.service"
    self.__runCommand(command, True)

    print("========================================= START SERVICE =========================================")
    command = "systemctl start system-info.service"
    self.__runCommand(command, True)