#!/usr/bin/env python3
#Created by Yudan for BCH 5884 Final Project
#Github link: https://github.com/Jak1022/FSU-BCH5884-Fall2020/tree/master/Final

from matplotlib import pyplot as plt
import numpy as np
import sys,math
from scipy.signal import argrelextrema

from optparse import OptionParser
parser=OptionParser()
parser.add_option('--input', dest='input', default='data.txt', help = "Input file")

# parsing function #

def read_data(filename):
    with open(filename) as fp:
        lines = fp.readlines()
        # initialize empty list to save Freq, Zreal, Zimag
        Freq_lst = []
        Zreal_lst = []
        Zimag_lst = []
        # read lines from file and discard the first two line
        for line in lines[2:]:
            # split each line and convert str to float
            con = line.split()
            cons = [float(a) for a in con]
            Freq_lst.append(cons[2])
            Zreal_lst.append(cons[3])
            Zimag_lst.append(cons[4])
        return np.array(Freq_lst), np.array(Zreal_lst), np.array(Zimag_lst)

def find_local_min(y):
    index_lst = argrelextrema(y, np.less)
    return index_lst[0]

# plotting functions #
## plot 1 - nyquist plot ##
def plot_zimag(zreal, zimag):
    """
    plot fig1
    """
    y = -zimag
    x = zreal
    fig = plt.figure()
    ax = fig.add_subplot(111)

    plt.scatter(x,y,c = "r")
    plt.xlabel("Zreal (ohm)")
    plt.ylabel("Zimag (ohm)")
    # find local min
    index_lst =  find_local_min(np.round(y,2))
    # scatter local min
    plt.scatter( x[index_lst], y[index_lst] , c = "b", marker="*", s = 150 )
    # add comment to figure
    i = 0
    for vx, vy in zip( x[index_lst], y[index_lst] ):
        ax.text(0.1, 0.1 + 0.1 * i, "V{}: ({}, {})".format(i, vx, vy), transform=ax.transAxes)
        i += 1
    plt.savefig("./zimag.png")

## plot 2 - conductivity plot ##
def plot_acsigma(freq, zreal):
    """
    plot fig2
    """
    plt.figure()
    y = 0.1 / (0.18 * zreal)
    x = freq * math.pi * 2 /(1e7)
    plt.ylim(min(y) - 0.00002, 0.0013)
    plt.plot(x,y,'mo')
    plt.xlabel("Angular Frequency (*1e7) (Hz)")
    plt.ylabel("AC Conductivity (mS/cm)")
    plt.savefig("./acsigma.png")

# html functions #

def openHTML(f,title):
	f.write("<!DOCTYPE html>")
	f.write("<head>\n")
	f.write("<h1>%s</h1>\n" % title)
	f.write("</head>\n")
	f.write("<body>\n")

def writeHTMLImage(f, title, imgpath):
	f.write('<p class="aucimage">%s</p>\n' % title)
	f.write('<img src="%s" />\n' % imgpath)

def closeHTML(f):
	f.write("</body>\n")
	f.write("</html>\n")
	f.close()

def create_html(html_filename, html_title, title1, title2, fig1_path, fig2_path):
    with open(html_filename,"w+") as fp:
        openHTML(fp, html_title)
        writeHTMLImage(fp, title1, fig1_path)
        writeHTMLImage(fp, title2, fig2_path)
        closeHTML(fp)

if __name__ == '__main__':
	# Parse the file
    options, args = parser.parse_args()
    if len(sys.argv) != 2:
        print("---Usage: <eisprogram.py> <datafile.txt>---")
        print("---I'll do the analysis and make plots in an html file.---")
        sys.exit()
    filename = sys.argv[1]
    Freq_lst, Zreal_lst, Zimag_lst = read_data(filename)
    print("Done!")
    print("You can find the web.html in the same directory as <program.py> and <data.txt>.")
    
    # Make plots from data from our analysis
    ## Plot 1 - Nyquist plot
    plot_zimag(Zreal_lst, Zimag_lst)
    ## Plot 2 - angular frequency vs. ac_conductivity
    plot_acsigma(Freq_lst, Zreal_lst)
	
	# Create an html file that contains our results and plots
    html_title = "Data Analysis Results"
    title1 = "Nyquist Plot"
    title2 = "Plot (AC Conductivity vs. Angular Frequency)"
    fig1_path = "./zimag.png"
    fig2_path = "./acsigma.png"
    create_html("web.html",html_title, title1, title2, fig1_path, fig2_path)
