# Desafios IDwall

Pedro Augusto Santos Orona Silva [Linkedin](https://www.linkedin.com/in/pedro-augusto-santos-orona-silva-476950122/)

A seguir seguem as soluções desenvolvidas, todas em python, para os desafios propostos:

## Manipulação de strings
Primeiramente, foi definido o texto a ser formatado dentro do arquivo [input](https://github.com/PedroOrona/desafios/blob/master/strings/input.txt), após esta primeira etapa, foi realizada contrução da solução utilizando. A primeira parte do trabalho se resumiu à utilização da biblioteca *textwrap*, utilizada para separação do texto utilizando o comprimento indicado. Para a segunda parte eu acabei construindo o código sem a utilização da biblioteca, tendo assim maior controle da formatação. 

Executando o [código](https://github.com/PedroOrona/desafios/blob/master/strings/string_idwall.py) através do comando:

`$ python string_idwall.py`

é gerado o seguinte resultado:
```
Texto Formatado:

In the beginning God created the heavens
and   the   earth.  Now  the  earth  was
formless  and  empty,  darkness was over
the  surface of the deep, and the Spirit
of  God  was  hovering  over the waters.

And  God said, "Let there be light," and
there  was light. God saw that the light
was  good,  and  he  separated the light
from  the darkness. God called the light
"day,"   and   the  darkness  he  called
"night."  And  there  was  evening,  and
there  was  morning  -  the  first  day.
```

sendo que, podemos testar para qualquer texto, apenas modificando o arquivo citado anteriormente.

**Obs.**:
- Eu pensei em não justificar a última linha de cada parágrafo, para ficar mais no padrão, porém no exemplo isso não foi realizado, então preferi manter como instruído nos exemplos.

## Crawlers

### Parte 1 - Versão CLI

Para a versão console foi utilizada a biblioteca *BeautifulSoup*, seguindo a dica oferecida.

Inspecionando as páginas do Reddit, na versão *old*, foram encontradas as tags em html que oferecem os conteúdos buscados para cada thread dentro dos subreddits: número de upvotes, título do subreddit, título da thread, link para os comentários da thread, link da thread.

Apenas para melhor compreensão do código, explicarei alguns trechos.

Nesta parte eu apenas removo da coleção, as threads que possuem menos que 5000 upvotes, para, por fim, poder apresentar as mais populares para o usuário. Para o cuso do subreddit não possuir nenhuma thread que possua o mínimo de upvotes definido, o programa imprime a mensagem de que este não possui nenhuma thread relevante.

```ruby
i, k = 0, 0
j = len(upvotes)        
while k < j:
    if int(upvotes[i]) < 5000:
        upvotes.pop(i)
        title.pop(i)
        link.pop(i)
        comments_link.pop(i)
    else:
       i = i + 1 
    k = k + 1    

if len(upvotes) == 0:
    print("Nenhuma thread relevante para o subreddit: {0}".format(u))
```

Os headers permitem simular um acesso via browser, por isso a definição do agente abaixo; sem eles o reddit bloqueava todas as vezes o meu acesso, e pedia para eu esperar um tempo antes de tentar executá-lo novamente.

```ruby
def request(url):
    headers = {'User-Agent': 'Mozilla/5.0'}
    source = requests.get('https://old.reddit.com/r/' + url + '/', headers=headers)
    return source
```

Então, executando o [código](https://github.com/PedroOrona/desafios/blob/master/crawlers/crawlers_idwall.py) através do seguinte comando:

`$ python crawlers_idwall.py`

o programa pede para o usuário entrar com os subreddits separados por ponto-e-vírgula, como por exemplo:
`askreddit;worldnews;cats`

e então retorna todas as informações das threads relevantes de cada subreddit.

### Parte 2 - Bot Telegram

Para criar o Bot que se conecte ao Telegram, foi preciso conversar com o @BotFather, dentro do telegram. Ele é o responsável pela criação de novos bots. Para isso, foi enviad o seguinte comando: `\newbot`.

Após definir um nome para o bot, *NadaPraFazerBot*, e um nome de usuário, *@idwall_bot*, podemos realizar a conexão com ele, através do token retornado pelo *BotFather*.

Para nos conectarmos ao bot que criamos usando o BotFather utilizamos o módulo python-telegram-bot, o qual realiza a conexão do programa com a API de bots do Telegram.

Para instalar este módulo, usamos o pip:

`pip install python-telegram-bot`

Agora podemos definir nossa [main](https://github.com/PedroOrona/desafios/blob/master/crawlers/crawlers_idwall_bot.py), contendo a conexão e os handlers a serem definidos por nós:

```ruby
updater = Updater(token='768765479:AAFAOG6qA5gZzAIduOCI4OOak5Q_sfOA7dc')
dispatcher = updater.dispatcher
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                 level=logging.INFO)

start_handler = CommandHandler('start', start)
dispatcher.add_handler(start_handler)
dispatcher.add_handler(CommandHandler('NadaPraFazer', NadaPraFazer, pass_args=True))
updater.start_polling()
updater.idle()
```

Foi setado também o módulo *login* para monitorar caso algo dê errado. Rodando a main, mantemos o programa em execução, podendo ser parado a qualquer momento, terminando assim a conexão com o bot *NadaPraFazerBot*.

Para realizar a busca dos dados do Reddit, devemos apenas adicionar o código desenvolvido na parte 1, definindo esta seção do programa, como um Handler, chamado aqui de *NadaPraFazer*, que recebe como argumento a lista de subreddits que o usuário tem interesse em explorar.

Logo, enviando para o bot a seguinte mensagem, por exemplo:

`/NadaPraFazer askreddit;worldnews;cats`

este irá enviar todas as informações definidas na parte 1 do desafio, porém agora via telegram, como apresnetado na figura a seguir:

![alt text](https://github.com/PedroOrona/desafios/blob/master/crawlers/telegram_bot.png)

- Para mais informações, sugiro que se explore os códigos desenvolvidos em python. 
- Foram comentadas as partes que eu considerei mais relevantes e que talvez necessitaram de uma maior explicação.  

Um abraço! :space_invader:
