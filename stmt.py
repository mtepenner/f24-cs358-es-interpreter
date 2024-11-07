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

  ?prog: stmt
  ?stmt: ID "=" relation                            -> assign
    | "if" "(" relation ")" stmt ["else" stmt]      -> if_stmt
    | "while" "(" relation ")" stmt                 -> while_stmt
    | "print" "(" relation ")"                      -> print_stmt
    | "{" stmt (";" stmt)* "}"                  -> block
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
    | ID                                        -> var
    | NUM                                       -> num

  %import common.WORD                           -> ID
  %import common.INT                            -> NUM
  %import common.WS
  %ignore WS
"""

parser = Lark(grammar)

# Interpreter
#
@v_args(inline=True)
class Eval(Interpreter):
    def __init__(self): self.env = {}
    def num(self, val):  return int(val)
    def var(self, name): return self.env.get(name, 0)
    def assign(self, name, value):
        self.env[name] = self.visit(value)
        return self.env[name]
    def add(self, x, y): return Eval().visit(x) + Eval().visit(y)
    def sub(self, x, y): return Eval().visit(x) - Eval().visit(y)
    def mul(self, x, y): return Eval().visit(x) * Eval().visit(y)
    def lt(self, x, y): return Eval().visit(x) < Eval().visit(y)
    def gt(self, x, y): return Eval().visit(x) > Eval().visit(y)
    def leq(self, x, y): return Eval().visit(x) <= Eval().visit(y)
    def gec(self, x, y): return Eval().visit(x) >= Eval().visit(y)
    def eq(self, x, y): return Eval().visit(x) == Eval().visit(y)
    def neq(self, x, y): return Eval().visit(x) != Eval().visit(y)
    def if_stmt(self, condition, then_branch, else_branch=None):
        if self.visit(condition):
            return self.visit(then_branch)
        elif else_branch is not None:
            return self.visit(else_branch)
    def while_stmt(self, condition, body):
        while self.visit(condition):
            return self.visit(body)
    def print_stmt(self, value):
        result = self.visit(value)
        print(result)
        return result
    def block(self, *statements):
        for stmt in statements:
            self.visit(stmt)



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

