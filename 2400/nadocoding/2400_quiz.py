'''
주민등록번호 앞 6자리를 변수 id_number에 넣고,
출생년도 끝 두자리\n출생 월일\n그 두개의 곱 출력
예시
id_number = 020316 일 때
출력 예시
02
0316
632
'''

id_number = "040423"
# print(id_number[0:2])
year = id_number[:2]
print(year)
# print(id_number[-6:-4])
# print(id_number[:-4])
# print(id_number[2:])        #0423
# print(id_number[2:6])       #0423
month_day = id_number[-4:]
print(month_day)  #
print(int(year) * int(month_day))
print('곱한결과: ' + str(int(year) * int(month_day)))
print('곱한결과: ', int(year) * int(month_day))
# print(year * month_day)

# String -> int
'''
java
Integer.parseInt("");

python
int()
'''

'''
집 전화번호를 phone_number에 넣고,
지역번호\n맨 끝 네 자리 출력하기
예시
phone_number = 02-1234-5678 또는 032-9876-4321
출력 예시
02			또는		032
5678		또는		4321
'''
phone_number = "02-2540-5357"
print(phone_number[:phone_number.index("-")])
print(phone_number[-4:])

# f-string
name = "임정훈"
age = 18
# %-formatting
print("안녕 나는 %s 이야. 내 나이는 %d 살이야" % (name, age))

# str.format()
print('안녕 나는 {} 이야. 내 나이는 {} 살이야'.format(name, age))

# f-string
print(f'안녕 나는 {name} 이야. 내 나이는 {age} 살이야')

print(name * 10)  # 문자열 + 문자열, 문자열 * 정수형

student_number = '2403'
print(student_number[1:2])
# print(number)
print(student_number[-2:][1])  # '03'[1]
print(int(student_number[-2:]))  # int('03')

# 휴대폰 번호를 입력할 때 - 있든, 없든, 없이 출력하기
phone_number1 = '010-2540-5357'
phone_number2 = '010 7584 1367'
phone_number3 = '01073201685'

phone_number = phone_number2
result = phone_number.replace('-', '').replace(' ', '')
print(result)

'''
Quiz2-1. 학번을 student_number 변수에 넣고, 학급을 출력하고, 학과를 출력하기
반이 0 미만이거나 7 이상이면 "잘못 입력했습니다." 출력하기
student_number = '2100' 또는 student_number = '2000'
<출력 예시>
1반 뉴미디어소프트웨어과 또는 잘못 입력했습니다.
'''
student_number = '2401'  # student_number[1:2]
number = student_number[1]
number = int(number)
majors = ['뉴소과', '뉴소과', '뉴웹과', '뉴웹과', '뉴디과', '뉴디과']
if 1 <= number <= 6:
    print(f"{number}반 {majors[number - 1]}")  # -1을 하냐면, 1->0, 2->1
else:
    print('잘못입력했습니다.')

'''
Quiz2-2. 학번을 함수의 인수(argument)로 전달하여 호출하면 학년과 학과를 리턴하는 함수 만들기
<함수 호출>
grade, major = get_major('2100')
print(major, grade) #뉴미디어소프트웨어과 2
'''


def get_major(student_number):
    majors = ['소', '소', '솔', '솔', '디', '디']
    grade = student_number[0]
    classroom = int(student_number[1])
    return grade, majors[classroom - 1]


grade, major = get_major('2400')
print(major, grade)  # 뉴미디어소프트웨어과 2
'''
Quiz2-3. 인수의 개수에 상관없이 인수로 숫자를 여러개 넣고, 함수를 호출하면 그 인수들의 평균을 구하여 리턴하는 함수 만들기
<함수 호출>

print(average(10, 20, 30)) #20.0
print(average(4, 23)) #13.5
'''


def average(*numbers):
    count = 0
    sum_value = 0
    for number in numbers:
        sum_value += number
        count += 1
    return sum_value / count


# def average(*numbers):
#     return sum(numbers)/len(numbers)

# print(average(10, 20, 30))  # 20.0
# print(average(4, 23))  # 13.5


'''
Quiz2-4. 키(cm)와 몸무게(kg)를 인수로 넣고, 함수를 호출하여 BMI 지수를 리턴하는 함수 만들기
(소수 첫째자리까지 반올림)
* BMI 지수 계산법: 체중(kg) ÷ 키의 제곱(m²)
18.5 미만: 저체중
18.5 이상 23 미만: 보통
23 이상 25 미만: 과체중
25 이상: 비만

<함수 호출>
bmi = get_bmi(176, 69)
print(bmi) #22.3
'''


def get_bmi(height, weight):
    height /= 100
    bmi = weight / height ** 2  # * BMI 지수 계산법: 체중(kg) ÷ 키의 제곱(m²)
    return round(bmi, 1)


bmi = get_bmi(176, 69)
print(bmi)  # 22.3

