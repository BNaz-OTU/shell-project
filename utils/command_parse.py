

def command_line_parser(command_line):
    command_line_stripped = command_line.strip()

    tokens = [] # Store the values after parsing the list
    single_quote_flag = False # Flag to help find single quotes

    tempToken = ""
    for idx in range(len(command_line_stripped) + 1):
        # If it reaches the last idx in command line append the remaining/leftover word
        if (idx == len(command_line_stripped)):
            if (tempToken != ""):
                tokens.append(tempToken)
            
            break

        char = command_line_stripped[idx]

        if (single_quote_flag == True):
            if (char == "'" or char == "\""):
                single_quote_flag = False
            else:
                tempToken += char
        
        else:
            if (char == "'" or char == "\""):
                single_quote_flag = True
            
            elif (char == " " and tempToken == ""):
                continue

            elif (char == " " and tempToken != ""):
                tokens.append(tempToken)
                tempToken = ""
            
            else:
                tempToken += char

    return tokens