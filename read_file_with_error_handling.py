from colorama import Fore

try:
    print(f"{Fore.MAGENTA}Reading file content:")
    with open("sample.txt", "r") as file:
        lines = file.readlines()
        for index, line in enumerate(lines, start=1):
            print(f"{Fore.CYAN}Line {index}: {Fore.GREEN}{line.strip()}")
except FileNotFoundError:
    print(f"{Fore.RED}Error: {Fore.RESET}The file '{Fore.CYAN}sample.txt{Fore.RESET}' was not found.")