if bmi < 18.5:
    print('저체중')
elif bmi < 23:  # elif 18.5 <= bmi < 23:
    print('정상')
elif bmi < 25:  # elif 23 <= bmi < 25:
    print('과체중')
else:  # elif 25 <= bmi:
    print('비만')

# import random
# 반4 = list(range(1, 20))
# 반4.remove(3)
# print(반4)
# print(random.choice(반4))

'''----------------------------------------------------------------------------------------------------------------------------------------------------
실습2. 나도코딩 - 파이썬 코딩 무료 강의 1:57:32~2:58:58
기본편 https://www.youtube.com/watch?v=kWiCuklohdY
1:57:32~2:58:58

각 챕터를 할 때마다 주석으로 제목을 달고, 코드 지우지 말고, 이어서 실습하자
이미 냈던 과제1의 파일에 이어서 작성하자
학번_practice.py, 학번_quiz.py 파일 제출

Quiz2-1. 학번을 student_number 변수에 넣고, 학급을 출력하고, 학과를 출력하기
반이 0 미만이거나 7 이상이면 "잘못 입력했습니다." 출력하기
student_number = '2100' 또는 student_number = '2000'
<출력 예시>
1반 뉴미디어소프트웨어과 또는 잘못 입력했습니다.

Quiz2-2. 학번을 함수의 인수(argument)로 전달하여 호출하면 학년과 학과를 리턴하는 함수 만들기
<함수 호출>
grade, major = get_major('2100')
print(major, grade) #뉴미디어소프트웨어과 2

Quiz2-3. 인수의 개수에 상관없이 인수로 숫자를 여러개 넣고, 함수를 호출하면 그 인수들의 평균을 구하여 리턴하는 함수 만들기
<함수 호출>
print(average(10, 20, 30)) #20.0
print(average(4, 23)) #13.5

Quiz2-4. 키(cm)와 몸무게(kg)를 인수로 넣고, 함수를 호출하여 BMI 지수를 리턴하는 함수 만들기
(소수 첫째자리까지 반올림)
* BMI 지수 계산법: 체중(kg) ÷ 키의 제곱(m²)
18.5 미만: 저체중
18.5 이상 23 미만: 보통
23 이상 25 미만: 과체중
25 이상: 비만

<함수 호출>
bmi = get_bmi(176, 69)
print(bmi) #22.3

----------------------------------------------------------------------------------------------------------------------------------------------------
실습1. 나도코딩 - 파이썬 코딩 무료 강의 기본편 ~1:57:32까지
https://www.youtube.com/watch?v=kWiCuklohdY

2. 0:38~7:25 환경설정은 생략(VScode로 코딩하는데 우리는 Pycharm으로 개발)

Quiz1-1.주민등록번호 앞 6자리를 변수 id_number에 넣고,
출생년도 끝 두자리\n출생 월일\n그 두개의 곱 출력
id_number = 020316 일 때
<출력 예시>
02
0316
632

Quiz1-2. 집 전화번호를 phone_number에 넣고,
지역번호\n맨 끝 네 자리 출력하기(지역번호의 자리수와 상관없이 동작하도록 하자)
phone_number = 02-1234-5678 또는 032-9876-4321
<출력 예시>
02 또는 032
5678 또는 4321

3. 각 챕터를 할 때마다 주석으로 제목을 달고 지난 내용 지우지 말고 실습하자
nadocoding폴더 만들고 그 안에
학번_helloworld.py,
학번_practice.py,
학번_quiz.py 파일 제출(압축하지 말고 파일 각각 제출)
'''
# 구구단 7단 출력하기
# i : 1~9: 1, 2, 3, 4, 5, 6, 7, 8, 9
for i in range(1, 9 + 1):
    print(f'7 x {i} = {7 * i}')

# 구구단 2~9단 출력하기
#dan: 2~9단
#i: x1~9
for dan in range(2, 9 + 1):     #2~9
    for i in range(1, 9 + 1):   #x1~x9
        print(f'{dan} x {i} = {dan * i}')
        #print() #1번
    print()     #2번
#print()         #3번

#구구단 2~7단까지 출력하기    break
for dan in range(2, 9 + 1):     #2~9
    for i in range(1, 9 + 1):   #x1~x9
        print(f'{dan} x {i} = {dan * i}')
    print()     #2번
    if dan == 7:        #7단 위에서 출력하고, 끝내라
        break

#구구단 2~7단 출력하되, x1, x3, x5, x7, x9 인 것만 출력하기    break, continue
for dan in range(2, 9 + 1):     #2~9
    for i in range(1, 9 + 1):   #x1~x9
        if i % 2 == 0:  #if i == 2 or i == 4 or i == 6 or i == 8:
            continue
        print(f'{dan} x {i} = {dan * i}')
    print()     #2번
    if dan == 7:        #7단 위에서 출력하고, 끝내라
        break