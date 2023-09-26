def _parse_macros (self):
    self.count = 0
    self.crc = 0
    self._iter_lines(self._parse_while)
    self._iter_lines(self._parse_macro)
    if self.crc > 0:
        self._flag = False
        self._line = 0
        self._errm = "{0} while loops not closed".format(self.crc)
    elif self.crc < 0:
        self._flag = False
        self._line = 0
        self._errm = "Trying to close a non existing while loop"


def _parse_macro (self, line, p, o):
    if line[0] != '$':
        return line
    else:
        macro = line[1:].split('(')[0]
        if macro == "MV":
            #$MV(A,B)
            args_split = str(line[4:].split(')')[0])
            args = args_split.split(',')
            if len(args) != 2:
                self._flag = False
                self._line = o
                self._errm = "Invalid move arguments"
                return line
            arg1 = args[0]
            arg2 = args[1]
            nl1 = "@" + arg1
            nl2 = "D=M"
            nl3 = "@" + arg2
            nl4 = "M=D"
            lst = [nl1, nl2, nl3, nl4]
            return lst
        elif macro  == "SWP":
            #$SWP(A,B)
            args_split = str(line[5:].split(')')[0])
            args = args_split.split(',')
            if len(args) != 2:
                self._flag = False
                self._line = o
                self._errm = "Invalid swap arguments"
                return line
            arg1 = args[0]
            arg2 = args[1]
            nl1 = "@" + arg1
            nl2 = "D=M"
            nl3 = "@temp"
            nl4 = "M=D"
            nl5 = "@" + arg2
            nl6 = "D=M"
            nl7 = "@" + arg1
            nl8 = "M=D"
            nl9 = "@temp"
            nl10 = "D=M"
            nl11 = "@" + arg2
            nl12 = "M=D"
            lst = [nl1, nl2, nl3, nl4, nl5, nl6, nl7, nl8, nl9, nl10, nl11, nl12]
            return lst
        elif macro == "SUM":
            #SUM(A,B,D)
            args_split = str(line[5:].split(')')[0])
            args = args_split.split(',')
            if len(args) != 3:
                self._flag = False
                self._line = o
                self._errm = "Invalid sum arguments"
                return line
            arg1 = args[0]
            arg2 = args[1]
            arg3 = args[2]
            nl1 = "@" + arg1
            nl2 = "D=M"
            nl3 = "@" + arg3
            nl4 = "M=D"
            nl5 = "@" + arg2
            nl6 = "D=M"
            nl7 = nl3
            nl8 = "M=M+D"
            lst = [nl1, nl2, nl3, nl4, nl5, nl6, nl7, nl8]
            return lst
        else:
            self._flag = False
            self._line = o
            self._errm = "Invalid macro"
            
            
def _parse_while(self, line, p, o):
    if line[0:6] != "$WHILE" and line != "$END":
        return line
    elif line[0:6] == "$WHILE":
        if self.crc > 0:
            hp = str(self.count) + str(self.crc)
        else:
            hp = str(self.count)
        arg = str(line[7:].split(')')[0])
        nl1 = "(WHILE_LOOP" + hp + ")"
        nl2 = "@" + arg
        nl3 = "D=M"
        nl4 = "@WHILE_END" + hp 
        nl5 = "D;JEQ"
        lst = [nl1, nl2, nl3, nl4, nl5]
        self.crc += 1
        return lst
    else:
        self.crc -= 1
        if self.crc > 0:
            hp = str(self.count) + str(self.crc)
        else:
            hp = str(self.count)
        nl1 = "@WHILE_LOOP" + hp
        nl2 = "0;JMP"
        nl3 = "(WHILE_END" + hp + ")"
        lst = [nl1, nl2, nl3]
        if self.crc == 0:
            self.count += 1
        return lst
        
            
            
            
            
    