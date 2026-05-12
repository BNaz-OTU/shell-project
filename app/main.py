import sys

BUILTINS = {"echo", "type", "exit"}

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
        
        # Implemnt the "type" command, will help check to see what type something is
        elif (arguements[0] == "type"):
            if (arguements[1] in BUILTINS):
                print(f"{arguements[1]} is a shell builtin")
            
            else:
                print(f"{arguements[1]}: not found")

        else:
            print(f"{command}: command not found")


if __name__ == "__main__":
    main()
