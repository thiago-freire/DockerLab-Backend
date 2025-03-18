from collections import namedtuple
from src.models.repositories.interfaces import MachineRepositoryInterface
from src.infra.configs.db_config_handler import DbConfigHandler
from src.models.entities.machine import Machine
from sqlalchemy import update

class MachineRepository(MachineRepositoryInterface):
    
    def create_machine(self, ip, name, user , password, port):
        with DbConfigHandler() as connection:
            try:
                new_machine = Machine(ip=ip, name=name, user=user, password=password, port=port)
                connection.session.add(new_machine)
                connection.session.commit()

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
    
    def getMachineInfo(self, machine: Machine, get: function, loads: function):

        x = get(f'http://{machine.ip}:5001/')

        return loads(x.text)