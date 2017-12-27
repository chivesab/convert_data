import sys, csv

date=sys.argv[1]
test=sys.argv[2]+'_'
a=open('heart_'+test+date).read().find('{"dataset"')
b=open('heart_'+test+date).read().rfind("]")
print a,b
c=open('heart_'+test+date,'r').read()[a:b]
d=c+"]}"
f=open('heart_'+test+date+'.txt','w')
f.write(d)
