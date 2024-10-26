from pci_passthrough_assist.pci import driver_of_pci_device


class PciDevice:

    def __init__(self, device_id: str):
        self.device_id = device_id

    def driver_name(self) -> str:
        return driver_of_pci_device(self.device_id)
