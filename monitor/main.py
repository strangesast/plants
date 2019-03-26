import glob
import serial
import time
import matplotlib as mpl
import numpy as np
mpl.use('Agg')
from matplotlib import pyplot as plt
import subprocess


def plot(gen):
    last = []
    lasttime = -1
    
    fig, ax1 = plt.subplots()
    
    color = 'tab:red'
    ax1.set_xlabel('time (s)')
    ax1.set_ylabel('temperature', color=color)
    
    line1, = ax1.plot(np.arange(0, 10), np.arange(0, 10), color=color)
    
    ax1.tick_params(axis='y', labelcolor=color)
    
    ax2 = ax1.twinx()
    color = 'tab:blue'
    ax2.set_ylabel('humidity', color=color)
    line2, = ax2.plot(np.arange(0, 10), np.arange(10, 0, -1), color=color)
    ax2.tick_params(axis='y', labelcolor=color)
    
    
    for temp, hum in gen:
        thistime = int(time.time())
    
        last.append((thistime, (temp, hum)))
    
        last = last[-600:]
    
        if thistime > lasttime + 60 or len(last) < 10:
            times, data = zip(*last)
            a = [d[0] for d in data]
            b = [d[1] for d in data]
    
            line1.set_ydata(a)
            line1.set_xdata(times)
            ax1.relim()
            ax1.autoscale_view()
    
            line2.set_ydata(b)
            line2.set_xdata(times)
            ax2.relim()
            ax2.autoscale_view()
            fig.tight_layout()
    
            plt.savefig('lastframe.png')
            lasttime = thistime

            yield 'lastframe.png'


plt.savefig('test.png')

ports = glob.glob('/dev/tty[A-Za-z]*')


def read_port(port):
    for line in port:
        temp, hum = line.strip().decode('utf-8').split(',')
        temp, hum = float(temp), int(hum)
        yield temp, hum


for address in ports:
    with serial.Serial(address, 9600) as ser:
        for picname in plot(read_port(ser)):
            subprocess.call(['fbi', '-T', '1', '-a', '-d', '/dev/fb0', picname])
