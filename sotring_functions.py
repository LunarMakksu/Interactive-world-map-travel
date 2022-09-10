
def country_fetch():
    with open ("places.csv", 'r') as c:
        csv_r=csv.reader(c)
        next(csv_r)
        for row in c:
            global Countries
            Countries = row[0]

def place_fetch():
    with open ("places.csv", 'r') as c:
        csv_r=csv.reader(c)
        next(csv_r)
    for row in c:
        global places
        places = row[1]

def lat_fetch():
    with open ("places.csv", 'r') as c:
        csv_r=csv.reader(c)
        next(csv_r)
        for row in c:
            global latt
            latt = row[2]

def long_fetch():
    with open ("places.csv", 'r') as c:
        csv_r=csv.reader(c)
        next(csv_r)
        for row in c:
            global long
            long = row[3]

def visited():
    