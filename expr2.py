# Matthew Penner
# 

# CS358 Fall'24 Assignment 2 (Part A)
#
# Expr2 - an expression language with arithmetic, logical, and 
#        relational operations
# The chain works!

from lark import Lark, v_args
from lark.visitors import Interpreter

# Grammar
#
grammar = """
  ?start: logic
  ?logic: logic "and" relation -> and
       | logic "or" relation   -> or
       | "not" relation   -> not
       | relation
  ?relation: relation "==" expr -> eq
           | relation "!=" expr -> neq
           | relation "<" expr -> lt
           | relation ">" expr -> gt
           | relation "<=" expr -> leq
           | relation ">=" expr -> geq
           | expr
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
    def eq(self, x, y): return Eval().visit(x) == Eval().visit(y)
    def neq(self, x, y): return Eval().visit(x) != Eval().visit(y)
    def lt(self, x, y): return Eval().visit(x) < Eval().visit(y)
    def gt(self, x, y): return Eval().visit(x) > Eval().visit(y)
    def leq(self, x, y): return Eval().visit(x) <= Eval().visit(y)
    def gec(self, x, y): return Eval().visit(x) >= Eval().visit(y)
    def and_(self, x, y): return Eval().visit(x) and Eval().visit(y)
    def or_(self, x, y): return Eval().visit(x) or Eval().visit(y)
    def not_(self, x): return not Eval().visit(x)

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
