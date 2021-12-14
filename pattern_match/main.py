"""
search returns None if no match found   .search() only gets fist instance
.findall()  will return a tuple of all the instances found

|            OR gate
(...)?       means optional, entire group or none
(...)*       match 0 or more
(...)+       match 1 or more

follow }? to use non greedy...python will return longest match found otherwise
(...){i}     match i occurances only             # a lot eaiser than writting it all out
(...){i,}    match occurances at least i times
(...){,i}    match occurances at least i times
(...){i,n}   match occurances at least i times, but no more than n times
"""
import re

print('\n1') # 1
spider = re.compile(r'Spider( wo)?man')
report = 'Spider woman is the only spider left' # spider man was removed for title 9
result = spider.search(report)
print(f"the character in the report is [{result.group()}]")

print('\n2') # 2
num1 = 'your new cell phone is 310-729-0934'
num2 = 'your new office number is 203-2231'
numbs = re.compile(r'(\d\d\d-)?\d\d\d\d') # area code made optional ...match none or all of portion in ()
result_1 = numbs.search(num1)
result_2 = numbs.search(num2)
print(f"your numbers are {result_1.group()} and {result_2.group()}")

print('\n3') # 3
batMan = re.compile(r'Bat(wo)*man')
title_1 = 'The Adventures of Batman'
result_1 = batMan.search(title_1)
title_2 = 'The Adventures of Batwoman'
result_2 = batMan.search(title_2)
title_3 = 'The Adventures of Batwowowowoman' # keeps catching repeat because it is optional
result_3 = batMan.search(title_3)
print (f"{result_1.group()} , {result_2.group()} , {result_3.group()}")

print('\n4') # 4
warden = 'inmates: 12322020, 34532019, 43432016, and 34292015 are on death row' # num-year
inmates = re.compile(r'(3)+\d\d\d\d')
execution = inmates.search(warden)
print(f"next up is {execution.group()}")

print('\n5') # 5
greedy = re.compile(r'(Ha){3,5}')
lazy = re.compile(r'(Ha){3,5}?')
phrase = 'HaHaHaHaHa' # 5x
result_greedy = greedy.search(phrase)
result_lazy = lazy.search(phrase)
print(f"lazy [{result_lazy.group()}] and greedy is [{result_greedy.group()}]")

print('\n6') # 6
note = 'office: 732-342-6454, mobile: 202-792-3412, home: 219-334-5921'
contact = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d') # can't have groups if using findall if you want list of strings
numbers = contact.findall(note)
print(numbers)
contact = re.compile(r'(\d\d\d)-(\d\d\d)-(\d\d\d\d)') # groups give a list of tuples...not strings
numbers = contact.findall(note)
print(numbers)

