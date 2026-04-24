import sys
from pyflowchart import Flowchart

def main():
    if len(sys.argv) < 2:
        print("Uso: python gerar_grafo.py <arquivo.py>")
        return

    file_path = sys.argv[1]
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            code = f.read()

        fc = Flowchart.from_code(code)
        print("\n--- COPIE O CÓDIGO ABAIXO ---\n")
        print(fc.flowchart())
        print("\n--- FIM ---\n")
        print("DICA: Cole o código acima no site: https://flowchart.fun/")
    except Exception as e:
        print(f"Erro: {e}")

if __name__ == "__main__":
    main()
