#-*- coding: utf-8 -*-

# 2022-2023 Programação 2 (LTI)
# Grupo 11
# 60289 Gonçalo Gouveia
# 60287 Carolina Rodrigues

import constants
import dateDay

class headerFiles:

    def __init__(self):
        self._skipperHeader = ""
        self._scheduleHeader = ""
        self._requestHeader = ""

    def setSkippersHeader(self, fileName):
        """
        Associates self._skipperHeader 
        to the name of the skipper file
        """

        self._skipperHeader = fileName
    
    def getSkippersHeader(self):
        """
        Reads the self._skipperHeader 
        wich is a text file with the skipper list, 
        and returns a list of list with the header only
        """

        inFile = open(self._skipperHeader, "r")
        self._skipperHeaderList = []

        for line in inFile:
            skipperHeaderData = line.rstrip().split(", ")
            self._skipperHeaderList.append(skipperHeaderData)

        return self._skipperHeaderList[:constants.NUM_HEADER_LINES]

    def setScheduleHeader(self, fileName):
        """
        Associates the self._scheduleHeader 
        to the name of the schedule file
        """

        self._scheduleHeader = fileName
    
    def getScheduleHeader(self):
        """
        
        """

        inFile = open(self._scheduleHeader, "r")
        self._scheduleHeaderList = []

        for line in inFile:
            scheduleHeaderData = line.rstrip().split(", ")
            self._scheduleHeaderList.append(scheduleHeaderData)

        return self._scheduleHeaderList[:constants.NUM_HEADER_LINES]
    
    def setRequestHeader(self, fileName):

        self._requestHeader = fileName
    
    def getRequestHeader(self):

        inFile = open(self._requestHeader, "r")
        self._requestHeaderList = []

        for line in inFile:
            requestHeaderData = line.rstrip().split(", ")
            self._requestHeaderList.append(requestHeaderData)

        return self._requestHeaderList[:constants.NUM_HEADER_LINES]
    
    def __eq__(self, otherFile):
        
        if self._requestHeader == "" and self._scheduleHeader == "":

            return self.getSkippersHeader() == otherFile.getSkippersHeader()
        
        elif self._skipperHeader == "" and self._scheduleHeader == "":

            return self.getRequestHeader() == otherFile.getRequestHeader()
        
        else:
            return self.getScheduleHeader() == otherFile.getScheduleHeader()