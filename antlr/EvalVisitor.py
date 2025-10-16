from ArithmeticVisitor import ArithmeticVisitor
from ArithmeticParser import ArithmeticParser

class EvalVisitor(ArithmeticVisitor):

    def visitExpr(self, ctx:ArithmeticParser.ExprContext):
        left = int(ctx.DIGIT(0).getText())
        right = int(ctx.DIGIT(1).getText())
        op = ctx.OP().getText()

        if op == '+':
            return left + right
        elif op == '-':
            return left - right
        elif op == '*':
            return left * right
        elif op == '/':
            # Manejo de division por cero
            if right == 0:
                raise ValueError("Error: Division por Cero")
            return left / right