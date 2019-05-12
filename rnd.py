
#!/usr/bin/env python

#
#每日口算题生成程序
#

import random
import math

def gen_equations( display_result ):
    for key,value in kv.items():
        second_arg = key - value
        if (second_arg > 0):
            if (display_result):
                print value , "+" , second_arg , "=" , key 
            else:
                print value , "+" , second_arg , "="
        else:
            if (display_result):
                print value , "-", abs(second_arg) , "=" , key 
            else:
                print value , "-", abs(second_arg) , "="

number_of_equations = 20
i = 0;
kv = {}
while (len(kv) < number_of_equations):
    result = random.randint(1,100)
    first_arg = random.randint(1,100)
    second_arg = 0;
    kv[result]=first_arg
    #print len(kv)
    #if (result == 100):
    #    second_arg = result - second_arg
    #print result
    i+=1;
#print kv.items()
print "questions:"
gen_equations(0)

print ""
print "answers:"
gen_equations(1)

