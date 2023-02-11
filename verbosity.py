import os

logLvl = os.environ.get('LOG_LEVEL')

if logLvl == '1':
    logTemp = open('log/logv1.txt','r')
    logInfo = logTemp.readlines()
elif logLvl == '2':
    logTemp = open('log/logv2.txt','r')
    logInfo = logTemp.readlines()
else:
    logInfo = []

log_true = open('log_file.txt','w+')

for t in logInfo:
    log_true.write(t)
    