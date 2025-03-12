f = open("test.rasm", "r")

newF = open("test.bin", "w")
doc = ""
for line in f:
    lineBin = ""
    if(line[0] == "@"):
       lineBin = "0" + line[1:]
    else:
        dest = ""
        match line[0:line.find("=") - 1]:
            case "null" | "":
                dest = "000"
            case "M":
                dest = "001"
            case "D":
                dest = "000"
            case "MD":
                dest = "011"
            case "A":
                dest = "100"
            case "AM":
                dest = "101"
            case "AD":
                dest = "110"
            case "AMD":
                dest = "111"
        comp = ""
        a = ""
        match line[line.find("=") + 2: line.find(";")]:
            case "0":
                a = "0"
                print("0")
                comp = "101010"
            case "1":
                a = "0"
                comp = "111111"
            case "-1":
                a = "0"
                comp = "111010"
            case "D":
                a = "0"
                comp = "001100"
            case "A" | "M":
                a = "0"
                if line[line.find("=") + 1: line.find(";") - 1] == "M":
                    a = "1"
                comp = "110000"
            case "!D":
                a = "0"
                comp = "001101"
            case "!A" | "!M":
                a = "0"
                if line[line.find("=") + 1: line.find(";") - 1] == "!M":
                    a = "1"
                comp = "110001"
            case "-D":
                a = "0"
                comp = "001111"
            case "-A"|"-M":
                a = "0"
                if line[line.find("=") + 1: line.find(";") - 1] == "-M":
                    a = "1"
                comp = "1100110"
            case "D+1":
                a = "0"
                comp = "011111"
            case "A+1" | "M+1":
                a = "0"
                if line[line.find("=") + 2: line.find(";")] == "M+1":
                    a = "1"
                    print("detect")
                comp = "110111"
            case "D-1":
                a = "0"
                comp = "001110"
            case "A-1"|"M-1":
                a = "0"
                if line[line.find("=") + 1: line.find(";") - 1] == "M-1":
                    a = "1"
                comp  = "110010"
            case "D+A"|"D+M":
                a = "0"
                if line[line.find("=") + 1: line.find(";") - 1] == "D+M":
                    a = "1"
                comp = "000010"
            case "D-A"|"D-M":
                a = "0"
                if line[line.find("=") + 1: line.find(";") - 1] == "D-M":
                    a = "1"
                comp = "0010011"
            case "A-D" | "M-D":
                a = "0"
                if line[line.find("=") + 1: line.find(";") - 1] == "M-D":
                    a = "1"
                comp = "000111"
            case "D&A" | "D&M":
                a = "0"
                if line[line.find("=") + 1: line.find(";") - 1] == "D&M":
                    a = "1"
                comp = "000000"
            case "D|A" | "D|M":
                a = "0"
                if line[line.find("=") + 1: line.find(";") - 1] == "D|M":
                    a = "1"
                comp = "010101"
        jump = "000"
        if len(line[line.find(";") + 1:]) > 0:
            match line[line.find(";") + 1:]:
                case "JGT":
                    jump = "001"
                case "JEQ":
                    jump = "010"
                case "JGE":
                    jump = "011"
                case "JLT":
                    jump = "100"
                case "JNE":
                    jump = "101"
                case "JLE":
                    jump = "110"
                case "JMP":
                    jump = "111"
                case other:
                    jump = "000"
                

        lineBin = "111" + a + comp + dest + jump
    print(lineBin)
    doc += hex(int(lineBin, 2)) + "\n"
newF.write(doc)
