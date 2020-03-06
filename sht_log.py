#--- Import Libraries
import os
import glob
import time
import datetime
from datetime import datetime
from datetime import date
from sht_sensor import Sht

filedate = date.today()

outfile='/data/sht/'+ str(filedate) + '-' + 'sht_rht.csv'


sht = Sht(21, 17)

with open(outfile,'a') as f:
    while True :
        f.write(datetime.utcnow().isoformat() + ',' + str(sht.read_t()) + '\n' ) #write the data to a string and to the output file
        print 'Temperature', sht.read_t()
        print 'Relative Humidity', sht.read_rh()
        time.sleep(2.4)
        f.flush()

