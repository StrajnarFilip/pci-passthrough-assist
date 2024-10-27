from os import listdir


def all_pci_device_ids() -> list[str]:
    return listdir("/sys/bus/pci/devices")


def all_pci_driver_ids() -> list[str]:
    return listdir("/sys/bus/pci/drivers")
