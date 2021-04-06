# desenvolvendo-com-JP

Jogo da forca.

O jogo da forca consiste basicamente de um jogador tentar adivinhar uma palavra secreta, sendo exibida apenas uma sequencia de traços "_" contendo a quantidade de letras da palavra. O jogador terá um numero pré definido de chances, onde ele poderá ir falando letras que imagina fazer parte da palavra. Para cada letra acertada a posição onde a letra se encontra na palavra será revelada e para cada erro uma chance será diminuída. O jogo termina de duas maneiras:
A primeira opção, o jogador consegue acertar todas as letras e a palavra se revela por completo.
A segunda opção, o jogador erra até que suas chances zerem, assim ele perde o jogo.

Esse jogo poderá ser em pares ou apenas um jogador.

Para o jogo em pares: Dois jogares decidem quantas partidas irão jogar e um deles inicia informando uma palavra e uma dica. Dando vez ao outro jogador que passa então ao cenario falando anteriormente.
Para o jogo com apenas um jogador: Inicialmente o jogo está pensando para o computador escolher num banco de dados palavras aleátorias podendo conter ou não dicas. Depois de escolhida a palavra o jogador inicia então.
( Também está em processamento a idéia do jogador escolher uma palavra e o computador tentar adivinhar. Como seria isso? O jogador escolhe a palavra então o computador começa aleátoriamente chutar letras. Quanto ele acertar pelo menos uma, inicia então uma busca em banco de dados a partir da quantidade de letras e posições das letras. O computador vai separando numa lista a cada iteração apenas palavras compativéis com a rodada atual.
   EX: o computador conseguiu acertar a letra A na palavra "A _ _ _", com isso ele irá separar todas as palavras de 4 letras e que iniciam em A.
   Verificar possivel API para busca em alfabeto contendo todas as palavras. 
  
 Para iniciar o jogo:
  O jogador terá que informar seu nome.
  Informar quantas rodadas irá jogar.
  Decidir quantas chances será. 
      Menor chance possivel 4
      Maior chance possivel 10
  O jogo então faz um sorteio aleátorio para decidir quem inicia ( caso seja em dupla), se for contra o PC inicia normalmente quanto o jogador apertar INICIAR.
  
  
  Vide Documento de arquitetura
  Primeira versão do jogo - V1:
  * O jogo será escrito em python3.
  * Será usado como banco de dados, arquivos de texto.
  * Não será usado orientação a objetos.
  * O jogo não irá ter uma interface gráfica.
  * O jogo não terá o computador tentando advinhar as palvras.
  
  Segunda versão V2:
  * O jogo será escrito em python3.
  * Será usado como banco de dados, mysql.
  * será usado orientação a objetos.
  * O jogo não irá ter uma interface gráfica.
  * O jogo não terá o computador tentando advinhar as palvras.
   
  Terceira versão V2:
  * O jogo será escrito em python3.
  * Será usado como banco de dados, mysql.
  * será usado orientação a objetos.
  * O jogo terá uma interface gráfica.
  * O jogo terá o computador tentando advinhar as palvras.
    
  
  Ferramentas usadas:
  IDE compativel com python3
  python3
  ASANA para organização das checklist
  
  
