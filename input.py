#!/usr/bin/env python
import os
import time
import automationhat
import time
import datetime
from datetime import datetime
from datetime import date

filedate = date.today()

outfile='/data/battery/'+ str(filedate) + '-' + 'battery_voltage.csv'




if automationhat.is_automation_hat():
    automationhat.light.power.write(1)
with open(outfile,'a') as f:
    while True:
    
        
        print(automationhat.input.read())
        print(automationhat.analog.read())
        time.sleep(0.5)
