from pci_passthrough_assist.process_runner import sh


def is_ran_by_root() -> bool:
    return sh(["whoami"]) == "root"
