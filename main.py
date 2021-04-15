#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys, os, argparse, json
from datetime import datetime, timedelta

dir_path = os.path.dirname(os.path.realpath(__file__))
sys.path.append(os.path.abspath(dir_path + '/Modulos/'))

# Importa os Módulos
import Criar, Listar, Deletar, Atualizar


# Instancia os módulos
Criar = Criar()
Listar = Listar()
Deletar = Deletar()
Atualizar = Atualizar()

# Parametros aceitos pelo Shell
args_parser = argparse.ArgumentParser(description='Google Calendario')
args_parser.add_argument("--listar", metavar="listar", default=None)
args_parser.add_argument("--acao", metavar="acao", default=None)
args_parser.add_argument("--id", metavar="id", default=None)

agora = datetime.now()

def zeroEsquerda(numero):
    return str('0' + str(numero) if numero < 10 else numero)

data_inicio = (str(agora.year) + '-' + zeroEsquerda(agora.month) + '-' + zeroEsquerda(agora.day) + ' ' + zeroEsquerda(agora.hour) + ':' + zeroEsquerda(agora.minute) + ':' + zeroEsquerda(agora.second))
data_fim = (str(agora.year) + '-' + zeroEsquerda(agora.month) + '-' + zeroEsquerda(agora.day) + ' ' + zeroEsquerda(agora.hour) + ':' + zeroEsquerda(agora.minute) + ':' + zeroEsquerda(agora.second))

args_parser.add_argument("--inicio", metavar="inicio", default=data_inicio)
args_parser.add_argument("--fim", metavar="fim", default=data_fim)
args_parser.add_argument("--titulo", metavar="titulo", default=None)
args_parser.add_argument("--descricao", metavar="descricao", default=None)

args = args_parser.parse_args()





# CASO FOR LISTAR CALENDARIO
if(args.listar == "calendarios"):

    Calendarios = Listar.calendarios()

    if(Calendarios == None):
        print("Nenhum calendario foi encontrado.")
        exit()

    print(Calendarios)
    exit()







# CASO FOR LISTAR EVENTOS
if(args.listar == "eventos"):

    Eventos = Listar.eventos()

    if(Eventos == None):
        print("Nenhum evento foi encontrado.")
        exit()

    print(Eventos)
    exit()







# CASO FOR CRIAR - e o titulo ou descricao for informado
if(args.acao == 'criar'):

    if(args.titulo == None or args.descricao == None):
        print("Informe qual é o Titulo e Descrição do evento para criar.")
        exit()

    # Monta o BODY
    body = '[{ "inicio": "' + args.inicio + '", "fim": "' + args.fim + '", "titulo": "' + args.titulo + '", "descricao": "' + args.descricao + '"}]'

    resposta = Criar.go(body)
    print(resposta)
    exit()







# CASO FOR ATUALIZAR - e o titulo ou descricao e ID for informado
if(args.acao == 'atualizar'):

    if(args.titulo == None or args.descricao == None or args.id == None):
        print("Informe qual é o ID, Titulo e Descrição do evento para atualiza-lo.")
        exit()

    # Monta o BODY
    body = '[{"id":"' + args.id + '", "inicio": "' + args.inicio + '", "fim": "' + args.fim + '", "titulo": "' + args.titulo + '", "descricao": "' + args.descricao + '"}]'

    resposta = Atualizar.go(body)
    print(resposta)
    exit()







# CASO FOR DELETAR - e o ID for informado
if(args.acao == 'deletar'):

    if(args.id == None):
        print("Informe qual é o ID do evento para deletar.")
        exit()

    Deletar = Deletar.codigo(args.id)

    if(Deletar == None or Deletar == ''):
        print("Não encontramos o evento para deletar ou algo de errado não deu certo.")
        exit()

    print(Deletar)
    exit()

print('https://programador.dev')