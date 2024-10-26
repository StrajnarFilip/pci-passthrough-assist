from pci_passthrough_assist.pci import driver_of_pci_device
from os.path import exists
from os import listdir


class PciDevice:

    def __init__(self, device_id: str):
        self.device_id = device_id

    def driver_name(self) -> str:
        return driver_of_pci_device(self.device_id)

    def is_vga(self) -> bool:
        return exists(f"/sys/bus/pci/devices/{self.device_id}/boot_vga")

    def devices_in_iommu_group(self) -> list['PciDevice']:
        device_ids: list[str] = listdir(
            f"/sys/bus/pci/devices/{self.device_id}/iommu_group/devices")
        return [PciDevice(device_id) for device_id in device_ids]

    def __str__(self) -> str:
        return f"{self.device_id} driver: {self.driver_name()} VGA: {self.is_vga()}"
