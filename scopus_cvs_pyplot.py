# plot stats

from matplotlib.pyplot import *
from matplotlib import dates
from scipy import *
import csv
import itertools as its
rcParams['font.size']=16
rcParams['font.family']='Serif'
def read_cvs_file( fname ):
    data = genfromtxt(fname, skip_header=9, delimiter=',',
                       converters={0:lambda s:int(s.decode().strip('"')), 1:lambda s:int(s.decode().strip('"'))})
    data = array([list(item) for item in data])
    data = data.T
    return data

data1 = read_cvs_file('Scopus-allAuthors-Analyze-Year.csv')
data2 = read_cvs_file('Scopus-noTOMIteam-Analyze-Year.csv')
data3 = read_cvs_file('Scopus-integrated-Analyze-Year.csv')


bar(data3[0],data3[1],label='AND integrated')
# bar(data1[0],data1[1],label='TOMI low-cost')
bar(data2[0],data2[1],label='AND low-cost')
title('Scopus: \"optical coherence tomography\"')
ylabel('Number per year')
xlabel('Year')
legend()
tight_layout()
# savefig('research_output.pdf')
show()
