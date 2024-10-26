from sys import platform

if platform != "linux":
    print("This tool will only work on Linux based OS.")
    exit(1)