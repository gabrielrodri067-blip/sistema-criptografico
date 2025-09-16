def decifra_substituicao(texto_cifrado: str, senha: str) -> str:
    alfabeto = 'abcdefghijklmnopqrstuvwxyz_*'
    decifrado = ""
    tamanho_alfabeto = len(alfabeto)

    for i, char_cifrado in enumerate(texto_cifrado):
        char_senha = senha[i % len(senha)]
        try:
            pos_cifrado = alfabeto.index(char_cifrado)
            pos_senha = alfabeto.index(char_senha)
            pos_original = (pos_cifrado - pos_senha + tamanho_alfabeto) % tamanho_alfabeto
            decifrado += alfabeto[pos_original]
        except ValueError:
            decifrado += char_cifrado
            
    return decifrado

def decifra_transposicao(texto_cifrado: str, senha: str) -> str:
    colunas = len(senha)
    linhas = -(-len(texto_cifrado) // colunas)
    matriz = [["" for _ in range(colunas)] for _ in range(linhas)]
    
    ordem = sorted(range(len(senha)), key=lambda x: senha[x])
    
    k = 0
    for indice_coluna in ordem:
        for i in range(linhas):
            matriz[i][indice_coluna] = texto_cifrado[k]
            k += 1
            
    decifrado = ""
    for i in range(linhas):
        for j in range(colunas):
            decifrado += matriz[i][j]
            
    decifrado_final = decifrado.replace('*', '').replace('_', ' ')
    
    return decifrado_final

try:
    ARQUIVO_CIFRADO = "cifrado.txt"
    ARQUIVO_DECIFRADO = "decifrado.txt"

    with open(ARQUIVO_CIFRADO, "r", encoding="utf-8") as f:
        texto_cifrado = f.read()

    senha = input("Digite a senha para DECIFRAR o texto: ")
    if not senha:
        print("Erro: A senha não pode estar vazia.")
    else:
        print("\n--- PROCESSO DE DECIFRAGEM ---")
        print("Texto cifrado  :", texto_cifrado)
        print("Senha          :", senha)
        print("-" * 30)

        texto_decifrado_subst = decifra_substituicao(texto_cifrado, senha)
        print("1. Decifrado (Substituição):", texto_decifrado_subst)

        texto_final_decifrado = decifra_transposicao(texto_decifrado_subst, senha)
        print("2. Decifrado (Final)     :", texto_final_decifrado)
        
        with open(ARQUIVO_DECIFRADO, "w", encoding="utf-8") as f:
            f.write(texto_final_decifrado)

        print("-" * 30)
        print(f"O texto decifrado foi salvo com sucesso em '{ARQUIVO_DECIFRADO}'")

except FileNotFoundError:
    print(f"Erro: Arquivo '{ARQUIVO_CIFRADO}' não encontrado. Cifre um texto primeiro usando o script 'cifrar.py'.")