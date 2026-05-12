import sys


def main():
    # TODO: Uncomment the code below to pass the first stage
    while True:
        sys.stdout.write("$ ")

        # Take in user input
        command = input("")
        arguements = command.split(" ")

        # Stop the REPL loop/Shell by entering "exit"
        if (command == "exit"):
            break
        
        # Implement the "echo" command
        elif (arguements[0] == "echo"):
            print(" ".join(arguements[1:]))

        else:
            print(f"{command}: command not found")


if __name__ == "__main__":
    main()
