import glob
import serial


import matplotlib as mpl
mpl.use('Agg')
from matplotlib import pyplot as plt

plt.savefig('test.png')


ports = glob.glob('/dev/tty[A-Za-z]*')

for port in ports:
    last_hour = []
    last_minute = []

    with serial.Serial(port, 9600) as ser:
        print(ser)

        for line in ser:
            temp, hum = line.strip().decode('utf-8').split(',')
            temp, hum = float(temp), int(hum)
    
            print('{}°f'.format(temp * 9 / 5 + 32), hum)
