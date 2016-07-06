#Convert to 4 columns for calculating likelihood
from math import *
import glob
import numpy as np
from optparse import OptionParser

parser = OptionParser()

parser.add_option('-i', metavar = 'N', type = 'string', action = 'store', default = '', dest = 'i', help='input filename')

parser.add_option('-o', metavar = 'N', type = 'string', action = 'store', default = '', dest = 'o', help='output filename')

(options, args) = parser.parse_args()

def writecls(f, l, spectrum):
	if spectrum == 'TT':
		index = 1
	elif spectrum == 'TE':
		index = 3
	elif spectrum == 'EE':
		index = 2
	elif spectrum == 'dd':
		index = 4

	print(len(l))
	#for i in range(len(l)):
	for i in range(0,2047):
		
		if(index == 5):
			f.write(str(l[i][index]) + '\n')
		else:
			f.write(str(2.*3.14159*l[i][index]/(l[i][0]*(l[i][0] + 1.))) + '\n')

def likformat(filename, number):
	f = open(filename, 'r')
	#outf = open('TElikcls_hil/' + filename[filename.rfind('/')+1:filename.rfind('.')] + '_likcls.txt', 'w')
	outf = open('lensingcamb.txt', 'a')
	lines = f.readlines()
	for i in range(len(lines)):
		lines[i] = lines[i].strip().split()[:9]
		
		#camb
		lines[i] = [float(lines[i][0]), float(lines[i][1]), float(lines[i][2]), float(lines[i][4]), float(lines[i][5])]
		#class
		#lines[i] = [float(lines[i][0]), float(lines[i][1]), float(lines[i][2]), float(lines[i][3]), float(lines[i][5])]

	if (number == 1):
		outf.write('0\n0\n')
		writecls(outf, lines, 'dd')	
	else:
		outf.write('0\n0\n')
		writecls(outf, lines, 'TT')
		outf.write('0\n0\n')
		writecls(outf, lines, 'EE')
		outf.write('0\n0\n')
		writecls(outf, lines, 'TE')
		
		outf.write("0.9980537") #A_planck
		
	outf.close()
	f.close()

def main():
	#nov25	
	#ds = np.linspace(0.018, 0.028, 11) 
	#cs = np.linspace(1.e-3, 2.e-3, 40) 
	#bs = np.linspace(10., 20., 40) 

	#jan5
	ds = 10**(np.linspace(np.log10(0.0012), np.log10(0.028), 20))
	cs = np.linspace(1.e-3, 2.e-3, 20) 
	bs = np.log10(np.linspace(10**14., 10**15., 10))

	files = ['output/montepython03_cl_lensed.dat','output/montepython02_cl_lensed.dat']
	#files = glob.glob("*dat")
	l = len(files)
	print l

	likformat(files[0],1)
	likformat(files[1],2)
main()
