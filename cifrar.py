def leitor(arquivo: str):
    with open(arquivo, "r", encoding="utf-8") as f:
        conteudo = f.read().lower()
    conteudo = conteudo.replace(" ", "_").replace("\n", "")
    return conteudo


def cifra_transposicao(texto: str, senha: str) -> str:
    colunas = len(senha)
    linhas = -(-len(texto) // colunas)
    matriz = [["" for _ in range(colunas)] for _ in range(linhas)]
    
    k = 0
    for i in range(linhas):
        for j in range(colunas):
            if k < len(texto):
                matriz[i][j] = texto[k]
            else:
                matriz[i][j] = '*'
            k += 1

    ordem = sorted(range(len(senha)), key=lambda x: senha[x])

    cifrado = ""
    for indice_coluna in ordem:
        for i in range(linhas):
            cifrado += matriz[i][indice_coluna]

    return cifrado


def cifra_substituicao(texto: str, senha: str) -> str:
    alfabeto = 'abcdefghijklmnopqrstuvwxyz_*'
    cifrado = ""
    tamanho_alfabeto = len(alfabeto)

    for i, char_texto in enumerate(texto):
        char_senha = senha[i % len(senha)]
        try:
            pos_texto = alfabeto.index(char_texto)
            pos_senha = alfabeto.index(char_senha)
            nova_pos = (pos_texto + pos_senha) % tamanho_alfabeto
            cifrado += alfabeto[nova_pos]
        except ValueError:
            cifrado += char_texto
            
    return cifrado

try:
    ARQUIVO_ORIGINAL = "texto.txt"
    ARQUIVO_CIFRADO = "cifrado.txt"

    texto_original = leitor(ARQUIVO_ORIGINAL)
    
    senha = input("Digite a senha para CIFRAR o texto: ")
    if not senha:
        print("Erro: A senha não pode estar vazia.")
    else:
        print("\n--- PROCESSO DE CIFRAGEM ---")
        print("Texto original :", texto_original)
        print("Senha          :", senha)
        print("-" * 30)

        texto_transposto = cifra_transposicao(texto_original, senha)
        print("1. Cifrado (Transposição) :", texto_transposto)

        texto_final_cifrado = cifra_substituicao(texto_transposto, senha)
        print("2. Cifrado (Final)        :", texto_final_cifrado)

        with open(ARQUIVO_CIFRADO, "w", encoding="utf-8") as f:
            f.write(texto_final_cifrado)
        
        print("-" * 30)
        print(f"O texto cifrado foi salvo com sucesso em '{ARQUIVO_CIFRADO}'")

except FileNotFoundError:
    print(f"Erro: Arquivo '{ARQUIVO_ORIGINAL}' não encontrado. Crie este arquivo e adicione o texto a ser cifrado.")