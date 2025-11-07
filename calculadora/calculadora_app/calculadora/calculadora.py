#!/usr/bin/env python3
import sys
from antlr4 import *
from CalculadoraLexer import CalculadoraLexer
from CalculadoraParser import CalculadoraParser
from calculadora_visitor import MiCalculadoraVisitor

def ejecutar_codigo_predefinido(valores_usuario, operador):
    codigo = f"""
x = {valores_usuario['x']};
y = {valores_usuario['y']};
if (x {operador} y) {{
    z = x + y;
}}
"""
    
    print("\nEJECUCIÓN PASO A PASO")
    print("====================")
    
    try:
        input_stream = InputStream(codigo)
        lexer = CalculadoraLexer(input_stream)
        stream = CommonTokenStream(lexer)
        parser = CalculadoraParser(stream)
        tree = parser.programa()
        
        visitor = MiCalculadoraVisitor()
        resultado = visitor.visit(tree)
        
        print("\nRESULTADO FINAL")
        print("===============")
        print(f"Estado de variables: {resultado}")
        
    except Exception as e:
        print(f"Error: {e}")

def main():
    print("CALCULADORA - INGRESO DE DATOS")
    print("==============================")
    print("Operadores: >, <, ==, !=")
    
    valores = {}
    
    try:
        print("\nIngresa los valores:")
        valores['x'] = input("Valor para x: ").strip()
        valores['y'] = input("Valor para y: ").strip()
        
        operador = input("Operador (> < == !=): ").strip()
        
        operadores_validos = ['>', '<', '==', '!=']
        if operador not in operadores_validos:
            print("Error: Operador no válido")
            return
        
        if not valores['x'].isdigit() or not valores['y'].isdigit():
            print("Error: Los valores deben ser números")
            return
        
        ejecutar_codigo_predefinido(valores, operador)
        
    except KeyboardInterrupt:
        print("\nPrograma interrumpido")

if __name__ == '__main__':
    main()