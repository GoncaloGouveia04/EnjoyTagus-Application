# -*- coding: utf-8 -*-

# 2022-2023 Programação 2 (LTI)
# Grupo 11
# 60289 Gonçalo Gouveia
# 60287 Carolina Rodrigues

import sys
import dateDay
import dateTime
import constants
from writingToFiles import writeFile
import dateTime
import dateDay


class update(writeFile):

    def __init__(self):
        super(writeFile).__init__()

    def assign(self, skippersFileName, scheduleFileName, requestsFileName):
        """
        Creates two text files with skippers and schedules updated

        Requires: skippersFileName being a string with the name of 
                 the skipper file, scheduleFileName being a string
                 with the name of the schedule file and requestsFileName 
                 being the name of the request file
        Ensures: Two text files with skippers and schedules each, with the time and date updated
        """

        try:
            # Variables to save the dates and times of the skippers
            # and schedules files
            timeSkipper = ""
            timeSchedule = ""
            dateSkipper = ""
            dateSchedule = ""

            # Set the headers to update the time and date of each file
            self.setSkippersHeader(skippersFileName)
            self.setScheduleHeader(scheduleFileName)

            # Create variables to compare with the text file name
            # to see if the names (skippers and schedules) are the same inside the text file
            name = "".join(self.getSkippersHeader()[constants.NUM_HEADER_FILETYPE])
            name2 = "".join(self.getScheduleHeader()[constants.NUM_HEADER_FILETYPE])
            name = name.split(":")
            name2 = name2.split(":")

            # Create variables to compare with the text file time
            # to see if the times of the files name are the same inside the text file
            time = "".join(self.getSkippersHeader()[constants.NUM_HEADER_TIME])
            time2 = "".join(self.getScheduleHeader()[constants.NUM_HEADER_TIME])

            if skippersFileName[9].upper() + skippersFileName[10:17] != name[0]:
                return "Input file error: scope or time inconsistency between name and header in file " + skippersFileName
            elif scheduleFileName[9].upper() + scheduleFileName[10:17] != name2[0]:
                return "Input file error: scope or time inconsistency between name and header in file " + scheduleFileName
            elif skippersFileName[17:19] + ":" + skippersFileName[20:22] != time:
                return "Input file error: scope or time inconsistency between name and header in file " + skippersFileName
            elif scheduleFileName[17:19] + ":" + scheduleFileName[20:22] != time2:
                return "Input file error: scope or time inconsistency between name and header in file " + scheduleFileName
            
            else:

                # Associate each previous date and time of each files to the variables
                timeSkipper = (timeSkipper.join(self.getSkippersHeader()
                                            [constants.NUM_HEADER_TIME]))
                timeSchedule = (timeSchedule.join(self.getScheduleHeader()
                                              [constants.NUM_HEADER_TIME]))
                dateSkipper = (dateSkipper.join(self.getSkippersHeader()
                                            [constants.NUM_HEADER_DATE]))
                dateSchedule = (dateSchedule.join(self.getScheduleHeader()
                                              [constants.NUM_HEADER_DATE]))

                # Create variables daySkipper and daySchedule
                # for the previous day of each file
                daySkipper = dateDay.dayToInt(dateSkipper)
                daySchedule = dateDay.dayToInt(dateSchedule)

                # Create variables monthSkipper and montheSchedule
                # for the previous month of each file
                monthSkipper = dateDay.monthToInt(dateSkipper)
                monthSchedule = dateDay.monthToInt(dateSchedule)

                # Create variables yearSkipper and yearSchedule
                # for the previous year of each file
                yearSkipper = dateDay.yearToInt(dateSkipper)
                yearSchedule = dateDay.yearToInt(dateSchedule)

                # Create variables hoursSkipper and hoursSchedule
                # for the previous hour of each file
                hourSkipper = dateTime.hourToInt(timeSkipper)
                hourSchedule = dateTime.hourToInt(timeSchedule)

                # Create variables minuteSkipper and minuteSchedule
                # for the previous minute of each file
                minuteSkipper = dateTime.minutesToInt(timeSkipper)
                minuteSchedule = dateTime.minutesToInt(timeSchedule)

                # Update minuteSkipper and minuteSchedule by
                # adding 30 minutes to each variable
                minuteSkipper += 30
                minuteSchedule += 30

                # Check if each variables that contain the minutes are
                # equal to 60, if yes set them to 0 and add 1 to
                # the variables hourSkipper and hourSchedule
                if minuteSkipper == 60 and minuteSchedule == 60:
                    minuteSkipper = 00
                    minuteSchedule = 00
                    hourSkipper += 1
                    hourSchedule += 1

                # Check if the hour is equal to 20 and the minutes are equal to 30
                # if so then reset the hours to 8
                # and minutes to 0 and add 1 to the variables daySkipper and daySchedule
                if hourSkipper >= 20 and minuteSkipper == 30 and \
                        hourSchedule >= 20 and minuteSchedule == 30:
                    hourSkipper = 8
                    hourSchedule = 8
                    minuteSkipper = 00
                    minuteSchedule = 00
                    daySkipper = daySkipper + 1
                    daySchedule += 1

                    # Check if the variables daySkipper
                    # and daySchedule are
                    # higher than 30, if so then reset them to 1
                    # and add 1 to monthSkipper and monthSchedule
                    if daySkipper > 30 and daySchedule > 30:
                        daySkipper = 1
                        daySchedule = 1
                        monthSkipper += 1
                        monthSchedule += 1

                    # Check if the variables monthSkipper
                    # and monthSchedule are
                    # higher than 12, if so then reset them to 1
                    # and add 1 to yearSkipper and yearSchedule
                    if monthSkipper > 12 and monthSchedule > 12:
                        monthSkipper = 1
                        monthSchedule = 1
                        yearSkipper += 1
                        yearSchedule += 1

                # Assign the updated skipper time and schedule time
                # to new variables into the form of xx:xx
                updatedTimeSkipper = dateTime.intToTime(hourSkipper, minuteSkipper)
                updatedTimeSchedule = dateTime.intToTime(hourSchedule, minuteSchedule)

                # Assign the updated skipper date and schedule date
                # to new variables into the form of xx:xx:xxxx
                updatedDateSkipper = dateDay.intToDate(
                    daySkipper, monthSkipper, yearSkipper)
                updatedDateSchedule = dateDay.intToDate(
                    daySchedule, monthSchedule, yearSchedule)

                # Split the skipper and schedule time to
                # add into the names of the text files
                tSkipper = updatedTimeSkipper.split(":")
                tSchedule = updatedTimeSchedule.split(":")

                # Assign the previous variables to
                # the updated hours and minutes
                hourSkipper = tSkipper[0]
                hourSchedule = tSchedule[0]
                minuteSkipper = tSkipper[1]
                minuteSchedule = tSchedule[1]

                # Create the updated skippers and schedules file with the updated time into each one
                skippersFile = open("skippers" +
                            hourSkipper + "h" + minuteSkipper + ".txt", "w+")
                schedulefile = open("schedule" +
                            hourSchedule + "h" + minuteSchedule + ".txt", "w+")

                # Create the list of lists for each type of file (skipper, schedule and request)
                self.setSkippersFile(skippersFileName)
                self.setScheduleFile(scheduleFileName)
                self.setRequestsFile(requestsFileName)

                # Assign the variables skipper, schedule and request into each list of lists
                skipper = self.getSkippersFile()
                request = self.getRequestsFile()
                schedules = self.getScheduleFile()

                # Update the skippers list of lists
                skippers = self.updateSkippers(skipper,
                                       request)
                schedules = self.updateSchedule(skipper,
                                        request, scheduleFileName)

                # Create the skippers header
                # and schedule header
                self.setSkippersHeader(skippersFileName)
                self.setScheduleHeader(scheduleFileName)

                # Assign the variables headerSkipper
                # and headerSchedule into each header
                headerSkipper = self.getSkippersHeader()
                headerSchedule = self.getScheduleHeader()

                # Update the time and date of each header (skipper and header)
                headerSkipper[constants.NUM_HEADER_TIME] = updatedTimeSkipper
                headerSkipper[constants.NUM_HEADER_DATE] = updatedDateSkipper
                headerSchedule[constants.NUM_HEADER_TIME] = updatedTimeSchedule
                headerSchedule[constants.NUM_HEADER_DATE] = updatedDateSchedule

                # Write the updated versions of the skippers
                # and schedule into the text files and finish the program
                self.writeSkipperFile(skippers, headerSkipper, skippersFile)
                self.writeScheduleFile(schedules, headerSchedule, schedulefile)

                return "Done!\n" +\
                    "Created files: skippers" + hourSkipper + "h" \
                    + minuteSkipper + ".txt and schedule" + \
                    hourSchedule + "h" + minuteSchedule + ".txt"
        
        except FileNotFoundError:
            return "A file in the arguments doesnt exist"



inFile1 = str(sys.argv[1])
inFile2 = str(sys.argv[2])
inFile3 = str(sys.argv[3])

u = update()
print(u.assign(inFile1, inFile2, inFile3))
