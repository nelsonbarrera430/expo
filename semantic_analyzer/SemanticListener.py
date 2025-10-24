from generated.CSVListener import CSVListener
from semantic_analyzer.SymbolTable import SymbolTable
import re

class SemanticListener(CSVListener):
    """Listener semántico: valida cada fila de datos del CSV."""

    def __init__(self):
        self.symbol_table = SymbolTable()   # Donde se guarda la información válida
        self.header = []                    # Encabezado del CSV
        self.errors = []                    # Lista de errores detectados
        self.is_header = True               # Bandera para saber si estamos en el encabezado

    def enterRow(self, ctx):
        """Se ejecuta cada vez que el parser entra a una fila (row)."""
        fields = [f.getText().replace('"', '') for f in ctx.field()]

        # Si la fila está vacía o incompleta, se ignora
        if len(fields) < 5:
            return

        # La primera fila se guarda como encabezado
        if self.is_header:
            self.header = fields
            self.is_header = False
        else:
            try:
                # Validar y registrar la clase
                self.validar_y_agregar(fields)
            except Exception as e:
                # Si algo falla, se registra el error pero no se detiene el programa
                self.errors.append(str(e))

    def validar_y_agregar(self, fields):
        """Valida una fila del CSV y la agrega si es correcta."""
        dia, inicio, fin, materia, salon = [x.strip() for x in fields]

        # Validar formato de hora (HH:MM)
        if not re.match(r"^\d{2}:\d{2}$", inicio) or not re.match(r"^\d{2}:\d{2}$", fin):
            raise Exception(f"Formato de hora inválido: {inicio}-{fin}")

        # Validar orden de las horas
        if inicio >= fin:
            raise Exception(f"Hora de inicio mayor o igual que fin: {inicio}-{fin}")

        # Si todo bien, se agrega a la tabla de símbolos
        self.symbol_table.add_clase(dia, inicio, fin, materia, salon)
