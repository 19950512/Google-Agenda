#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys, os, json
from datetime import datetime, timedelta

dir_path = os.path.dirname(os.path.realpath(__file__))
sys.path.append(os.path.abspath(dir_path + '/Modulos/'))

import Servico

class Listar(Servico):

    def __init__(self):
        super().__init__()

    def calendarios(self):

        calendars_result = self.servico().calendarList().list().execute()

        calendars = calendars_result.get('items', [])

        calendariosList = calendars

        if not calendars:
            return 'Ops, nenhum calendario encontrado.'

        return calendariosList

    def eventos(self, maxResults = 60):

        try:
            now = datetime.utcnow().isoformat() + 'Z' # 'Z' indicates UTC time
            events_result = self.servico().events().list(calendarId=self.calendarId, timeMin=now,
                                                maxResults=maxResults, singleEvents=True,
                                                orderBy='startTime').execute()
            events = events_result.get('items', [])

            if not events:
                return 'Ops, nenhum evento encontrado.'

            return events
        except Exception as msg:

            x, y = msg.args
            for i in x:
                if i == 'status' and x[i] == '404':
                    return 'Ops, não encontramos este calendario.'

            return 'Ops, algo de errado não deu certo. '

sys.modules[__name__] = Listar