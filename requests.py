#-*- coding: utf-8 -*-

# 2022-2023 Programação 2 (LTI)
# Grupo 11
# 60289 Gonçalo Gouveia
# 60287 Carolina Rodrigues


from readingFromFile import readingFromFile
from headerFiles import headerFiles

class request():

    def __init__(self):
        super(readingFromFile).__init__()
        super(headerFiles).__init__()
        self._requestclientname = ""
        self._requestlanguage = ""
        self._requestlevel = ""
        self._requestspeciality = ""
        self._requesthours = ""
    
    def setRequestClientName(self, request):

        self._requestclientname = request
    
    def getRequestClientName(self):

        return self._requestclientname

    def setRequestLanguage(self, request):

        self._requestlanguage = request.split(';')

    def getRequestLanguage(self):    
        
        return self._requestlanguage
    
    def setRequestLevel(self, request):

        self._requestlevel = request

    def getRequestLevel(self):

        return self._requestlevel

    def setRequestspeciality(self, request):

        self._requestspeciality = request

    def getRequestspeciality(self):

        return self._requestspeciality
    
    def setRequestHours(self, request):

        self._requesthours = request
    
    def getRequestHours(self):

        return self._requesthours