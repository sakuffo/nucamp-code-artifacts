def banner():
    print("          === Automated Teller Machine ===          ")


def atm_menu(name):
    print("")
    banner()
    print("User: " + name)
    print("------------------------------------------")
    print("| 1.    Balance     | 2.    Deposit      |")
    print("------------------------------------------")
    print("------------------------------------------")
    print("| 3.    Withdraw    | 4.    Logout       |")
    print("------------------------------------------")


banner()
name = input("Enter name to register: ")
pin = input("Enter PIN: ")
balance = 0
print(f"{name} has been registered with with a starting balance of {balance}")

while True:
    banner()
    print("LOGIN")
    login_name = input("Enter name: ")
    login_pin = input("Enter PIN: ")
    if login_name == name and login_pin == pin:
        print("Login successful!\n")
        break
    else:
        print("Invalid Credentials!\n")
        continue

while True:
    atm_menu(name)
    option = input("Choose an option: ")
