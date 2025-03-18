import paramiko
import paramiko.client

def runCommand(command: str):

    host = "192.168.200.116"
    username = "viplab"
    password = "viplab321"

    client = paramiko.client.SSHClient()

    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    client.connect(host, username=username, password=password)
    
    _stdin, _stdout, _stderr = client.exec_command(command)
    
    print(_stdout.read().decode(), _stderr.read().decode())

    client.close()



if __name__ == "__main__":

    command =   "git clone https://github.com/thiago-freire/DockerLab-SystemInfo.git;" \
                "cd DockerLab-SystemInfo;/bin/python3 -m venv .env;source .env/bin/activate;" \
                "pip install -r requirements.txt;.env/bin/python run.py"
    runCommand(command)

    # runCommand("git clone https://github.com/thiago-freire/DockerLab-SystemInfo.git")