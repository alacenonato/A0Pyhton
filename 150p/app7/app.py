import string
from collections import Counter


def analisar_texto(texto):
    # Remover pontuação
    texto_limpo = texto.translate(str.maketrans('', '', string.punctuation))

    # Padronizar para minúsculas
    texto_limpo = texto_limpo.lower()

    palavras = texto_limpo.split()

    # Contagem
    total_palavras = len(palavras)
    total_caracteres = len(texto)
    total_frases = texto.count('.') + texto.count('!') + texto.count('?')

    frequencia = Counter(palavras)

    palavra_mais_comum = frequencia.most_common(1)

    return {
        "palavras": total_palavras,
        "caracteres": total_caracteres,
        "frases": total_frases,
        "frequencia": frequencia,
        "mais_comum": palavra_mais_comum
    }


def main():
    print("===== ANALISADOR DE TEXTO =====")

    try:
        texto = input("Digite um texto: ")

        if not texto.strip():
            raise ValueError("Texto vazio!")

        resultado = analisar_texto(texto)

        print(f"\nTotal de palavras: {resultado['palavras']}")
        print(f"Total de caracteres: {resultado['caracteres']}")
        print(f"Total de frases: {resultado['frases']}")

        if resultado["mais_comum"]:
            palavra, qtd = resultado["mais_comum"][0]
            print(f"Palavra mais frequente: '{palavra}' ({qtd}x)")

        print("\nFrequência de palavras:")
        for palavra, qtd in resultado["frequencia"].items():
            print(f"{palavra}: {qtd}")

    except Exception as e:
        print(f"Erro: {e}")


if __name__ == "__main__":
    main()