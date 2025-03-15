from src.models.repositories.machine_repository import MachineRepository

from src.controllers.machine import (
    MachineInfoController,
    CreateMachineController
)

from src.services.machine import (
    MachineInfoService,
    CreateMachineService

)

def machine_info_compose():

    machine_repository = MachineRepository()
    machine_info_service = MachineInfoService(machine_repository)
    machine_info_controller = MachineInfoController(machine_info_service)

    return machine_info_controller

def create_machine_compose():

    machine_repository = MachineRepository()
    create_machine_service = CreateMachineService(machine_repository)
    create_machine_controller = CreateMachineController(create_machine_service)

    return create_machine_controller