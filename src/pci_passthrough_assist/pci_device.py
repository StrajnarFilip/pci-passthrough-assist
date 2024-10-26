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

    def unbind_driver(self):
        with open(f"/sys/bus/pci/devices/{self.device_id}/driver/unbind",
                  "w") as device_driver:
            device_driver.write(self.device_id)

    def bind_to_driver(self, driver_to_bind: str, unbind_first: bool = True):
        if unbind_first:
            self.unbind_driver()

        with open(f"/sys/bus/pci/drivers/{driver_to_bind}/bind",
                  "w") as driver:
            driver.write(self.device_id)

    def devices_in_iommu_group(self) -> list['PciDevice']:
        device_ids: list[str] = listdir(
            f"/sys/bus/pci/devices/{self.device_id}/iommu_group/devices")
        return [PciDevice(device_id) for device_id in device_ids]

    def __str__(self) -> str:
        return f"{self.device_id} driver: {self.driver_name()} VGA: {self.is_vga()}"
