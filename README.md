# Desafios IDwall

Pedro Augusto Santos Orona Silva [Linkedin](https://www.linkedin.com/in/pedro-augusto-santos-orona-silva-476950122/)

A seguir seguem as soluções desenvolvidas, todas em python, para os desafios propostos:

## Manipulação de strings
Primeiramente, foi definido o texto a ser formatado dentro do arquivo [input](https://github.com/PedroOrona/desafios/blob/master/strings/input.txt), após esta primeira etapa, foi realizada contrução da solução utilizando. A primeira parte do trabalho se resumiu à utilização da biblioteca *textwrap*, utilizada para separação do texto utilizando o comprimento indicado. Para a segunda parte eu acabei construindo o código sem a utilização da biblioteca, tendo assim maior controle da formatação. 

Executando o código através do comando:

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

Apenas explicando alguns trechos do código:
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
Nesta parte eu apenas removo da coleção, as threads que possuem menos que 5000 upvotes, para, por fim, poder apresentar as mais populares para o usuário.

```ruby
def request(url):
    headers = {'User-Agent': 'Mozilla/5.0'}
    source = requests.get('https://old.reddit.com/r/' + url + '/', headers=headers)
    return source
```

Os headers permitem simular um acesso via browser; sem eles o reddit bloqueava todas as vezes o meu acesso, e pedia para eu esperar um tempo antes de tentar executá-lo novamente.

Então, executando o [código](https://github.com/PedroOrona/desafios/blob/master/crawlers/crawlers_idwall.py) através do seguinte comando:

`$ python crawlers_idwall.py`

o programa pede para o usuário entrar com os subreddits separados por ponto-e-vírgula, como por exemplo:
`askreddit;worldnews;cats`

e então retorna todas as informações das threads relevantes de cada subreddit.




