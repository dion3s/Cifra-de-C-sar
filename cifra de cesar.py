TAM_MAX_CH = 26 # tamanho maximo da chave de rotação.
 
def recebeModo():
    """
    Função que pergunta se o usuário quer criptografar ou
    decriptografar e garante que uma entrada válida foi recebida
    """
 
    while True:
        modo = input("Você deseja criptografar ou decriptografar?\n").lower()
        if modo in 'criptografar c decriptografar d'.split():
            return modo
        else:
            print("Entre 'criptografar' ou 'c' ou 'decriptografar' ou 'd'.")
 
def recebeChave():
    """
    Função que pede o valor da chave para o usuário
    e devolve a chave caso o valor desta esteja adequado
    """
    global TAM_MAX_CH
    chave = 0
 
    while True:
        chave = int(input('Entre o número da chave (1-%s)\n'%(TAM_MAX_CH)))
 
        if 1 <= chave <= TAM_MAX_CH:
            return chave
 
def geraMsgTraduzida(modo, mensagem, chave):
    """
    Traduz a mensagem do usuário de modo conveniente
    Usar a rotação(13) e gravar no arquivo criptografado 
    """
    if modo[0] == 'd':
        chave *= -1
 
    traduzido = ''
 
    for simbolo in mensagem:
        if simbolo.isalpha():
            num = ord(simbolo)
            num += chave
 
            if simbolo.isupper():
                if num > ord('Z'):
                    num -= 26
                elif num < ord('A'):
                    num += 26
            elif simbolo.islower():
                if num > ord('z'):
                    num -= 26
                elif num < ord('a'):
                    num += 26
 
            traduzido += chr(num)
            file = open('arquivo.txt', 'w')
            file.write(traduzido)
            file.close()
        else:
            traduzido += simbolo
            
            
    return traduzido
 
def main():
    """
    Função principal do codigo onde vai receber o arquivo, ler ele e criptografar
    """
    modo = recebeModo()
    arq = input("Digite o nome do arquivo: ")
    file = open(arq, 'r')
    mensagem = file.read()
    file.close()
    
    chave = recebeChave()
 
    print("Seu arquivo está pronto!")
    geraMsgTraduzida(modo, mensagem, chave)
 
main()
