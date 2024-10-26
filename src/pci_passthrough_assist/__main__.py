from sys import platform
from pci_passthrough_assist.permissions import is_ran_by_root

if platform != "linux":
    print("This tool will only work on Linux based OS.")
    exit(1)

if not is_ran_by_root():
    print("This script needs to run as root.")
    exit(1)