from antlr4 import *
from generated.CSVLexer import CSVLexer
from generated.CSVParser import CSVParser
from semantic_analyzer.SemanticListener import SemanticListener
from semantic_analyzer.IR_Generator import IRGenerator

def main():
    # 1️ Lectura del archivo CSV de entrada
    input_stream = FileStream("datos.csv", encoding="utf-8")

    # 2️ Fases léxica y sintáctica (ANTLR)
    lexer = CSVLexer(input_stream)           # Analizador léxico
    tokens = CommonTokenStream(lexer)        # Flujo de tokens
    parser = CSVParser(tokens)               # Analizador sintáctico
    tree = parser.csvFile()                  # Estructura sintáctica (árbol)

    # 3️ Fase semántica: validar datos y construir tabla
    listener = SemanticListener()
    walker = ParseTreeWalker()
    walker.walk(listener, tree)              # Recorre el árbol con el listener

    # 4️ Mostrar errores semánticos (si existen)
    if listener.errors:
        print("⚠️ ERRORES DETECTADOS:")
        for e in listener.errors:
            print("  -", e)
        return

    # 5️ Fase intermedia: generar archivo JSON + estadísticas
    ir = IRGenerator(listener.symbol_table)
    ir.generar_json()
    ir.mostrar_estadisticas()

if __name__ == "__main__":
    main()
