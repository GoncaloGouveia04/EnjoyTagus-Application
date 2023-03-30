#-*- coding: utf-8 -*-

# 2022-2023 Programação 2 (LTI)
# Grupo 11
# 60289 Gonçalo Gouveia
# 60287 Carolina Rodrigues

import constants

class readingFromFile:

    def __init__(self):
        self._skippersFile = ""
        self._scheduleFile = ""
        self._requestsFile = ""
    
    def setSkippersFile(self, fileName):

        self._skippersFile = fileName

    def getSkippersFile(self):

        inFile = open(self._skippersFile, "r")
        self._skippersList = []

        for line in inFile:
            skippersData = line.rstrip().split(", ")
            self._skippersList.append(skippersData)

        return self._skippersList[constants.NUM_HEADER_LINES:]
    
    def setScheduleFile(self, fileName):

        self._scheduleFile = fileName
    
    def getScheduleFile(self):

        inFile = open(self._scheduleFile, "r")
        self._scheduleList = []

        for line in inFile:
            scheduleData = line.rstrip().split(", ")   
            self._scheduleList.append(scheduleData)

        return self._scheduleList[constants.NUM_HEADER_LINES:]
    
    def setRequestsFile(self, fileName):
        
        self._requestsFile = fileName
    
    def getRequestsFile(self):
        
        inFile = open(self._requestsFile, "r")
        self._requestsList = []

        for line in inFile:
            requestsData = line.rstrip().split(", ")
            self._requestsList.append(requestsData)
        
        return self._requestsList[constants.NUM_HEADER_LINES:]