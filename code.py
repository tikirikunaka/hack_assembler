
class Code:
    def __init__(self, tree):
        self.tree = tree
        open('filename.hack', 'w')
    
    def code_generate(self):
        for element in self.tree:
            if element[0] == "A_COMMAND":
                self.a_command(element[1])
            elif element[0] == "C_COMMAND":
                self.c_command(element[1])
            else:
                print("L-command not implementation")

    def c_command(self, commands):
        dest_command = commands[0]
        comp_command = commands[1]
        jump_command = commands[2]
        dest_ = self.dest(dest_command)
        comp_ = self.comp(comp_command)
        jump_ = self.jump(jump_command)

        with open('filename.hack', 'a') as f:
            f.write('111')
            print(dest_, comp_, jump_)
            f.write(comp_+dest_+jump_+'\n')

    def jump(self, jump_command):
        if jump_command == None:
            return '000'
        elif jump_command == 'JGT':
            return '001'
        elif jump_command == 'JEQ':
            return '010'
        elif jump_command == 'JGE':
            return '011'
        elif jump_command == 'JLT':
            return '100'
        elif jump_command == 'JNE':
            return '101'
        elif jump_command == 'JLE':
            return '110'
        elif jump_command == 'JMP':
            return '111'
        else:
            print("jump error")


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
        else:
            print("dest error")
    
    def comp(self, comp_command):
        if comp_command == '0':
            return '0101010'
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
            return '0001111'
        elif comp_command == '-A':
            return '0110011'
        elif comp_command == '-M':
            return '1110011'
        elif comp_command == 'D+1':
            return '0011111'
        elif comp_command == 'A+1':
            return '0110111'
        elif comp_command == 'M+1':
            return '1110111'
        elif comp_command == 'D-1':
            return '0001110'
        elif comp_command == 'A-1':
            return '0110010'
        elif comp_command == 'M-1':
            return '1110010'
        elif comp_command == 'D+A':
            return '0000010'
        elif comp_command == 'D+M':
            return '1000010'
        elif comp_command == 'D-A':
            return '0010011'
        elif comp_command == 'D-M':
            return '1010011'
        elif comp_command == 'A-D':
            return '0000111'
        elif comp_command == 'M-D':
            return '1000111'
        elif comp_command == 'D&A':
            return '0000000'
        elif comp_command == 'D&M':
            return '1000000'
        elif comp_command == 'D|A':
            return '0010101'
        elif comp_command == 'D|M':
            return '1010101'
        else:
            print("comp error : ", comp_command)

    def a_command(self, command):
        with open('filename.hack', 'a') as f:
            f.write('0')
            a = bin(int(command[1:]))[2:]
            f.write(a.zfill(15))
            f.write('\n')
