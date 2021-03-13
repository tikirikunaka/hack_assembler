from parser import Parser
from code import Code

with open('./add/Add.asm', 'r') as f:
    parser = Parser(f.read())
    tree, table = parser.parse()
    code_generater = Code(tree, table)
    code_generater.code_generate()