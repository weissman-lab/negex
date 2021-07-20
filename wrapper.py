# This script has been modified so that it runs from the command line as
# python3 wrapper.py

from negex import *
import csv

rfile = open(r'negex_triggers.txt')
irules = sortRules(rfile.readlines())
reports = csv.reader(open(r'Annotations-1-120.txt','r'), delimiter = '\t')
reportNum = 0
correctNum = 0
ofile = open(r'negex_output.txt', 'w')
output = []
outputfile = csv.writer(ofile, delimiter = '\t')
for report in reports:
    tagger = negTagger(sentence = report[2], phrases = [report[1]], rules = irules, negP=False)
    report.append(tagger.getNegTaggedSentence())
    report.append(tagger.getNegationFlag())
    report = report + tagger.getScopes()
    reportNum += 1
    if report[3].lower() == report[5]:
        correctNum +=1
    output.append(report)
outputfile.writerow(['Percentage correct:', float(correctNum)/float(reportNum)])
for row in output:
    if row:
        outputfile.writerow(row)
ofile.close()
