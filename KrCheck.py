# -*- coding: utf-8 -*-
import sys
from hanspell import spell_checker
reload(sys)
sys.setdefaultencoding("utf-8")

def krcheck(input):
    input_convert = input.replace('.','.#').split('#')
    input_list =  [""]

    for i in input_convert:
        print(i)
        if len(input_list[-1]) + len(i) < 500:
            input_list[-1] += i
        else:
            input_list.append(i)
    
    result = spell_checker.check(input_list)

    return result

def main():
    input = '의미는 메인 함수의 선언, 시작을 의미합니다. 해당 코드 밑에 main 등의 함수 호출 코드를 작성해서 함수의 기능을 수행합니다.의미는 메인 함수의 선언, 시작을 의미합니다. 해당 코드 밑에 main 등의 함수 호출 코드를 작성해서 함수의 기능을 수행합니다.의미는 메인 함수의 선언, 시작을 의미합니다. 해당 코드 밑에 main 등의 함수 호출 코드를 작성해서 함수의 기능을 수행합니다.의미는 메인 함수의 선언, 시작을 의미합니다. 해당 코드 밑에 main 등의 함수 호출 코드를 작성해서 함수의 기능을 수행합니다.의미는 메인 함수의 선언, 시작을 의미합니다. 해당 코드 밑에 main 등의 함수 호출 코드를 작성해서 함수의 기능을 수행합니다.의미는 메인 함수의 선언, 시작을 의미합니다. 해당 코드 밑에 main 등의 함수 호출 코드를 작성해서 함수의 기능을 수행합니다.의미는 메인 함수의 선언, 시작을 의미합니다. 해당 코드 밑에 main 등의 함수 호출 코드를 작성해서 함수의 기능을 수행합니다.의미는 메인 함수의 선언, 시작을 의미합니다. 해당 코드 밑에 main 등의 함수 호출 코드를 작성해서 함수의 기능을 수행합니다.의미는 메인 함수의 선언, 시작을 의미합니다. 해당 코드 밑에 main 등의 함수 호출 코드를 작성해서 함수의 기능을 수행합니다.의미는 메인 함수의 선언, 시작을 의미합니다. 해당 코드 밑에 main 등의 함수 호출 코드를 작성해서 함수의 기능을 수행합니다.의미는 메인 함수의 선언, 시작을 의미합니다. 해당 코드 밑에 main 등의 함수 호출 코드를 작성해서 함수의 기능을 수행합니다.의미는 메인 함수의 선언, 시작을 의미합니다. 해당 코드 밑에 main 등의 함수 호출 코드를 작성해서 함수의 기능을 수행합니다.의미는 메인 함수의 선언, 시작을 의미합니다. 해당 코드 밑에 main 등의 함수 호출 코드를 작성해서 함수의 기능을 수행합니다.의미는 메인 함수의 선언, 시작을 의미합니다. 해당 코드 밑에 main 등의 함수 호출 코드를 작성해서 함수의 기능을 수행합니다.의미는 메인 함수의 선언, 시작을 의미합니다. 해당 코드 밑에 main 등의 함수 호출 코드를 작성해서 함수의 기능을 수행합니다.의미는 메인 함수의 선언, 시작을 의미합니다. 해당 코드 밑에 main 등의 함수 호출 코드를 작성해서 함수의 기능을 수행합니다.의미는 메인 함수의 선언, 시작을 의미합니다. 해당 코드 밑에 main 등의 함수 호출 코드를 작성해서 함수의 기능을 수행합니다.의미는 메인 함수의 선언, 시작을 의미합니다. 해당 코드 밑에 main 등의 함수 호출 코드를 작성해서 함수의 기능을 수행합니다.의미는 메인 함수의 선언, 시작을 의미합니다. 해당 코드 밑에 main 등의 함수 호출 코드를 작성해서 함수의 기능을 수행합니다.의미는 메인 함수의 선언, 시작을 의미합니다. 해당 코드 밑에 main 등의 함수 호출 코드를 작성해서 함수의 기능을 수행합니다.의미는 메인 함수의 선언, 시작을 의미합니다. 해당 코드 밑에 main 등의 함수 호출 코드를 작성해서 함수의 기능을 수행합니다.의미는 메인 함수의 선언, 시작을 의미합니다. 해당 코드 밑에 main 등의 함수 호출 코드를 작성해서 함수의 기능을 수행합니다.의미는 메인 함수의 선언, 시작을 의미합니다. 해당 코드 밑에 main 등의 함수 호출 코드를 작성해서 함수의 기능을 수행합니다.의미는 메인 함수의 선언, 시작을 의미합니다. 해당 코드 밑에 main 등의 함수 호출 코드를 작성해서 함수의 기능을 수행합니다.의미는 메인 함수의 선언, 시작을 의미합니다. 해당 코드 밑에 main 등의 함수 호출 코드를 작성해서 함수의 기능을 수행합니다.의미는 메인 함수의 선언, 시작을 의미합니다. 해당 코드 밑에 main 등의 함수 호출 코드를 작성해서 함수의 기능을 수행합니다.의미는 메인 함수의 선언, 시작을 의미합니다. 해당 코드 밑에 main 등의 함수 호출 코드를 작성해서 함수의 기능을 수행합니다.의미는 메인 함수의 선언, 시작을 의미합니다. 해당 코드 밑에 main 등의 함수 호출 코드를 작성해서 함수의 기능을 수행합니다.의미는 메인 함수의 선언, 시작을 의미합니다. 해당 코드 밑에 main 등의 함수 호출 코드를 작성해서 함수의 기능을 수행합니다.의미는 메인 함수의 선언, 시작을 의미합니다. 해당 코드 밑에 main 등의 함수 호출 코드를 작성해서 함수의 기능을 수행합니다.의미는 메인 함수의 선언, 시작을 의미합니다. 해당 코드 밑에 main 등의 함수 호출 코드를 작성해서 함수의 기능을 수행합니다.의미는 메인 함수의 선언, 시작을 의미합니다. 해당 코드 밑에 main 등의 함수 호출 코드를 작성해서 함수의 기능을 수행합니다.의미는 메인 함수의 선언, 시작을 의미합니다. 해당 코드 밑에 main 등의 함수 호출 코드를 작성해서 함수의 기능을 수행합니다.의미는 메인 함수의 선언, 시작을 의미합니다. 해당 코드 밑에 main 등의 함수 호출 코드를 작성해서 함수의 기능을 수행합니다.의미는 메인 함수의 선언, 시작을 의미합니다. 해당 코드 밑에 main 등의 함수 호출 코드를 작성해서 함수의 기능을 수행합니다.의미는 메인 함수의 선언, 시작을 의미합니다. 해당 코드 밑에 main 등의 함수 호출 코드를 작성해서 함수의 기능을 수행합니다.의미는 메인 함수의 선언, 시작을 의미합니다. 해당 코드 밑에 main 등의 함수 호출 코드를 작성해서 함수의 기능을 수행합니다.의미는 메인 함수의 선언, 시작을 의미합니다. 해당 코드 밑에 main 등의 함수 호출 코드를 작성해서 함수의 기능을 수행합니다.의미는 메인 함수의 선언, 시작을 의미합니다. 해당 코드 밑에 main 등의 함수 호출 코드를 작성해서 함수의 기능을 수행합니다.의미는 메인 함수의 선언, 시작을 의미합니다. 해당 코드 밑에 main 등의 함수 호출 코드를 작성해서 함수의 기능을 수행합니다.의미는 메인 함수의 선언, 시작을 의미합니다. 해당 코드 밑에 main 등의 함수 호출 코드를 작성해서 함수의 기능을 수행합니다.의미는 메인 함수의 선언, 시작을 의미합니다. 해당 코드 밑에 main 등의 함수 호출 코드를 작성해서 함수의 기능을 수행합니다.의미는 메인 함수의 선언, 시작을 의미합니다. 해당 코드 밑에 main 등의 함수 호출 코드를 작성해서 함수의 기능을 수행합니다.의미는 메인 함수의 선언, 시작을 의미합니다. 해당 코드 밑에 main 등의 함수 호출 코드를 작성해서 함수의 기능을 수행합니다.의미는 메인 함수의 선언, 시작을 의미합니다. 해당 코드 밑에 main 등의 함수 호출 코드를 작성해서 함수의 기능을 수행합니다.의미는 메인 함수의 선언, 시작을 의미합니다. 해당 코드 밑에 main 등의 함수 호출 코드를 작성해서 함수의 기능을 수행합니다.의미는 메인 함수의 선언, 시작을 의미합니다. 해당 코드 밑에 main 등의 함수 호출 코드를 작성해서 함수의 기능을 수행합니다.의미는 메인 함수의 선언, 시작을 의미합니다. 해당 코드 밑에 main 등의 함수 호출 코드를 작성해서 함수의 기능을 수행합니다.의미는 메인 함수의 선언, 시작을 의미합니다. 해당 코드 밑에 main 등의 함수 호출 코드를 작성해서 함수의 기능을 수행합니다.의미는 메인 함수의 선언, 시작을 의미합니다. 해당 코드 밑에 main 등의 함수 호출 코드를 작성해서 함수의 기능을 수행합니다.의미는 메인 함수의 선언, 시작을 의미합니다. 해당 코드 밑에 main 등의 함수 호출 코드를 작성해서 함수의 기능을 수행합니다.의미는 메인 함수의 선언, 시작을 의미합니다. 해당 코드 밑에 main 등의 함수 호출 코드를 작성해서 함수의 기능을 수행합니다.의미는 메인 함수의 선언, 시작을 의미합니다. 해당 코드 밑에 main 등의 함수 호출 코드를 작성해서 함수의 기능을 수행합니다.의미는 메인 함수의 선언, 시작을 의미합니다. 해당 코드 밑에 main 등의 함수 호출 코드를 작성해서 함수의 기능을 수행합니다.의미는 메인 함수의 선언, 시작을 의미합니다. 해당 코드 밑에 main 등의 함수 호출 코드를 작성해서 함수의 기능을 수행합니다.의미는 메인 함수의 선언, 시작을 의미합니다. 해당 코드 밑에 main 등의 함수 호출 코드를 작성해서 함수의 기능을 수행합니다.의미는 메인 함수의 선언, 시작을 의미합니다. 해당 코드 밑에 main 등의 함수 호출 코드를 작성해서 함수의 기능을 수행합니다.의미는 메인 함수의 선언, 시작을 의미합니다. 해당 코드 밑에 main 등의 함수 호출 코드를 작성해서 함수의 기능을 수행합니다.의미는 메인 함수의 선언, 시작을 의미합니다. 해당 코드 밑에 main 등의 함수 호출 코드를 작성해서 함수의 기능을 수행합니다.의미는 메인 함수의 선언, 시작을 의미합니다. 해당 코드 밑에 main 등의 함수 호출 코드를 작성해서 함수의 기능을 수행합니다.의미는 메인 함수의 선언, 시작을 의미합니다. 해당 코드 밑에 main 등의 함수 호출 코드를 작성해서 함수의 기능을 수행합니다.의미는 메인 함수의 선언, 시작을 의미합니다. 해당 코드 밑에 main 등의 함수 호출 코드를 작성해서 함수의 기능을 수행합니다.의미는 메인 함수의 선언, 시작을 의미합니다. 해당 코드 밑에 main 등의 함수 호출 코드를 작성해서 함수의 기능을 수행합니다.의미는 메인 함수의 선언, 시작을 의미합니다. 해당 코드 밑에 main 등의 함수 호출 코드를 작성해서 함수의 기능을 수행합니다.의미는 메인 함수의 선언, 시작을 의미합니다. 해당 코드 밑에 main 등의 함수 호출 코드를 작성해서 함수의 기능을 수행합니다.의미는 메인 함수의 선언, 시작을 의미합니다. 해당 코드 밑에 main 등의 함수 호출 코드를 작성해서 함수의 기능을 수행합니다.의미는 메인 함수의 선언, 시작을 의미합니다. 해당 코드 밑에 main 등의 함수 호출 코드를 작성해서 함수의 기능을 수행합니다.의미는 메인 함수의 선언, 시작을 의미합니다. 해당 코드 밑에 main 등의 함수 호출 코드를 작성해서 함수의 기능을 수행합니다.의미는 메인 함수의 선언, 시작을 의미합니다. 해당 코드 밑에 main 등의 함수 호출 코드를 작성해서 함수의 기능을 수행합니다.의미는 메인 함수의 선언, 시작을 의미합니다. 해당 코드 밑에 main 등의 함수 호출 코드를 작성해서 함수의 기능을 수행합니다.의미는 메인 함수의 선언, 시작을 의미합니다. 해당 코드 밑에 main 등의 함수 호출 코드를 작성해서 함수의 기능을 수행합니다.의미는 메인 함수의 선언, 시작을 의미합니다. 해당 코드 밑에 main 등의 함수 호출 코드를 작성해서 함수의 기능을 수행합니다.의미는 메인 함수의 선언, 시작을 의미합니다. 해당 코드 밑에 main 등의 함수 호출 코드를 작성해서 함수의 기능을 수행합니다.의미는 메인 함수의 선언, 시작을 의미합니다. 해당 코드 밑에 main 등의 함수 호출 코드를 작성해서 함수의 기능을 수행합니다.의미는 메인 함수의 선언, 시작을 의미합니다. 해당 코드 밑에 main 등의 함수 호출 코드를 작성해서 함수의 기능을 수행합니다.의미는 메인 함수의 선언, 시작을 의미합니다. 해당 코드 밑에 main 등의 함수 호출 코드를 작성해서 함수의 기능을 수행합니다.의미는 메인 함수의 선언, 시작을 의미합니다. 해당 코드 밑에 main 등의 함수 호출 코드를 작성해서 함수의 기능을 수행합니다.의미는 메인 함수의 선언, 시작을 의미합니다. 해당 코드 밑에 main 등의 함수 호출 코드를 작성해서 함수의 기능을 수행합니다.의미는 메인 함수의 선언, 시작을 의미합니다. 해당 코드 밑에 main 등의 함수 호출 코드를 작성해서 함수의 기능을 수행합니다.의미는 메인 함수의 선언, 시작을 의미합니다. 해당 코드 밑에 main 등의 함수 호출 코드를 작성해서 함수의 기능을 수행합니다.의미는 메인 함수의 선언, 시작을 의미합니다. 해당 코드 밑에 main 등의 함수 호출 코드를 작성해서 함수의 기능을 수행합니다.의미는 메인 함수의 선언, 시작을 의미합니다. 해당 코드 밑에 main 등의 함수 호출 코드를 작성해서 함수의 기능을 수행합니다.의미는 메인 함수의 선언, 시작을 의미합니다. 해당 코드 밑에 main 등의 함수 호출 코드를 작성해서 함수의 기능을 수행합니다.의미는 메인 함수의 선언, 시작을 의미합니다. 해당 코드 밑에 main 등의 함수 호출 코드를 작성해서 함수의 기능을 수행합니다.의미는 메인 함수의 선언, 시작을 의미합니다. 해당 코드 밑에 main 등의 함수 호출 코드를 작성해서 함수의 기능을 수행합니다.의미는 메인 함수의 선언, 시작을 의미합니다. 해당 코드 밑에 main 등의 함수 호출 코드를 작성해서 함수의 기능을 수행합니다.의미는 메인 함수의 선언, 시작을 의미합니다. 해당 코드 밑에 main 등의 함수 호출 코드를 작성해서 함수의 기능을 수행합니다.'
    result = krcheck(input)
    time = 0
    print("검사 전: ")
    for i in result:
        print(i.original)
        time = time + i.time
    print("검사 후: ")
    for i in result:
        print(i.checked)
        time = time + i.time
    print("진행시간: "+time)


if __name__ == "__main__":
	main()