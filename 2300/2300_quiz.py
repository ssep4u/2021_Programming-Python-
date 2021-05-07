'''
3. Quiz
3-1.주민등록번호 앞 6자리를 변수 id_number에 넣고,
출생년도 끝 두자리\n출생 월일\n그 두개의 곱 출력
예시
id_number = 020316 일 때

출력 예시
02
0316
632
'''

id_number = "020316"
year = id_number[0:2]  # [:2], [-6:-4]
month_day = id_number[2:6]  # [2:] [-4:]
print(year)
print(month_day)
print("둘의 곱은: " + str(int(year) * int(month_day)))

'''
3-2. 집 전화번호를 phone_number에 넣고,
지역번호\n맨 끝 네 자리 출력하기(지역번호의 자리수와 상관없이 동작하도록 하자)
예시
phone_number = 02-1234-5678 또는 032-9876-4321

출력 예시
02 또는 032
5678 또는 4321
'''
phone_number = "02-1234-5678"
phone_number2 = "032-9876-4321"
x = phone_number2.find('-')        #index() 없으면, ValueError    , find() 없으면 -1
print(phone_number2[0:x])  # [:2]
print(phone_number2[-4:])  # [8:]

# 전화번호 입력시, -가 있든, -가 없든, 찰떡같이 알아먹기
phone_number1 = '010-1234-5678'
phone_number2 = '01098765432'
phone_number3 = '010 1111 2222'

phone_number = phone_number3
result = phone_number.replace('-', '').replace(' ', '')
print(result)

# 2-1
'''
학번을 student_number 변수에 넣고, 학급을 출력하고, 학과를 출력하기
반이 0 미만이거나 7 이상이면 "잘못 입력했습니다." 출력하기
student_number = '2100'		또는			student_number = '2000'
<출력예시>
1반 뉴미디어소프트웨어과					잘못 입력했습니다.
'''
student_number = "2000"
number = student_number[1]  # [1:2]        #'3'
number = int(number)  # str -> int
# if number==1:
#     print(f"{number}반 뉴미디어소프트웨어과")
# elif number == 2:
#     print(f"{number}반 뉴미디어소프트웨어과")
# elif number == 3:
#     print(f"{number}반 뉴미디어웹솔루션과")
# elif number == 4:
#     print(f"{number}반 뉴미디어웹솔루션과")
# elif number == 5:
#     print(f"{number}반 뉴미디어디자인과")
# elif number == 6:
#     print(f"{number}반 뉴미디어디자인과")
# else :
#     print("잘못 입력하셨습니다")
# majors = ['뉴미디어소프트웨어과', '뉴미디어소프트웨어과', '뉴미디어웹솔루션과', '뉴미디어웹솔루션과', '뉴미디어디자인과', '뉴미디어디자인과']
# print(f'{number}반 {majors[number-1]}')

majors = ['뉴미디어소프트웨어과', '뉴미디어웹솔루션과', '뉴미디어디자인과']
if 1 <= number <= 6:            # 1 <= number && number <= 6   in java
    print(f'{number}반 {majors[(number - 1) // 2]}')
else:
    print("잘못입력했습니다.")

'''
학번을 함수의 인수(argument)로 전달하여 호출하면 학년과 학과를 리턴하는 함수 만들기
함수 호출
grade, major = get_major('2100')
print(major, grade) 				#뉴미디어소프트웨어과 2
'''

def get_major(student_number):
    global major
    grade = student_number[0]       #'2'
    if student_number[1] =='1' or student_number[1] =='2':      #student_number[1] == '3'
        major = "뉴미디어소프트웨어과"
    elif student_number[1] == '3' or student_number[1] == '4':       # '4' == True
        major = "뉴미디어웹솔루션과"
    elif student_number[1] == '5' or student_number[1] == '6':
        major = "뉴미디어디자인과"
    return grade, major
grade,major = get_major("2510")
print(major,grade)

'''
인수의 개수에 상관없이 인수로 숫자를 여러개 넣고, 함수를 호출하면 그 인수들의 평균을 구하여 리턴하는 함수 만들기
print(average(10, 20, 30))			#20.0
print(average(4, 23))			#13.5
'''
#평균 = 더한만큼 / 나누면 되잖아요 = 총합 / 개수
def average(*numbers):
    sum_value = 0
    count = 0
    for number in numbers:
        sum_value += number
        count += 1
    return sum_value / count

print(average(10, 20, 30))          #(10, 20, 30) ==> numbers
print(average(4, 23))               #(4, 23) ==> numbers

def average2(*numbers):
    return sum(numbers) / len(numbers)

print(average2(10, 20, 30))          #(10, 20, 30) ==> numbers
print(average2(4, 23))               #(4, 23) ==> numbers

'''
4. 키(cm)와 몸무게(kg)를 인수로 넣고, 함수를 호출하여 BMI 지수를 리턴하는 함수 만들기
  (소수 첫째자리까지 반올림)
  * BMI 지수 계산법: 체중(kg) ÷ 키의 제곱(m²)
  
    a. 함수호출
      bmi = get_bmi(176, 69)
      print(bmi)					#22.3
'''
def get_bmi(height, weight):
    height /= 100
    return round(weight / height ** 2, 1)

bmi = get_bmi(176, 69)
# print(bmi)
if bmi < 18.5:
    print('저체중')
elif bmi < 23:
    print('정상')
elif bmi < 25:
    print('과체중')
elif 25 <= bmi:
    print('비만')

# 구구단 7단 출력하기
for i in range(1, 9 + 1):    #i : 1~9
    print(f'7 x {i} = {7 * i}')

# 구구단 2~9단 출력하기
for dan in range(2, 10):   #dan: 2~9
    for i in range(1, 9 + 1):    #i : 1~9
        print(f'{dan} x {i} = {dan * i}')
    print('-' * 10)

# 구구단 2~7단까지 출력하기
for dan in range(2, 9 + 1):   #dan: 2~9
    for i in range(1, 9 + 1):    #i : 1~9
        print(f'{dan} x {i} = {dan * i}')
    print('-' * 10)
    if dan == 7:
        break

# 구구단 2~7단 출력하되, x1, x3, x5, x7, x9 인 것만 출력하기
for dan in range(2, 9 + 1):   #dan: 2~9
    for i in range(1, 9 + 1):    #i : 1~9
        if i % 2 == 0:  #i == 2 or i == 4 or i == 6 or i == 8:
            continue
        print(f'{dan} x {i} = {dan * i}')
    print('-' * 10)
    if dan == 7:
        break

'''
Quiz3-1. n_sum() 함수를 만든다. 함수의 인수(argument)로 10자리 숫자보다 작은 숫자를 넣으면, 각 자리의 숫자의 합계를 리턴한다. 10자리 이상이면 -1 리턴한다.
'''
def n_sum(n):
    #하나씩 쪼개자
    n = 123
        #1, 2, 3
        #123 // 100 : 1
        #123 // 10  : 2
        #123 % 10 : 3
    # 123 -> "123"
    n = str(n)



    #쪼갠거 하나씩 더하자 => 리턴

result = n_sum(10)
print(result)        #1
result = n_sum(331)
print(result)         #7
result = n_sum(408)
print(result)         #12
result = n_sum(1000000000)
print(result)         #-1




