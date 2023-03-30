#-*- coding: utf-8 -*-

# 2022-2023 Programação 2 (LTI)
# Grupo 11
# 60289 Gonçalo Gouveia
# 60287 Carolina Rodrigues

from readingFromFile import readingFromFile
from headerFiles import headerFiles
from skippers import skipper
from requests import request
import constants
from operator import itemgetter

class schedule(skipper, request):

    def __init__(self):
        super(readingFromFile).__init__()
        super(headerFiles).__init__()
        self._scheduledaystart = ""
        self._scheduletimestart = ""
        self._scheduleskippername = ""

    def setScheduleDayStart(self, schedule):

        self._scheduledaystart = schedule

    def getScheduleDayStart(self):

        return self._scheduledaystart
    
    def setScheduleTimeStart(self, schedule):

        self._scheduletimestart = schedule

    def getScheduleTimeStart(self):

        return self._scheduletimestart
    
    def setScheduleDuration(self, schedule):

        self._scheduleduration = schedule

    def getScheduleDuration(self):

        return self._scheduleduration
    
    def setScheduleSkipperName(self, schedule):

        self._scheduleskippername = schedule

    def getScheduleSkipperName(self):

        return self._scheduleskippername
    
    def setScheduleCruisePrice(self, schedule):

        self._schedulecruiseprice = schedule

    def getScheduleCruisePrice(self):

        return self._schedulecruiseprice
    
    def setScheduleClientName(self, schedule):

        self._scheduleclientname = schedule

    def getScheduleClientName(self):

        return self._scheduleclientname

    def updateSkippers(self, skippers, requests):

        listaskippers = []
        for request in requests:
            for skipper in skippers:
                self.setRequestLanguage\
                    (request[constants.REQUEST_LANGUAGE_IDX])
                
                self.setSkipperLanguage\
                    (skipper[constants.SKIPPER_LANGUAGE_IDX])
                
                # Compare the client and skipper language
                if any(self.getRequestLanguage()) == \
                    any(self.getSkipperLanguage()):

                    self.setRequestLevel\
                        (request[constants.REQUEST_LEVEL_IDX])
                    
                    self.setSkipperCard\
                        (skipper[constants.SKIPPER_CATEGORY_IDX])
                    
                    # if the skipper has a language that the client requires than
                    # we compare the client level (1*, 2*, 3*) and skipper card
                    # so we can move to the spcialization
                    if self.getRequestLevel() == self.getSkipperCard():

                        self.setRequestspeciality\
                            (request[constants.REQUEST_SPECIALITY_IDX])
                        
                        self.setSkipperSpecialization\
                            (skipper[constants.SKIPPER_SPECILIZATION_IDX])
                        
                        # Compare the specialization of each
                        # If they are the same we assign the skipper to the client and update
                        # The time that the skipper still has to do and the time the skipper has his/her last ride
                        if self.getRequestspeciality() == self.getSkipperSpecialization():
                            self.setRequestHours(request[constants.REQUEST_HOURS_IDX])

                            self.setSkipperTimeAccumulated\
                                (skipper[constants.SKIPPER_SOMTIME_IDX])
                            
                            time = int(self.getRequestHours()) + \
                                int(self.getSkipperTimeAccumulated())
                            skipper[constants.SKIPPER_SOMTIME_IDX] = str(time)
                            self.setSkipperTimeFinish\
                                (skipper[constants.SKIPPER_LASTIME_IDX])
                            self.setSkipperDayFinish\
                                (skipper[constants.SKIPPER_DATE_IDX])
                            lasttime = self.getSkipperTimeFinish().split(")")
                            lastdate = self.getSkipperDayFinish().split("(")
                            lasttime = lasttime[0].split(":")
                            lastdate = lastdate[1].split(":")
                            lasttime[0] = str(int(lasttime[0]) + int(self.getRequestHours()))
                            if int(lasttime[0]) >20 or \
                                int(lasttime[0]) >=20 and int(lasttime[1]) == 30:
                                lasttime[0] = str(8)
                                lasttime[0] = str(int(lasttime[0]) + \
                                                  int(self.getRequestHours()))
                                lastdate[0] = str(int(lastdate[0]) + 1)
                                if int(lastdate[0]) > 30:
                                    lastdate[0] = str(1)
                                    lastdate[1] = str(int(lastdate[1]) + 1)
                                    if int(lastdate[1]) > 12:
                                        lastdate[1] = str(0) + str(1)
                                        lastdate[2] = str(int(lastdate[2]) + 1)
                            
                            if int(lastdate[0]) < 10:

                                lastdate[0] = "0" + str(int(lastdate[0]))
                            
                            if int(lastdate[1]) < 10:

                                lastdate[1] = "0" + str(int(lastdate[1]))
                            
                            self.setSkipperTime(skipper[constants.SKIPPER_WREST_IDX])
                            # If the time the skipper has to do doesnt surpass the time it holds without
                            # resting for 2 days, we assign the client to the skipper
                            # if not the client has the status not-assign
                            if int(time) <= int(self.getSkipperTime()):
                                lasttime = str(":".join(lasttime))
                                lastdate = str(":".join(lastdate))
                                lasttime = lasttime + ")"
                                lastdate = "(" + lastdate
                                skipper[constants.SKIPPER_LASTIME_IDX] = lasttime 
                                skipper[constants.SKIPPER_DATE_IDX] = lastdate
                                listaskippers.append(skipper)

        return sorted(listaskippers, key=itemgetter(0))

    def updateSchedule(self, skippers, requests, schedules):

        listaschedules = []
        for request in requests:
            for skipper in skippers:
                self.setRequestLanguage\
                    (request[constants.REQUEST_LANGUAGE_IDX])
                self.setSkipperLanguage\
                    (skipper[constants.SKIPPER_LANGUAGE_IDX])
                if any(self.getRequestLanguage()) == \
                    any(self.getSkipperLanguage()):
                    self.setRequestLevel\
                        (request[constants.REQUEST_LEVEL_IDX])
                    self.setSkipperCard\
                        (skipper[constants.SKIPPER_CATEGORY_IDX])
                    if self.getRequestLevel() == \
                        self.getSkipperCard():
                        self.setRequestspeciality\
                            (request[constants.REQUEST_SPECIALITY_IDX])
                        self.setSkipperSpecialization\
                            (skipper[constants.SKIPPER_SPECILIZATION_IDX])
                        if self.getRequestspeciality() ==\
                              self.getSkipperSpecialization():
                            self.setRequestHours\
                                (request[constants.REQUEST_HOURS_IDX])
                            self.setSkipperDayFinish\
                                (skipper[constants.SKIPPER_DATE_IDX])
                            self.setSkipperTimeFinish\
                                (skipper[constants.SKIPPER_LASTIME_IDX])
                            self.setRequestHours\
                                (request[constants.REQUEST_HOURS_IDX])
                            self.setSkipperPrice\
                                (skipper[constants.SKIPPER_COST_IDX])
                            listaschedule = []
                            listaschedule.append\
                                (self.getSkipperDayFinish().split("(")[1])
                            listaschedule.append\
                                (self.getSkipperTimeFinish().split(")")[0])
                            listaschedule.append\
                                (self.getRequestHours())
                            listaschedule.append\
                                (skipper[constants.SKIPPER_NAME_IDX])
                            listaschedule.append\
                                (str(int(self.getSkipperPrice()) * int(self.getRequestHours())))
                            listaschedule.append\
                                (request[constants.CLIENT_NAME_IDX])
                            listaschedules.append\
                                (listaschedule)
                        
                        else:
                            # If none of the requirements are met, 
                            # add the not-assigned to the client in the schedule file
                            self.setScheduleHeader(schedules)
                            listaschedule = []
                            date = ""
                            date = (date.join\
                                    (self.getScheduleHeader()[constants.NUM_HEADER_DATE]))
                            listaschedule.append(date)
                            listaschedule.append("not-assigned")
                            listaschedule.append(request[constants.CLIENT_NAME_IDX])
                            listaschedules.append(listaschedule)

        return sorted(listaschedules, key=itemgetter(0,1))