import sys, os

BUILTINS = {"echo", "type", "exit"}

def main():
    # TODO: Uncomment the code below to pass the first stage
    while True:
        sys.stdout.write("$ ")

        # Take in user input
        command_line = input("")
        arguements = command_line.split(" ")

        command = arguements[0] # Have the command/first value put in the prompt

        # Stop the REPL loop/Shell by entering "exit"
        if (command == "exit"):
            break
        
        # Implement the "echo" command
        elif (command == "echo"):
            print(" ".join(arguements[1:]))
        
        # Implemnt the "type" command, will help check to see what type something is
        elif (command == "type"):
            
            path_var = os.environ.get("PATH")
            directory_paths = path_var.split(":")
            # print(directory_paths)

            for dir in directory_paths:
                print(dir)
                
            for dir in directory_paths:
                if (os.access(dir, os.X_OK)):
                    print(f"{command} is {dir}")
                    break
            
            # CASE 1: BUILTIN
            if (arguements[1] in BUILTINS):
                print(f"{arguements[1]} is a shell builtin")


            # CASE 3: NOT FOUND
            else:
                print(f"{arguements[1]}: not found")

        else:
            print(f"{command}: command not found")


if __name__ == "__main__":
    main()
