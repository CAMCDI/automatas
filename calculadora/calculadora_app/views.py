from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
import os
import sys


current_dir = os.path.dirname(__file__)
calculadora_dir = os.path.join(current_dir, 'calculadora')
sys.path.append(calculadora_dir)

try:
    from .calculadora.calculadora_visitor import MiCalculadoraVisitor
    from antlr4 import *
    from .calculadora.CalculadoraLexer import CalculadoraLexer
    from .calculadora.CalculadoraParser import CalculadoraParser
except ImportError as e:
    print(f"Error importando módulos: {e}")

def index(request):
    return render(request, 'calculadora/index.html')

@csrf_exempt
def ejecutar_codigo(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            codigo = data.get('codigo', '')
            
            print(f"Código recibido: {codigo}")  
            
            
            input_stream = InputStream(codigo)
            lexer = CalculadoraLexer(input_stream)
            stream = CommonTokenStream(lexer)
            parser = CalculadoraParser(stream)
            tree = parser.programa()
            
            visitor = MiCalculadoraVisitor()
            resultado = visitor.visit(tree)
            
            return JsonResponse({
                'success': True,
                'resultado': resultado,
                'pasos': visitor.pasos  
            })
            
        except Exception as e:
            return JsonResponse({
                'success': False,
                'error': str(e)
            })
    
    return JsonResponse({'error': 'Método no permitido'}, status=405)