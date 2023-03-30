#-*- coding: utf-8 -*-

# 2022-2023 Programação 2 (LTI)
# Grupo 11
# 60289 Gonçalo Gouveia
# 60287 Carolina Rodrigues

from readingFromFile import readingFromFile
from headerFiles import headerFiles

class skipper(readingFromFile, headerFiles):

    def __init__(self):
        super(readingFromFile).__init__()
        super(headerFiles).__init__()
        self._skipperlanguage = ""
        self._skippercard = ""
        self._skipperprice = ""
        self._specialization = ""
        self._skippertime = ""
        self._skippertimeacc = ""
        self._skipperdayinish = ""
        self._skippertimefinish = ""
    
    def setSkipperLanguage(self, skipper):

        self._skipperlanguage = skipper.split(';')
    
    def getSkipperLanguage(self):

        return self._skipperlanguage
    
    def setSkipperCard(self, skipper):

        self._skippercard = skipper
    
    def getSkipperCard(self):

        return self._skippercard
    
    def setSkipperPrice(self, skipper):

        self._skipperprice = skipper
    
    def getSkipperPrice(self):

        return self._skipperprice
    
    def setSkipperSpecialization(self, skipper):

        self._specialization = skipper

    def getSkipperSpecialization(self):

        return self._specialization
    
    def setSkipperTime(self, skipper):

        self._skippertime = skipper

    def getSkipperTime(self):

        return self._skippertime
    
    def setSkipperTimeAccumulated(self, skipper):

        self._skippertimeacc = skipper

    def getSkipperTimeAccumulated(self):

        return self._skippertimeacc
    
    def setSkipperDayFinish(self, skipper):

        self._skipperdayfinish = skipper

    def getSkipperDayFinish(self):

        return self._skipperdayfinish
    
    def setSkipperTimeFinish(self, skipper):

        self._skippertimefinish = skipper
    
    def getSkipperTimeFinish(self):

        return self._skippertimefinish