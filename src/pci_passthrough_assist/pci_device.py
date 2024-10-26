from pci_passthrough_assist.pci import driver_of_pci_device
from os.path import exists


class PciDevice:

    def __init__(self, device_id: str):
        self.device_id = device_id

    def driver_name(self) -> str:
        return driver_of_pci_device(self.device_id)

    def is_vga(self) -> bool:
        return exists(f"/sys/bus/pci/devices/{self.device_id}/boot_vga")

    def __str__(self) -> str:
        return f"{self.device_id} driver: {self.driver_name()} VGA: {self.is_vga()}"