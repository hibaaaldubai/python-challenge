import os
import csv

election_data = r"C:\Users\haldu\UBHM-VIRT-DATA-PT-08-2022-U-LOLC\02-Homework\03-Python\Instructions\PyPoll\Resources\election_data.csv"

votersamount = 0
highestvotes = 0

candidates = {}
candidatepercentages = {}

csvfile = open(election_data, 'r')
csvreader = csv.reader(csvfile, delimiter=',')

for voter in csvreader:
    votersamount = votersamount + 1
    candidatevotedfor = voter['Candidate']

    try:
        candidates[candidatevotedfor] = candidates[candidatevotedfor] + 1

    except:
        candidates[candidatevotedfor] = 1

for c in candidates:
    votesamount = candidates[c]
    percentage = (votesamount/votersamount) * 100
    candidatepercentages[c] = percentage

    if numberofvotes > highestvotes:
        highestvotes = numberofvotes

for c in candidates:
    votesamount = candidates[c]
    if votesamount == highestvotes:
        winner = c


print(votersamount)
print(candidates)

csvfile.close()
