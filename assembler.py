import re

class Parser:
    def __init__(self, file):
        self.file = file #str
        self.tokens = []
        self.current = 0
        self.output = []

        self.a_command_pattern = '@\w*'
        self.c_command_pattern = '(\w=)?([^;]*)(;\w*)?'
    
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
        
        return self.output

    def lexer(self):
        i = 0
        code_without_newline = re.split("\n+", self.file)
        code = list(filter(lambda e : e != '', code_without_newline))

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
            
            c_command = re.match('(\w=)?([^;]*)(;\w*)?', element)
            if c_command:
                i += 1
                self.tokens.append(c_command.group())
                continue


class Code:
    def __init__(self, tree):
        self.tree = tree
        print(self.tree)
        open('filename.hack', 'w')
    
    def code_generate(self):
        for element in self.tree:
            if element[0] == "A_COMMAND":
                self.a_command(element[1])
            elif element[0] == "C_COMMAND":
                self.c_command(element[1])

    def c_command(self, commands):
        dest_command = commands[0]
        comp_command = commands[1]
        jump_command = commands[2]
        dest_ = self.dest(dest_command)
        comp_ = self.comp(comp_command)
        #jump_ = self.jump(jump_command)

    def dest(self, dest_command):
        if dest_command == None:
            return '000'
        elif dest_command == 'M':
            return '001'
        elif dest_command == 'D':
            return '010'
        elif dest_command == 'MD':
            return '011'
        elif dest_command == 'A':
            return '100'
        elif dest_command == 'AM':
            return '101'
        elif dest_command == 'AD':
            return '110'
        elif dest_command == 'AMD':
            return '111'
    
    def comp(self, comp_command):
        if comp_command == '0':
            return '0001010'
        elif comp_command == '1':
            return '0111111'
        elif comp_command == '-1':
            return '0111010'
        elif comp_command == 'D':
            return '0001100'
        elif comp_command == 'A':
            return '0110000'
        elif comp_command == 'M':
            return '1110000'
        elif comp_command == '!D':
            return '0001101'
        elif comp_command == '!A':
            return '0110001'
        elif comp_command == '!M':
            return '1110001'
        elif comp_command == '-D':
            return 'ki'

    def a_command(self, command):
        with open('filename.hack', 'a') as f:
            f.write('0')
            a = bin(int(command[1:]))[2:]
            f.write(a.zfill(15))
            f.write('\n')

with open('./add/Add.asm', 'r') as f:
    parser = Parser(f.read())
    tree = parser.parse()
    code_generater = Code(tree)
    code_generater.code_generate()