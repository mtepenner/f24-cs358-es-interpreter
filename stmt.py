# Matthew Penner
#

# CS358 Fall'24 Assignment 2 (Part B)
#
# Stmt - a language with simple statements
#
#   prog -> stmt
#
#   stmt -> ID "=" expr 
#         | "if" "(" expr ")" stmt ["else" stmt]
#         | "while" "(" expr ")" stmt
#         | "print" "(" expr ")"
#         | "{" stmt (";" stmt)* "}" 
#
#   expr -> expr "+" term
#         | expr "-" term
#         | term         
#
#   term -> term "*" atom
#         | term "/" atom
#         | atom
#
#   atom: "(" expr ")"
#         | ID
#         | NUM
#
from lark import Lark, v_args
from lark.visitors import Interpreter

# Grammar
#
grammar = """
  ?start: stmt

  ... need code

  %import common.WORD   -> ID
  %import common.INT    -> NUM
  %import common.WS
  %ignore WS
"""

parser = Lark(grammar)

# Interpreter
#
@v_args(inline=True)
class Eval(Interpreter):
    def num(self, val):  return int(val)
    def add(self, x, y): return Eval().visit(x) + Eval().visit(y)
    def sub(self, x, y): return Eval().visit(x) - Eval().visit(y)
    def mul(self, x, y): return Eval().visit(x) * Eval().visit(y)
    def div(self, x, y): return Eval().visit(x) // Eval().visit(y)

    # ... need code

def main():
    try:
        prog = input("Enter a program: ")
        tree = parser.parse(prog)
        print(prog)
        print(tree.pretty(), end="")
        print(Eval().visit(tree))
    except Exception as e:
        print(e)

if __name__ == "__main__":
    main()

