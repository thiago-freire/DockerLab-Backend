from collections import namedtuple
from src.models.repositories.interfaces import MachineRepositoryInterface
from src.infra.configs.db_config_handler import DbConfigHandler
from src.models.entities.machine import Machine
# from sqlalchemy import update

import paramiko
import paramiko.client

class MachineRepository(MachineRepositoryInterface):
    
    def create_machine(self, ip, name, user , password, port):

        self.host = ip
        self.user = user
        self.password = password

        with DbConfigHandler() as connection:
            try:
                new_machine = Machine(ip=ip, name=name, user=user, password=password, port=port)
                connection.session.add(new_machine)
                connection.session.commit()

                self.__createServiceInfo()

                return new_machine.to_dict()
            except: 
                connection.session.rollback()
                raise
            finally:
                connection.session.close()

    def get_all(self):

        with DbConfigHandler() as connection:
            try:
                machines = connection.session.query(Machine).all()

                machine_dicts = [machine.to_dict() for machine in machines]
                
                return machine_dicts
            except: 
                connection.session.rollback()
                raise
            finally:
                connection.session.close()

    def get_machine_by_name(self, name: str):

        with DbConfigHandler() as connection:
            try:
                machine = connection.session.query(Machine).filter_by(name=name).first()

                return machine
            except: 
                connection.session.rollback()
                raise
            finally:
                connection.session.close()

    def get_machine_by_id(self, id):
        with DbConfigHandler() as connection:
            try:
                machine = connection.session.query(Machine).filter_by(id=id).first()

                return machine
            except: 
                connection.session.rollback()
                raise
            finally:
                connection.session.close()

    def get_machine_by_ip(self, ip: str):

        with DbConfigHandler() as connection:
            try:
                machine = connection.session.query(Machine).filter_by(ip=ip).first()

                return machine
            except: 
                connection.session.rollback()
                raise
            finally:
                connection.session.close()

    def delete_machine(self, machine: Machine) -> bool:
        with DbConfigHandler() as connection:
            try:
                connection.session.delete(machine)
                connection.session.commit()

                return True
            except:
                connection.session.rollback()
                raise
            finally:
                connection.session.close()

    def update_machine(self, machine: Machine) -> bool:

        if not machine:
            return False

        with DbConfigHandler() as connection:
            try:
                mach = connection.session.query(Machine).filter_by(id=machine.id).first()

                mach.ip = machine.ip
                mach.name = machine.name
                mach.user = machine.user
                mach.password = machine.password
                mach.port = machine.port

                return True

            except:
                connection.session.rollback()
                return False

            finally:
                connection.session.close()
    
    def getMachineInfo(self, ip: str, get, loads):

        x = get(f'http://{ip}:5001/')

        return loads(x.text)
        
        
    def __runCommand(self, command: str, sudo: bool = False):

        client = paramiko.client.SSHClient()

        client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        client.connect(self.host, username=self.user, password=self.password)
        
        if sudo:
            _stdin, _stdout, _stderr = client.exec_command("sudo -S -p '' %s" % command)
            print("EXECUTANDO SUDO COMMAND")
            _stdin.write(self.password + "\n")
            _stdin.flush()
        else:
            _stdin, _stdout, _stderr = client.exec_command(command)
        
        print(_stdout.read().decode(), _stderr.read().decode())

        client.close()

    def __createServiceInfo(self):

        print("========================================= CLONING PROJECT =========================================")
        command = "git clone https://github.com/thiago-freire/DockerLab-SystemInfo.git;"
        self.__runCommand(command)

        print("========================================= INSTALLING PYTHON ENV =========================================")
        command = "apt update"
        self.__runCommand(command, True)

        command = "apt install python3.8-venv -y"
        self.__runCommand(command, True)

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