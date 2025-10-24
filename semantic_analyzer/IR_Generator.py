
import json

class IRGenerator:
    """Genera el JSON final y muestra las estadísticas del horario."""

    def __init__(self, symbol_table):
        self.symbol_table = symbol_table

    def generar_json(self, salida="salida.json"):
        """Crea el archivo JSON con el horario validado."""
        with open(salida, "w", encoding="utf-8") as f:
            json.dump(self.symbol_table.horario, f, indent=2, ensure_ascii=False)
        print(f"\n✅ Archivo {salida} generado correctamente.")

    def mostrar_estadisticas(self):
        """Imprime estadísticas generales del horario."""
        stats = self.symbol_table.estadisticas()
        print("\n📊 ESTADÍSTICAS DEL HORARIO")
        print("----------------------------")
        for k, v in stats.items():
            print(f"{k}: {v}")
        print("----------------------------")
