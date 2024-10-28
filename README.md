# Usabit Technical Test
Este é um projeto para teste técnico na empresa Usabit que cria um command para
pesquisar cidades pelo ID no OpenWeather API e popular dados de temperatura

***

## Pré-requisitos
- Docker
- Docker Compose

## Instalação
- Clone o repositório:
```bash
git clone https://github.com/gi0dogr4u/usabit-technical-test.git
```

- Crie e ative um ambiente virtual (opcional, mas recomendado):
```bash
python -m venv .venv
```

- Para Linux/Mac
```bash
source .venv/bin/activate  
# Para Windows
.venv\Scripts\activate  

# Para Linux  
source .venv/bin/activate
```

- Instale as dependências:
```bash
pip install -r requirements.txt
```

## Configurando variáveis de ambiente
Crie um arquivo .env utilizando o .env-example na raiz do projeto para configurar as variáveis de ambiente
OBS: Crie uma API Key para o OpenWeather em https://openweathermap.org/api. 

```bash
OPENWEATHER_API_KEY=your_openweather_api_key
```

## Configuração do Docker
Construa e inicie os containers (lembre-se de criar um .env):

```bash
docker-compose up -d 
```

## Executando as migrações do banco de dados
Com o contêiner PostgreSQL em execução, execute as migrações para configurar o banco de dados:

```bash
python manage.py migrate
```

## Executando o command
Depois de garantir que o banco está em execução, execute o seguinte comando para carregar os dados de clima:

```bash
python manage.py load_data
```

## Visualizando Painel Admin
- Primeiro, crie um Django Superuser para acessar o admin:
```bash
python manage.py createsuperuser
```
- Depois de rodar as migrações e o command e criar o superuser, você pode subir a aplicação e acessar o Painel Admin em http://127.0.0.1:8000/
```bash
python manage.py runserver
```


