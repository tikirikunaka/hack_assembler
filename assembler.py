from parser import Parser
from code import Code

with open('./add/Add.asm', 'r') as f:
    parser = Parser(f.read())
    tree = parser.parse()
    code_generater = Code(tree)
    code_generater.code_generate()