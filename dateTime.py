#-*- coding: utf-8 -*-

# 2022-2023 Programação 2 (LTI)
# Grupo 11
# 60289 Gonçalo Gouveia
# 60287 Carolina Rodrigues

def hourToInt(time):
    """
    Hours to integer
    """
    t = time.split(":")
    return int(t[0])

def minutesToInt(time):
    """
    Minutes to integer
    """
    pass #TODO
    t = time.split(":")
    return int(t[1])
    
def intToTime(hour, minutes):
    """
    Hours and minutes to time
    """
    h = str(hour)
    m = str(minutes)

    if hour < 10:
        h = "0" + h

    if minutes < 10:
        m = "0" + m

    return h + ":" + m