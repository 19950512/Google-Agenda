#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys, os, os.path, pickle
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request

class Servico:

    def __init__(self):
        
        self.dir_path = os.path.dirname(os.path.realpath(__file__)).replace('/Modulos', '')

        # If modifying these scopes, delete the file token.pickle.
        self.SCOPES = ['https://www.googleapis.com/auth/calendar']
        self.CREDENTIALS_FILE = self.dir_path + '/credentials.json'

        self.calendarId = 'primary'

    def servico(self):
        creds = None
        # The file token.pickle stores the user's access and refresh tokens, and is
        # created automatically when the authorization flow completes for the first
        # time.

        if os.path.exists(self.dir_path + '/token.pickle'):
            with open(self.dir_path + '/token.pickle', 'rb') as token:
                creds = pickle.load(token)
        # If there are no (valid) credentials available, let the user log in.
        if not creds or not creds.valid:
            if creds and creds.expired and creds.refresh_token:
                creds.refresh(Request())
            else:
                flow = InstalledAppFlow.from_client_secrets_file(
                    self.CREDENTIALS_FILE, self.SCOPES)
                creds = flow.run_local_server(port=8080)
            # Save the credentials for the next run
            with open(self.dir_path + '/token.pickle', 'wb') as token:
                pickle.dump(creds, token)

        service = build('calendar', 'v3', credentials=creds)
        return service


sys.modules[__name__] = Servico