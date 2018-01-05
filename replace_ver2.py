import csv
import sys

#1. Place each record of a file in a list.
#2. Iterate thru each element of the list.
#3. If the index==1 amd x is '0'.

#test=sys.argv[2] #sys.argv[2]=test3
#date=sys.argv[1] #sys.argv[1]=2017-12-08
test='test3'
date='2017-12-26'
file_heart='heart_'+test+'_try.csv' # = heart_test3_2017-12-08.csv
f=open('replace_try.csv','w') #heart_test3_2017-12-08_replace.csv

reader = csv.reader(open(file_heart, "rb"))
y=1
for row in reader:
    for i, x in enumerate(row):
        if (i==1 and x=='0'):
            x =row[i]=" "
        if (i==0):
            x=row[i][3:5]
            x=int(x)
            if y==x+1:
                y+=1
            else:
                if y==61:
                    x=0
                    y=2
                else:
                    x=y-1
                    y+=1
            print 'x=',x
            f.write(''.join(str(x))+'\n')
#    f.write(''.join(str(x) for x in row)+'\n')


#heart_test3_1213_replace.csv

