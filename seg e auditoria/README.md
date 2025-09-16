# Projeto de Criptografia em Python

Este projeto foi desenvolvido para a disciplina de Segurança e Auditoria de Sistemas e implementa um sistema criptográfico com duas camadas de cifras: Transposição Colunar e Vigenère.

## Dependências e Requisitos

Este projeto não possui dependências externas. Para executá-lo, você precisa apenas de:

- **Python 3.6 ou superior**

Nenhuma outra biblioteca precisa ser instalada, pois o código utiliza apenas recursos da biblioteca padrão do Python.

## Funcionalidades

- **`cifrar.py`**: Lê um texto de `texto.txt`, solicita uma senha e gera um arquivo `cifrado.txt` com o conteúdo criptografado.
- **`decifrar.py`**: Lê o arquivo `cifrado.txt`, solicita a senha e gera um arquivo `decifrado.txt` com o conteúdo original.

## Como Executar

1.  Certifique-se de ter o Python 3 instalado.
2.  Clone este repositório para a sua máquina.
3.  Edite o arquivo `texto.txt` com a mensagem a ser cifrada.
4.  Para cifrar, execute no terminal:
    ```bash
    python cifrar.py
    ```
5.  Para decifrar, execute:
    ```bash
    python decifrar.py
    ```

## Arquivos no Projeto

- `cifrar.py`: Script para criptografar.
- `decifrar.py`: Script para descriptografar.
- `texto.txt`: Arquivo de entrada com o texto em claro.
- `cifrado.txt`: (Gerado) Arquivo com o texto cifrado.
- `decifrado.txt`: (Gerado) Arquivo com o texto decifrado.