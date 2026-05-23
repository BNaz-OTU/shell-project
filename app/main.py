import sys, os, subprocess

BUILTINS = {"echo", "type", "exit", "pwd", "cd"}

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
        
        # Implement the "pwd" command
        elif (command == "pwd"):
            print(os.getcwd())
        
        elif (command == "cd"):
            if (os.path.isdir(arguements[1])):
                os.chdir(arguements[1])
            else:
                print(f"cd: {arguements[1]}: No such file or directory")
        
        # Implement the "type" command, will help check to see what type something is
        elif (command == "type"):
            
            # CASE 1: BUILTIN
            if (arguements[1] in BUILTINS):
                print(f"{arguements[1]} is a shell builtin")
            
            # CASE 2: CHECK PATH
            else:
                path_var = os.environ.get("PATH")
                directory_paths = path_var.split(":")
                found_file_path_flag = False

                for dir in directory_paths:
                    file_path = os.path.join(dir, arguements[1])

                    if (os.access(file_path, os.X_OK)):
                        print(f"{arguements[1]} is {file_path}")
                        found_file_path_flag = True
                        break

                # CASE 3: NOT FOUND
                if (found_file_path_flag == False):
                    print(f"{arguements[1]}: not found")
        
        # Unknown command
        else:
            path_var = os.environ.get("PATH")
            directory_paths = path_var.split(":")
            command_not_found_flag = False

            for path in directory_paths:
                cmd_path = path + "/" + command

                if (os.access(cmd_path, os.X_OK)):
                    subprocess.run(arguements)
                    command_not_found_flag = True

            if (command_not_found_flag == False):
                print(f"{command}: command not found")

if __name__ == "__main__":
    main()
