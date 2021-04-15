#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys, os

dir_path = os.path.dirname(os.path.realpath(__file__))
sys.path.append(os.path.abspath(dir_path + '/Modulos/'))

import Servico

class Deletar(Servico):

    def __init__(self):
        super().__init__()

    def codigo(self, eventId):

        try:
            self.servico().events().delete(
                calendarId=self.calendarId,
                eventId=eventId,
            ).execute()
        except googleapiclient.errors.HttpError:
            return "Ops, falha ao deletar o evento."
        
        return "Evento deletado."

sys.modules[__name__] = Deletar