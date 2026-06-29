

def command_line_parser(command_line):
    command_line_stripped = command_line.strip()

    tokens = [] # Store the values after parsing the list
    single_quote_flag = False # Flag to help find SINGLE quotes
    double_quote_flag = False # Flag to help find DOUBLE quotes

    tempToken = ""
    idx = 0
    while idx < len(command_line_stripped) + 1:
        # If it reaches the last idx in command line append the remaining/leftover word
        if (idx == len(command_line_stripped)):
            if (tempToken != ""):
                tokens.append(tempToken)
            
            break

        char = command_line_stripped[idx]

        # First check if value is an already opened "double quote"
        if (char == "\\" and idx < len(command_line_stripped)):
            tempToken += command_line_stripped[idx + 1]
            idx += 1

        elif (double_quote_flag == True):
            if (char == "\""):
                double_quote_flag = False
            else:
                tempToken += char
        
        # If value is not in an "opened double quote" the check if its a "single quote"
        elif (single_quote_flag == True):
            if (char == "'"):
                single_quote_flag = False
            else:
                tempToken += char
        

        else:
            # Check first if the current index is a "double quote"
            if (char == "\""):
                double_quote_flag = True
            
            # Then check if the current index is a "single quote" but is not within an already
            # defined/found double quote
            elif (char == "'" and double_quote_flag == False):
                single_quote_flag = True
            
            # If there is an empty space ignore it and continue
            elif (char == " " and tempToken == ""):
                idx += 1
                continue
            
            elif (char == " " and tempToken != ""):
                tokens.append(tempToken)
                tempToken = ""
            
            else:
                tempToken += char
        
        idx += 1

    return tokens