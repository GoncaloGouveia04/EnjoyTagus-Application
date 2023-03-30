#-*- coding: utf-8 -*-

# 2022-2023 Programação 2 (LTI)
# Grupo 11
# 60289 Gonçalo Gouveia
# 60287 Carolina Rodrigues

from schedule import schedule

class writeFile(schedule):

    def __init__(self):

        super(schedule).__init__()

    def writeSkipperFile(self, skipper, header, fileName):
        '''
        Write the updated version of the skipper file into a new text file

        Requires: skipper being a list of lists with skippers, 
                 header being a list of lists of the skipper header 
                 and fileName being the file to write the header
                 and updated version of the skippers
        Ensures: Done! when all is written into the new text file
        '''
        headerS = list(map("".join, header))
        skippersS = list(map(", ".join, skipper))
        for item in headerS:
            fileName.write(item)
            fileName.write("\n")
        for item in skippersS:
            fileName.write(item)
            fileName.write("\n")

        return "Done!"
    
    def writeScheduleFile(self, schedule, header, fileName):
        """
        Write the updated version of the schedule file into a new text file

        Requires: schedule is a list of lists with schedules, 
                  header being a list of lists of the schedule header
                 and fileName being the file to write the header 
                 and updated version of the schedules
        Ensures: Done! when all is written into the new text file
        """
        headerS = list(map("".join, header))
        scheduleS = list(map(", ".join, schedule))
        for item in headerS:
            fileName.write(item)
            fileName.write("\n")
        for item in scheduleS:
            fileName.write(item)
            fileName.write("\n")

        return "Done"