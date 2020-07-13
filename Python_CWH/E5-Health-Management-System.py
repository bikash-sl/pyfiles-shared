"""
Health Management System
3 clients - Pravin, Bikash and Subham
Total 6 files
write a function that when executed takes as input client name
One more function to retrieve exercise or food for any client
"""

print("\t\t\tHealth Management System\n")
client_list = {1: "Pravin", 2: "Bikash", 3: "Subham"}
log_files = {1: "Exercise", 2: "Diet"}


def getdate():
    import datetime
    return datetime.datetime.now().strftime("%d-%b-%Y \t %I:%M %p")


def log_procedure():
    client = ""
    try:
        for key, value in client_list.items():
            print(key, ": ", value)
        client = int(input("Enter your Client's Sl. No.: "))
        operation = int(input("Press [1] log an entry or [2] retrieve entries: "))
        if operation == 1:  # Log operation
            log = "y"
            while log == "y":
                file_name = int(input("Press [1] for Exercise or [2] Diet: "))
                with open(client_list[client] + "_"
                          + log_files[file_name] + ".txt", "a") as file:
                    text = input("Enter " + log_files[file_name] + " details: ")
                    file.write(str(getdate()) + "\t:\t " + text + "\n")
                print("Added Successfully.")
                log = input("Do want to add more? [Y/N]: ").lower()
        elif operation == 2:  # Retrieve operation
            file_name = int(input("Press [1] for Exercise or [2] for Diet: "))
            with open(client_list[client] + "_" + log_files[file_name] + ".txt") as file:
                contents = file.read()
                print("\n\t\t>> " + log_files[file_name] +
                      " log of " + client_list[client] + " <<\n")
                print(contents)
    except FileNotFoundError:
        print("No such file or directory found for " + client_list[client] + ".")
    except (ValueError, TypeError, KeyError):
        print(" !!! Wrong input !!!")


logger = "y"
while logger == "y":
    log_procedure()
    logger = input("\nDo you want to log or retrieve more files [Y/N]: ").lower()
    if logger == "n":
        exit()
else:
    print(" !!! Wrong input !!!")
