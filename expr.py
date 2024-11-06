# Matthew Penner
#

# CS358 Fall'24 Assignment 2 (Part A)
#
# Expr - an expression language with arithmetic, logical, and 
#        relational operations
#

from lark import Lark, v_args
from lark.visitors import Interpreter

# Grammar
#
grammar = """
  ?start: ...

  # ... need sections for logical and relational ops

  # the arith ops section, need some adjustments

  ?expr: expr "+" term  -> add
       | expr "-" term  -> sub
       | term         

  ?term: term "*" atom  -> mul
       | term "/" atom  -> div
       | atom

  ?atom: "(" expr ")"
       | NUM            -> num

  %import common.INT    -> NUM
  %ignore " "
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
        prog = input("Enter an expr: ")
        tree = parser.parse(prog)
        print(prog)
        print(tree.pretty(), end="")
        print(Eval().visit(tree))
    except Exception as e:
        print(e)

if __name__ == "__main__":
    main()
