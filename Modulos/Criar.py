#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys, os, json
from datetime import datetime, timedelta

dir_path = os.path.dirname(os.path.realpath(__file__))
sys.path.append(os.path.abspath(dir_path + '/Modulos/'))

import Servico

class Criar(Servico):

    def __init__(self):
        super().__init__()

    def go(self, body = {}):

        data = json.loads(body)

        # Valida inicialmente o BODY
        resposta = self.validation(data)

        # Se houver algum erro
        if(resposta != True):
            return resposta


        data_inicio = datetime.strptime(data[0]['inicio'], '%Y-%m-%d %H:%M:%S')
        data_fim = datetime.strptime(data[0]['fim'], '%Y-%m-%d %H:%M:%S')

        start = data_inicio.isoformat()
        end = data_fim.isoformat()
        
        body = { 
            "summary": data[0]['titulo'], 
            "description": data[0]['descricao'],
            "start": {"dateTime": start, "timeZone": 'America/Sao_Paulo'}, 
            "end": {"dateTime": end, "timeZone": 'America/Sao_Paulo'},
        }

        event_result = self.servico().events().insert(calendarId=self.calendarId, body=body).execute()

        return {
            "id": event_result['id'],
            "summary": event_result['summary'],
            "starts at": event_result['start']['dateTime'],
            "ends at": event_result['end']['dateTime'],
        }

    def validation(self, data):
        
        # Atravessa o BODY
        for param in data:

            # YYYY-MM-DD HH:ii:ss (2021-04-16 10:00:00)
            if 'inicio' not in param:
                return 'Ops, precisa informar qual é a Data/Hora Início do Evento (YYYY-MM-DD HH:MM:SS)'

            if 'fim' not in param:
                return 'Ops, precisa informar qual é a Data/Hora Fim do Evento (YYYY-MM-DD HH:MM:SS)'

        return True

sys.modules[__name__] = Criar