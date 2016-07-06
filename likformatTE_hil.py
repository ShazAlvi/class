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

	print(len(l))
	#for i in range(len(l)):
	for i in range(0,2507):
		#f.write(str(l[i][index]) + '\n')
		f.write(str(2.*pi*l[i][index]/(l[i][0]*(l[i][0] + 1.))) + '\n')

def likformat(filename):#, outfname):
	f = open(filename, 'r')
	#outf = open('TElikcls_hil/' + filename[filename.rfind('/')+1:filename.rfind('.')] + '_likcls.txt', 'w')
	outf = open('hilcambfixprior.txt', 'w')
	lines = f.readlines()
	for i in range(len(lines)):
		lines[i] = lines[i].strip().split()[:7]
		
		#camb CHANGE TO 4
		lines[i] = [float(lines[i][0]), float(lines[i][1]), float(lines[i][2]), float(lines[i][4])]
		#class
		#lines[i] = [float(lines[i][0]), float(lines[i][1]), float(lines[i][2]), float(lines[i][3])]

	outf.write('0\n0\n')
	writecls(outf, lines, 'TT')
	outf.write('0\n0\n')
	writecls(outf, lines, 'EE')
	outf.write('0\n0\n')
	writecls(outf, lines, 'TE')

        #outf.write("27.2\n") #A_cib_217                                                                      
	outf.write("55.03218\n") #A_cib_217                                                                      
        outf.write("-1.3\n") #cib_index                                                                      
        #outf.write("0.03\n") #xi_sz_cib                                                                     
        outf.write("0.04252888\n") #xi_sz_cib                                                                 
        #outf.write("6.8\n") #A_sz                                                                            
        outf.write("5.854106\n") #A_sz                                                                            
        #outf.write("152.0\n") #ps_A_100_100                                                                  
        outf.write("237.5333\n") #ps_A_100_100                                                                  
        #outf.write("63.3\n") #ps_A_143_143                                                                   
        outf.write("39.56775\n") #ps_A_143_143                                                                   
        outf.write('28.45131\n') #ps_A_143_217                                         
        #outf.write(str(0.916*sqrt(63.3*117.0)) + '\n') #ps_A_143_217                                         
        outf.write("109.0333\n") #ps_A_217_217                                                                  
        #outf.write("117.0\n") #ps_A_217_217                                                                  
        outf.write("1.838041\n") #ksz_norm                                                                        
        #outf.write("0.9\n") #ksz_norm                                                                        
        outf.write("7.004857\n") #gal545_A_100 
        #outf.write("7.\n") #gal545_A_100 (used prior max)                                                    
        #outf.write("9.\n") #gal545_A_143 (used prior max)                                                    
        outf.write("7.709635\n") #gal545_A_143 
        outf.write("18.72368\n") #gal545_A_143_217 
        #outf.write("21.0\n") #gal545_A_143_217 (used prior max)                                              
        outf.write("74.04406\n") #gal545_A_217 
        #outf.write("80.0\n") #gal545_A_217 (used prior max)                                                  
        outf.write("0.2061162\n") #galf_EE_A_100 
        #outf.write("0.060\n") #galf_EE_A_100 (used prior max)                                                
        outf.write("0.05255299\n") #galf_EE_A_100_143 
        #outf.write("0.050\n") #galf_EE_A_100_143 (used prior max)                                            
        outf.write("0.1510102\n") #galf_EE_A_100_217
        #outf.write("0.110\n") #galf_EE_A_100_217 (used prior max)                                            
        outf.write("0.1038330\n") #galf_EE_A_143
        #outf.write("0.10\n") #galf_EE_A_143 (used prior max)                                                 
        outf.write("0.2527346\n") #galf_EE_A_143_217
        #outf.write("0.240\n") #galf_EE_A_143_217 (used prior max)                                            
        outf.write("0.6770028\n") #galf_EE_A_217
        #outf.write("0.72\n") #galf_EE_A_217 (used prior max)                                                 
	outf.write("-2.4\n") #galf_EE_index                                                                  
        outf.write("0.2013605\n") #galf_TE_A_100
        #outf.write("0.140\n") #galf_TE_A_100 (used prior max)                                                
        outf.write("0.2110358\n") #galf_TE_A_100_143
        #outf.write("0.120\n") #galf_TE_A_100_143 (used prior max)                                            
        outf.write("0.3983750\n") #galf_TE_A_100_217
        #outf.write("0.30\n") #galf_TE_A_100_217 (used prior max)                                             
        outf.write("0.2040024\n") #galf_TE_A_143
        #outf.write("0.240\n") #galf_TE_A_143 (used prior max)                                                
        outf.write("0.3798387\n") #galf_TE_A_143_217
        #outf.write("0.30\n") #galf_TE_A_143_217 (used prior max)                                             
        outf.write("1.361574\n") #galf_TE_A_217 (used prior max)                                                 
        #outf.write("1.80\n") #galf_TE_A_217 (used prior max)                                                 
        outf.write("-2.4\n") #galf_TE_index



	outf.write("0.0\n") #bleak_epsilon_0_0T_0E
	outf.write("0.0\n") #bleak_epsilon_1_0T_0E
	outf.write("0.0\n") #bleak_epsilon_2_0T_0E
	outf.write("0.0\n") #bleak_epsilon_3_0T_0E
	outf.write("0.0\n") #bleak_epsilon_4_0T_0E
	outf.write("0.0\n") #bleak_epsilon_0_0T_1E
	outf.write("0.0\n") #bleak_epsilon_1_0T_1E
	outf.write("0.0\n") #bleak_epsilon_2_0T_1E
	outf.write("0.0\n") #bleak_epsilon_3_0T_1E
	outf.write("0.0\n") #bleak_epsilon_4_0T_1E
	outf.write("0.0\n") #bleak_epsilon_0_0T_2E
	outf.write("0.0\n") #bleak_epsilon_1_0T_2E
	outf.write("0.0\n") #bleak_epsilon_2_0T_2E
	outf.write("0.0\n") #bleak_epsilon_3_0T_2E
	outf.write("0.0\n") #bleak_epsilon_4_0T_2E
	outf.write("0.0\n") #bleak_epsilon_0_1T_1E
	outf.write("0.0\n") #bleak_epsilon_1_1T_1E
	outf.write("0.0\n") #bleak_epsilon_2_1T_1E
	outf.write("0.0\n") #bleak_epsilon_3_1T_1E
	outf.write("0.0\n") #bleak_epsilon_4_1T_1E
	outf.write("0.0\n") #bleak_epsilon_0_1T_2E
	outf.write("0.0\n") #bleak_epsilon_1_1T_2E
	outf.write("0.0\n") #bleak_epsilon_2_1T_2E
	outf.write("0.0\n") #bleak_epsilon_3_1T_2E
	outf.write("0.0\n") #bleak_epsilon_4_1T_2E
	outf.write("0.0\n") #bleak_epsilon_0_2T_2E
	outf.write("0.0\n") #bleak_epsilon_1_2T_2E
	outf.write("0.0\n") #bleak_epsilon_2_2T_2E
	outf.write("0.0\n") #bleak_epsilon_3_2T_2E
	outf.write("0.0\n") #bleak_epsilon_4_2T_2E
	outf.write("0.0\n") #bleak_epsilon_0_0E_0E
	outf.write("0.0\n") #bleak_epsilon_1_0E_0E
	outf.write("0.0\n") #bleak_epsilon_2_0E_0E
	outf.write("0.0\n") #bleak_epsilon_3_0E_0E
	outf.write("0.0\n") #bleak_epsilon_4_0E_0E
	outf.write("0.0\n") #bleak_epsilon_0_0E_1E
	outf.write("0.0\n") #bleak_epsilon_1_0E_1E
	outf.write("0.0\n") #bleak_epsilon_2_0E_1E
	outf.write("0.0\n") #bleak_epsilon_3_0E_1E
	outf.write("0.0\n") #bleak_epsilon_4_0E_1E
	outf.write("0.0\n") #bleak_epsilon_0_0E_2E
	outf.write("0.0\n") #bleak_epsilon_1_0E_2E
	outf.write("0.0\n") #bleak_epsilon_2_0E_2E
	outf.write("0.0\n") #bleak_epsilon_3_0E_2E
	outf.write("0.0\n") #bleak_epsilon_4_0E_2E
	outf.write("0.0\n") #bleak_epsilon_0_1E_1E
	outf.write("0.0\n") #bleak_epsilon_1_1E_1E
	outf.write("0.0\n") #bleak_epsilon_2_1E_1E
	outf.write("0.0\n") #bleak_epsilon_3_1E_1E
	outf.write("0.0\n") #bleak_epsilon_4_1E_1E
	outf.write("0.0\n") #bleak_epsilon_0_1E_2E
	outf.write("0.0\n") #bleak_epsilon_1_1E_2E
	outf.write("0.0\n") #bleak_epsilon_2_1E_2E
	outf.write("0.0\n") #bleak_epsilon_3_1E_2E
	outf.write("0.0\n") #bleak_epsilon_4_1E_2E
	outf.write("0.0\n") #bleak_epsilon_0_2E_2E
	outf.write("0.0\n") #bleak_epsilon_1_2E_2E
	outf.write("0.0\n") #bleak_epsilon_2_2E_2E
	outf.write("0.0\n") #bleak_epsilon_3_2E_2E
	outf.write("0.0\n") #bleak_epsilon_4_2E_2E
        outf.write("0.9982559\n") #calib_100T                                                         
        #outf.write("0.999\n") #calib_100T                                                         
        outf.write("0.9949409\n") #calib_217T                                                         
        #outf.write("0.995\n") #calib_217T                                                         
	outf.write("1.\n") #calib_100P                                                            
        outf.write("1.\n") #calib_143P                                                            
        outf.write("1.\n") #calib_217P                                                            
	outf.write("1.\n") #A_pol                                                                 
        outf.write("0.9980537") #A_planck   
        #outf.write("1.") #A_planck   
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

	files = ['../montepython_public-2.2.1/unlensedcls.txt']
	#files = ['output/montepython02_cl.dat']
	#files = glob.glob("*dat")
	l = len(files)
	print l
	for m in range(l):
		#print int(.1*l)
		#if (m+1)%int(.1*l) == 0:
		#	print 'Done ' + str(100.*float(m+1)/float(l)) + '%'
		likformat(files[m])
	#likformat(options.i, options.o)
main()
