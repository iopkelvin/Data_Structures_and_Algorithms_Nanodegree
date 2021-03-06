"""
Read file into texts and calls.
It's ok if you don't understand how to read files.
"""
import csv

with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)

"""
TASK 4:
The telephone company want to identify numbers that might be doing
telephone marketing. Create a set of possible telemarketers:
these are numbers that make outgoing calls but never send texts,
receive texts or receive incoming calls.

Print a message:
"These numbers could be telemarketers: "
<list of numbers>
The list of numbers should be print out one per line in lexicographic order with no duplicates.
"""

# call_send = [x[0] for x in calls if x[0].startswith('140')]
makes_call = set([call[0] for call in calls])
receives_call = set([call[1] for call in calls])

makes_text = set([text[0] for text in texts])
receives_text = set([text[1] for text in texts])

telemarketer = []
for caller in makes_call:
    if (caller not in receives_call) and (caller not in makes_text) and (caller not in receives_text):
        telemarketer.append(caller)


unique_sorted_tele = sorted(telemarketer)
print("These numbers could be telemarketers: ")
for i in unique_sorted_tele:
    print(i)