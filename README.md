# BirdieChallenge

### Repositório com a solução do desafio técnico da Birdie

# CONFIGURANDO O AMBIENTE
1. Recomenda-se criar um virtual enviroment para instalar as depêncidas utilizadas nesse projeto.

2. Após isso execute o comando:
>$ pip install -r requirements.txt

3. Com isso o ambiente está pronto para a execução do projeto.


# EXECUTANDO SCRAPING

1. Para iniciar o scraping execute o script run.sh
>$./run.sh
Esse script realizará o download da lista de Urls, agrupa-las por loja e inicia o scraping das paginas utilizando a ferramenta Scrapy.

# EXECUTANDO API
1. Para executar a API execute o arquivo run_api.py.
>$./run_api.sh
A API será inicializada e os resultados do scraping poderão ser consultados.

# Documentação da API
A API fornece 4 tipos de busca: nomes que contém a string passada, intervalo de valores, lojas e todos os items.

### Nomes que contém a string passada
- /productName?name=string

### Intervalo de preços
- /price?min=float&max=float

Os argumentos min e max são opcionais e possuem valores default. 
 - min = 0
 - max = 1000000

### Lojas
 - /store?store=string

 Os valores possíveis são" Magazine Luiza" e "Mercado Livre".

### Todos
 - /all

 Retorna todos os dados


# ARQUITETURA DA SOLUÇÃO
A seguir um resumo dos arquivos em ordem que devem serão executados pelos scripts:

### DownloadUrls
Esse arquivo executa o download das urls direto do  google planilhas no formato csv e armazena com o nome "urls.csv".

### GroupUrls
Esse arquivo realiza o agrupamento das urls em listas em relação a loja que pertencem. As listas são armazenadas na pasta urlsBuffers para serem usadas posteriormente.

### ofertas_service/ofertas_api
Esse inicia a API para as consultas no banco de dados


### BirdieChalenge/Craw
Arquivo que inicia a execução dos spiders no scrapy.

# ARQUITETURA DO SCRAPY
Utilizando o scrapy foi possivel realizar o scraping das urls, o tratamento e armazenamento em um banco de dados não relacional(MongoDB).

Ao iniciar os spiders do scrapy (arquivo craw), os seguintes passos ocorrem:
1. Os spiders realizam o request das páginas e extraem os dados solicitados, criando Items.  
2. Após criados os itens eles são tratados no arquivo "pipelines", onde são feitas as seguintes verificações:
    1. Se o nome dos produtos e o preço foram obtidos
    2. Retirados caracteres inválidos
    3. Preço são transformados no tipo float
    4. Centavos são acrescentados no preço
    5. Item é inserido no banco de dados caso
    - Obs: caso o Item não tenha nome ou preço ele é descartado

## Spiders
Foram criados 3 spiders para o scraping:
 - Mercado Livre
 - Casas Bahia
 - Magazine Luiza

Cada spider extrai os dados das paginas de sua loja, mas no final todos os items gerados são tratados no mesmo pipeline.

## Itens

Os item possuem os seguintes parâmetros:
 -  Name
 - Price
 - Cents (utilzado até ser acrescentado ao price)
 - Store
 - Url
 - Last Update


# DESAFIOS ENCONTRADOS

### Tempo para requests
Após ver o tempo que levava o scraping utilizando o Selenium, foi procurada uma ferramenta para melhorar essa performance. Assim foi encontrado o Scrapy que realizada o scraping em um tempo consideravelmente menor. Porém após ver que muitas urls eram redirecionadas para paginas de verificação de contas ou robots descobri que o tempo entre requests para o mesmo dominio deveria ser maior que 2. Assim esse tempo foi alterado nas configurações do Scrapy e spiders individuais foram criados para cada dominio.

### UserAgents
Após verificar que o dominio da Casas Bahia não era acessado e sempre retornava o erro 403, após algumas pesquisas estudei sobre os UserAgents e sua importância no scraping. Ao fim foi instalado um pacote para usar UserAgents aleatórios, e foi escolhido usar UserAgents de mobile, porém como eram alterados os nomes das classes do HTML utilizados para o scraping, foi então testado usar UserAgents de desktop do navegador Opera, o que retornou resultados satisfatórios e eram acessados todos os dominios. 

### Scraping no site da CasasBahia
Após conseguir acessar o dominio da Casas Bahia foi notado que os dados não eram extraidos do HTML. Após algumas pesquisas foi notado que o dominio utiliza JavaScript para extrair os dados. Usando a ferramenta scrapy-splash as paginas eram armazenadas e acessado o HTML, porém os dados não foram obtidos dessa forma. Outra forma utilizada foi transformar o JavaScript em XML pois os dados estavam presentes do código JavaScript da página, porém após notar que os valores de preço estavam nulos não foi possível obter eles. Assim o spider da Casas Bahia não é executado e **não foram obtidos os dados desse dominio**.

### Banco de dados local
O banco de dados utilizado foi o MongoDB, ele armazena os dados extraidos e é acessado pelo código da API para disponibiliza-los. Como o banco é local então os dados não foram disponibilizados. Porém após 5 minutos de execução do scraping já se obtém dados satisfatórios para o teste da API. Em uma das execuções feitas o scraping executou por 13 horas e não finalizou todas a urls.
    




