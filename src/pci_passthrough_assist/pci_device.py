from pci_passthrough_assist.pci import driver_of_pci_device
from os.path import exists
from os import listdir


class PciDevice:

    def __init__(self, device_id: str):
        assert exists(f"/sys/bus/pci/devices/{self.device_id}")
        self.device_id = device_id

    def driver_name(self) -> str:
        return driver_of_pci_device(self.device_id)

    def is_vga(self) -> bool:
        return exists(f"/sys/bus/pci/devices/{self.device_id}/boot_vga")

    def vendor_code(self, remove_prefix: bool = True) -> str:
        with open(f"/sys/bus/pci/devices/{self.device_id}/vendor") as vendor:
            return vendor.read() if not remove_prefix else vendor.read(
            ).lstrip("0x")

    def device_code(self, remove_prefix: bool = True) -> str:
        with open(f"/sys/bus/pci/devices/{self.device_id}/vendor") as device:
            return device.read() if not remove_prefix else device.read(
            ).lstrip("0x")

    def unbind_driver(self):
        driver_unbind_path = f"/sys/bus/pci/devices/{self.device_id}/driver/unbind"
        if not exists(driver_unbind_path):
            print("Device is not bound to any driver.")
            return

        with open(driver_unbind_path, "w") as device_driver:
            device_driver.write(self.device_id)

    def set_driver_override(self, reserved_for_driver: str):
        with open(f"/sys/bus/pci/devices/{self.device_id}/driver_override",
                  "w") as driver_override:
            driver_override.write(reserved_for_driver)

    def bind_to_driver(self, driver_to_bind: str, unbind_first: bool = True):
        if unbind_first:
            self.unbind_driver()

        driver_bind_path = f"/sys/bus/pci/drivers/{driver_to_bind}/bind"
        if not exists(driver_bind_path):
            print(f"Can't bind to driver: {driver_bind_path}.")
            return

        with open(driver_bind_path, "w") as driver:
            driver.write(self.device_id)

    def devices_in_iommu_group(self) -> list['PciDevice']:
        device_ids: list[str] = listdir(
            f"/sys/bus/pci/devices/{self.device_id}/iommu_group/devices")
        return [PciDevice(device_id) for device_id in device_ids]

    def __str__(self) -> str:
        return f"{self.device_id} driver: {self.driver_name()} VGA: {self.is_vga()}"
