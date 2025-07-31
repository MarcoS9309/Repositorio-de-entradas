import os
import random
from datetime import datetime

CARPETA_DIARIO = "diario_entradas"

ESPIRAL = r"""
     @
    @ @
   @   @
    @ @
     @
"""

ONDA = r"""
~     ~     ~     ~
  ~     ~     ~
~     ~     ~     ~
"""

NUCLEO = r"""
   *****
  *     *
 *   •   *
  *     *
   *****
"""

VERTICE = r"""
    /\
   /  \
  /____\
"""

HORIZONTE = r"""
──────────────
──────────────
──────────────
"""

def crear_carpeta_si_no_existe():
    if not os.path.exists(CARPETA_DIARIO):
        os.makedirs(CARPETA_DIARIO)

def obtener_nombre_archivo():
    fecha_actual = datetime.now().strftime("%Y-%m-%d")
    return os.path.join(CARPETA_DIARIO, f"{fecha_actual}.md")

def seleccionar_ascii_abstracto():
    simbolos = [
        ("🔄 Espiral", ESPIRAL),
        ("🌊 Onda", ONDA),
        ("🌀 Núcleo", NUCLEO),
        ("🔺 Vértice", VERTICE),
        ("🧭 Horizonte", HORIZONTE),
    ]
    return random.choice(simbolos)

def agregar_entrada():
    print("\n📔 Bienvenido a tu Diario Reflexivo")
    print("Escribe tu entrada. Para terminar, escribe una línea con solo 'FIN'.\n")

    lineas = []
    while True:
        linea = input()
        if linea.strip().upper() == "FIN":
            break
        lineas.append(linea)

    contenido = "\n".join(lineas)
    archivo = obtener_nombre_archivo()
    titulo, simbolo = seleccionar_ascii_abstracto()

    with open(archivo, "a", encoding="utf-8") as f:
        f.write(f"\n## Entrada: {datetime.now().strftime('%H:%M:%S')}\n")
        f.write(contenido + "\n")
        f.write("\n---\n")
        f.write(f"### Símbolo abstracto del día: {titulo}\n")
        f.write(f"```\n{simbolo}\n```\n")

    print(f"\n✅ Entrada guardada en: {archivo}")
    print("\n🔷 Símbolo abstracto del día:")
    print(titulo)
    print(simbolo)

def main():
    crear_carpeta_si_no_existe()
    agregar_entrada()

if __name__ == "__main__":
    main()
