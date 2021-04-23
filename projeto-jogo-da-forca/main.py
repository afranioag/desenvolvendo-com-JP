
#coding: utf-8
import os

'''
    executar com python3 via terminal - python .\main.py -
'''

# guarda as letras já informadas
def words(char, list_char):
    if(char == "" or char in list_char or len(char) > 1 ):
        return sorted(list_char)
    list_char.append(char)
    return sorted(list_char)

# recebe a palavra e ecripta
def encrypts(word):
   return list((word.__len__() * "-"))

# verifica se a letra existe dentro da palavra
def compare_char(word, char):
    if(word.__contains__(char)):
        return True
    return False

# verifica se a palavra secreta ja e igual a palavra informada
def compare(word, secret):
    word_secret = ""
    for i in secret:
        word_secret += i
    return word_secret == word

# se a letra existe ela modifica a palavra
def update(secret, word, char):
    for i in range(word.__len__()):
        if(word[i] == char):
            secret[i] = char
    
    return secret

# exibe na tela durante o jogo
def prints(word):
    show = word[0]
    for i in range(1,len(word)):
        show += (" "+ (word[i]))
    print("WORD: "+show)

# o jogador informa uma palavra e uma dica e essas são armazenadas em arquivo txt
def word_game():
    word = input("Digite uma palavra para o inicio do jogo :\n")
    if os.name == 'posix':
        os.system('clear')
    else:
        os.system('cls')

    trip = input("Informe uma dica para a palavra :\n")
    if os.name == 'posix':
        os.system('clear')
    else:
        os.system('cls')
    
    with open('database.txt', 'a') as add:
        print(word, file=add)
        print(trip, file=add)
    return word.upper()
#armazena as palavras e as dicas em um dicioário
def data_base() -> dict:
    key = []
    value = []
    db = {}
    with open('database.txt') as look:
        w = look.read()
        colection = w.split('\n')
        colection.pop()
    for i in range(len(colection)):
        if i%2 == 0:
            key.append(colection[i])
        else:
            value.append(colection[i])
    for i in range(len(key)):
        db[key[i]] = value[i]
    return db
def char_game():
    char = input("Iforme uma letra :")
    if os.name == 'posix':
        os.system('clear')
    else:
        os.system('cls')

    return char.upper()

def game():
    if os.name == 'posix':
        os.system('clear')
    else:
        os.system('cls')
    word = word_game()
    word_encrypt = encrypts(word)
    chances = 5
    words_dig = []
    char = ""
    while(True):
        print("-------------------------------------")
        print("CHARS ", words(char, words_dig))
        print("CHANCES ", chances)
        prints(word_encrypt)
        print("-------------------------------------")
              
        char = char_game()
        if(not compare_char(word, char)):
            chances -= 1

            if(chances == 0):
                if os.name == 'posix':
                    os.system('clear')
                else:
                    os.system('cls')

                print("\n\nYOU LOSER!!!\n\n\n")
                break

        word_encrypt = update(word_encrypt, word, char)

        if(compare(word, word_encrypt)):
            if(chances == 0):
                if os.name == 'posix':
                    os.system('clear')                          
                else:
                    os.system('cls') 
            print("\n\nYOU WIN!!!\n\n\n")
            print(data_base())
            break
        
        
        
           
    

def __main__ ():
    game()

if __name__ == '__main__':
    __main__()
