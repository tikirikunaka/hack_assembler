import re
from symboltable import SymbolTable

class Parser:
    def __init__(self, file):
        self.file = file #str
        self.tokens = []
        self.current = 0
        self.output = []
        self.table = SymbolTable()

        self.a_command_pattern = '@\w*'
        self.c_command_pattern = '(\w*=)?([^;]*)(;\w*)?'
    
    def hasMoreCommands(self):
        if self.current < len(self.tokens):
            return True
        else:
            return False

    def advance(self):
        self.current += 1
    
    def commandType(self):
        first_char = self.tokens[self.current][0]
        if first_char == '@':
            return "A_COMMAND"
        elif first_char == '(':
            return "L_COMMAND"
        else:
            return "C_COMMAND"

    def dest(self):
        c_command = re.match(self.c_command_pattern, self.tokens[self.current])
        if not c_command.groups()[0]:
            return c_command.groups()[0]
        else:
            return c_command.groups()[0][:-1]

    def comp(self):
        c_command = re.match(self.c_command_pattern, self.tokens[self.current])
        return c_command.groups()[1]
    
    def jump(self):
        c_command = re.match('(\w=)?([^;]*)(;\w*)?', self.tokens[self.current])
        if not c_command.groups()[2]:
            return c_command.groups()[2]
        else:
            return c_command.groups()[2][1:]

    
    def parse(self):
        self.lexer()
        while self.hasMoreCommands():
            command_type = self.commandType()
            token = self.tokens[self.current]
            if command_type == 'C_COMMAND':
                dest_mnemonic = self.dest()
                comp_mnemonic = self.comp()
                jump_mnemonic = self.jump()
                token = [dest_mnemonic, comp_mnemonic, jump_mnemonic]
            self.output.append((command_type, token))
            self.advance()
        self.create_symboltable()

        return self.output, self.table

    def create_symboltable(self):
        rom = 0
        for element in self.output:
            if element[0] == 'A_COMMAND' or element[0] == 'C_COMMAND':
                rom += 1
            else:
                self.table.addEntry(element[1][1:-1], rom)



    def lexer(self):
        i = 0
        code = self.file.split()
        for element in code:
            a_command = re.match(self.a_command_pattern, element)
            if a_command:
                self.tokens.append(a_command.group())
                i += 1
                continue
            
            comment = re.match('//.*', element)
            if comment:
                i += 1
                continue
            
            space = re.match(' ', element)
            if space:
                i += 1
                continue
            
            c_command = re.match(self.c_command_pattern, element)
            if c_command:
                i += 1
                self.tokens.append(c_command.group())
                continue

