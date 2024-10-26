from os import listdir
from os.path import realpath, basename


def all_pci_device_ids() -> list[str]:
    return listdir("/sys/bus/pci/devices")


def all_pci_driver_ids() -> list[str]:
    return listdir("/sys/bus/pci/drivers")


def driver_of_pci_device(pci_device_id: str) -> str:
    driver_directory: str = realpath(
        f"/sys/bus/pci/devices/{pci_device_id}/driver")
    return basename(driver_directory)
