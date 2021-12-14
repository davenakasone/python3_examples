"""
making a multiplication quiz
"""

import pyinputplus as pyip
import os
import random
import time

number_of_questions = 4
correct_answers = 0
for question in range(number_of_questions):
    num1 = random.randint(0,9)
    num2 = random.randint(0,9)
    prompt = f"#{question}.  {num1} x {num2} = "
    try:
        pyip.inputStr(prompt,\
                      allowRegexes = ['^%s$' % (num1 * num2)],\
                      blockRegexes = [('.*', 'wrong')],\
                      timeout = 5,\
                      limit = 2)
    except pyip.TimeoutException:
        print('out of time')
    except pyip.RetryLimitException:
        print('no more attempts')
    else:
        print('correct')
        correct_answers += 1
    print(f"score {correct_answers} / {question + 1}")
    time.sleep(1)
    os.system("clear")
print(f"test complete, final score {correct_answers} / {number_of_questions}")




