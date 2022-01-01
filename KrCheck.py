# -*- coding: utf-8 -*-
from hanspell import spell_checker

def KrCheck(input):
    input_convert = input.replace('.','.#').split('#')
    input_list =  [""]
    time = 0

    for i in input_convert:
        if len(input_list[-1]) + len(i) < 500:
            input_list[-1] += i
        else:
            input_list.append(i)
    
    output_text = spell_checker.check(input_list)

    return output_text
