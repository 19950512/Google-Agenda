# Gooogle Agenda
Google Agenda com Python3


## O que preciso ter instalado ?
Eu fiz o script, testes tudo mais utilizando *<b>Python3</b>* junto  com *<b>PIP3</b>* _(Gerenciador de pacotes, tipo NPM, YARN, APT, SNAP, COMPOSER, etc..)._<br/>
Caso você não tenha o python3 ou o pip3, segue para instalar
```sh
  sudo apt-get install software-properties-common
  sudo add-apt-repository ppa:deadsnakes/ppa
  sudo apt-get update
  sudo apt-get install python3.9    # Instalar o Python3
  sudo apt-get install python3-pip  # Instalar o PIP3
```

<br />


## O que preciso instalar ?
recomendo antes executar
```sh
  sudo apt-get update
  sudo apt-get upgrade
```

agora, vamos instalar a lib da Google Client (Google client library)
```sh
  pip3 install --upgrade google-api-python-client google-auth-httplib2 google-auth-oauthlib
```

<br />

Você pode ver mais sobre no link <a href="https://developers.google.com/calendar/quickstart/python" target="_blank">Quickstart</a>

<br />

## Baixei tudo, e agora ?
<ol>
  <li>Entrar no console da Google - <a href="https://console.cloud.google.com" target="_blank">LINK</a></li>
  <li>Criar um projeto <i>se não tiver</i> - <a href="https://developers.google.com/workspace/guides/create-project" target="_blank">LINK</a></li>
  <li>Ativar a API Agenda <i>se não tiver</i> - <a href="https://console.cloud.google.com/apis/library/calendar-json.googleapis.com?id=84f291c9-2585-4af1-a78b-09c53a78202f" target="_blank">LINK</a></li>
  <li>Criar (ID do cliente OAuth 2.0) e Baixar a <i>credentials.json</i> - <a href="https://console.cloud.google.com/apis/api/calendar-json.googleapis.com/credentials" target="_blank">LINK</a></li>
</ol>

Colocar o arquivo credentials.json na raíz do projeto.

<br />

## Com isso tudo, já podemos brincar.

<br />

Com o terminal, na raíz do projeto...
### Criar um Evento
```sh
  python3 main.py --acao criar --titulo "Hello World!" --descricao "programador.dev"
```
O output do comando é um "json" com informações do evento, o mais importante é o ID, esse você deve guardar em algum lugar (DB) para gerenciar, alterar, remover, etc..

OBS: Por default, irá criar o evento na Agenda no momento em que foi executado. Para criar um evento com outra data/hora, é só informar 2 parametros no formato (_2021-04-15 01:55:00_)

```sh
  python3 main.py --acao criar --titulo "Hello World!" --descricao "programador.dev" --inicio "2021-04-15 01:55:00" --fim "2021-04-15 02:15:00" 
```

<br />

### Listar Eventos | Calendarios
```sh
  python3 main.py --listar eventos
  python3 main.py --listar calendarios
```
Você quer listar os eventos para pegar o ID para atualizar ou excluír.

<br />

### Atualizar um Evento
```sh
  python3 main.py --acao atualizar --titulo "Programador.DEV" --descricao "programador.dev" --id eventId
```
Você pode atualizar tudo sobre um evento, "jogar" ele para outra data, mudar descrição, titulo, etc..

<br />

### Deletar um Evento
```sh
  python3 main.py --acao deletar --id eventId
```

<br />

## Em breve mais atualizações..
