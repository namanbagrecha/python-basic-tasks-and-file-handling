from colorama import Fore

text = input(f"Enter {Fore.CYAN}text{Fore.RESET} to write to the file: ")
with open("output.txt", "w") as file:
    file.write(text + "\n")
print(f"{Fore.GREEN}Data successfully written {Fore.RESET}to output.txt.")

append_text = input(f"\nEnter additional {Fore.CYAN}text{Fore.RESET} to append: ")
with open("output.txt", "a") as file:
    file.write(append_text + "\n")
print(f"{Fore.GREEN}Data successfully appended.{Fore.RESET}")

print(f"\nFinal content {Fore.CYAN}of output.txt{Fore.RESET}:")
with open("output.txt", "r") as file:
    print(file.read())
