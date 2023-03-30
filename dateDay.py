#-*- coding: utf-8 -*-

# 2022-2023 Programação 2 (LTI)
# Grupo 11
# 60289 Gonçalo Gouveia
# 60287 Carolina Rodrigues

def dayToInt(date):
    """
    Day to integer
    """
    d = date.split(":")
    return int(d[0])

def monthToInt(date):
    """
    Month to integer
    """
    d = date.split(":")
    return int(d[1])

def yearToInt(date):
    """
    Year to integer
    """
    d = date.split(":")
    return int(d[2])

def intToDate(day, month, year):
    """
    Day, month and year to date
    """
    d = str(day)
    m = str(month)
    y = str(year)

    if day < 10:
        d = "0" + d
    
    if month < 10:
        m + "0" + m
    
    return d + ":" + m + ":" + y