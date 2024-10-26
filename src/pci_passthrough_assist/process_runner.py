from subprocess import run


def sh_binary(args: list[str], ) -> bytes:
    return run(args, capture_output=True).stdout


def sh(args: list[str], rstrip_newline=True):
    string_output: str = sh_binary(args).decode()
    return string_output if not rstrip_newline else string_output.rstrip("\n")


def sh_lines(args: list[str]) -> list[str]:
    return sh(args, rstrip_newline=True).splitlines()
