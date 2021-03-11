from parser import Parser


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