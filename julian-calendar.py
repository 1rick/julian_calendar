#!/usr/local/bin/python3
"""convert gregorial calendar date to julian.
Following the formula given here: http://quasar.as.utexas.edu/BillInfo/JulianDatesG.html.
Next to do is turn it into a Google date range search."""

y = input("Type the year: ")
m = input("Type the month: ")
d = input("Type the numeric day of the month: ")

a = int(y)/100
b = a/4
c = 2-a+b
e = 365.25*(int(y)+4716)
f = 30.6001*(int(m)+1)
juliandate = c+int(d)+e+f-1524.5

print("The Julian Calendar date is", juliandate)