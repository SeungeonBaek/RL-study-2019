# -*- coding: utf-8 -*-
"""
Created on Sat Jan 20 11:24:58 2018

@author: Seungeon
"""

def isLeapYear(y):
    if (y%4 ==0)and(y%100==0)and(y%400==0):
        return True
    return False

def daysInmonth(y,m):
    if isLeapYear(y):
        Day=(31,29,31,30,31,30,31,31,30,31,30,31)
    else :
        Day=(31,28,31,30,31,30,31,31,30,31,30,31)
    
    days = Day[m-1]
    return days

def days_between_dates(y1, m1, d1, y2, m2, d2):
    days=0
    if y1<y2 :
        for i in range(y2-y1-1):
            for j in range(12):
                days+=daysInmonth(y1+i+1,j+1)
             
        for k in range(12-m1):
            days+=daysInmonth(y1,m1+1+k)        
           
        for l in range(m2-1):
            days+=daysInmonth(y2,l+1)

        days = days+daysInmonth(y1,m1)-d1+d2
    elif y1==y2:
        if m1<m2: # 2 7
            for i in range(m2-m1-1):
                days+=daysInmonth(y1,(m1+i+1))
             
        elif m1==m2:
            return d2-d1
        
        days = days+daysInmonth(y1,m1)-d1+d2               
    else:    
        return 0
    
    
    
    return days

   
def test_days_between_dates():
    
    # test same day
    assert(days_between_dates(2017, 12, 30,
                              2017, 12, 30) == 0)
    # test adjacent days
    assert(days_between_dates(2017, 12, 30, 
                              2017, 12, 31) == 1)
    # test new year
    assert(days_between_dates(2017, 12, 30, 
                              2018, 1,  1)  == 2)
    # test full year difference
    
    assert(days_between_dates(2012, 6, 29,
                              2013, 6, 29)  == 365)
    
    print("Congratulations! Your days_between_dates")
    print("function is working correctly!")
    
test_days_between_dates()