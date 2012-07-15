#!/usr/local/bin/python3
"""convert gregorial calendar date to julian.
Following the formula given here: http://quasar.as.utexas.edu/BillInfo/JulianDatesG.html.
Next to do is turn it into a Google date range search."""

from time import gmtime, strftime

def julianify(date):
    """given a date 'n' in 8-digit format, parse and convert to julian"""
    d = n[0:2]
    m = n[2:4]
    Y = n[4:8]
    a = int(Y)/100
    b = a/4
    c = 2-a+b
    e = 365.25*(int(Y)+4716)
    f = 30.6001*(int(m)+1)
    return (c+int(d)+e+f-1524.5)

while True:
    n = input("Type the date (in DDMMYYYY format) or enter for today: ")
    if not n:
        n = strftime("%d%m%Y")
    print("The Julian Calendar date is", julianify(n))
    break