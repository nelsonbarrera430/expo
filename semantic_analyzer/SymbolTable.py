
class SymbolTable:
    """Tabla de símbolos: almacena la información validada del horario."""

    def __init__(self):
        # Estructuras internas
        self.horario = {}              # Diccionario: día → lista de clases
        self.materias = set()          # Conjunto de materias únicas
        self.salones = set()           # Conjunto de salones únicos
        # Días válidos permitidos
        self.dias_validos = {"Lunes", "Martes", "Miércoles", "Jueves", "Viernes", "Sábado"}

    def add_clase(self, dia, inicio, fin, materia, salon):
        """Agrega una clase validada al horario."""

        # Validar que el día sea válido
        if dia not in self.dias_validos:
            raise Exception(f"Día inválido: {dia}")

        # Si el día no está en la tabla, lo creamos
        if dia not in self.horario:
            self.horario[dia] = []

        # Validar conflictos de horario (traslape de horas)
        for c in self.horario[dia]:
            # Si el nuevo horario se cruza con otro existente
            if not (fin <= c["inicio"] or inicio >= c["fin"]):
                raise Exception(f"Conflicto horario el {dia}: {inicio}-{fin} con {c['inicio']}-{c['fin']}")

        # Si no hay errores, registramos la clase
        self.horario[dia].append({
            "inicio": inicio,
            "fin": fin,
            "materia": materia,
            "salon": salon
        })

        # Añadimos la materia y salón a sus conjuntos
        self.materias.add(materia)
        self.salones.add(salon)

    def estadisticas(self):
        """Devuelve estadísticas descriptivas del horario."""
        total_dias = len(self.horario)
        total_clases = sum(len(v) for v in self.horario.values())
        total_materias = len(self.materias)
        total_salones = len(self.salones)
        clases_por_dia = {dia: len(v) for dia, v in self.horario.items()}

        # Devolvemos un resumen útil
        return {
            "Total días": total_dias,
            "Total clases": total_clases,
            "Total materias": total_materias,
            "Total salones": total_salones,
            "Clases por día": clases_por_dia
        }
