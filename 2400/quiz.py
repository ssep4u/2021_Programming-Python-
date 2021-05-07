'''
국어 30점, 영어 20점, 파이썬 80점을 저장하고,
모든 과목과 점수를 출력하고, 총점과 평균을 출력하기
'''
records1 = {'국어': 30, '영어': 20, '파이썬': 80}
records2 = {'국어': 70, '영어': 100, '파이썬': 30}
cherry_blossoms = [records1, records2]

# def sum_average(records):
#   count = 0
#   sum_value = 0
#   for key in records:
#     print(key, ':', records[key])
#     sum_value += records[key]
#     count += 1
#   print('총점:', sum_value, '\t평균: ', sum_value / count)
#
# keys = cherry_blossoms[0].keys()
# for key in keys:
#   count = 0
#   sum_value = 0
#   for cherry_blossom in cherry_blossoms:
#     sum_value += cherry_blossom[key]
#     count += 1
#   print(key, sum_value / count)

'''
Quiz3-1. n_sum() 함수를 만든다. 함수의 인수(argument)로 10자리 숫자보다 작은 숫자를 넣으면, 각 자리의 숫자의 합계를 리턴한다. 10자리 이상이면 -1 리턴한다.
'''


def n_sum(numbers):
  # return sum([int(n) for n in str(numbers)])
  return sum(list(map(int, str(numbers))))


result = n_sum(331)
print(result)  # 1
result = n_sum(1000000000)
print(result)  # 1

'''
Quiz3-2. get_subway_fare() 함수를 만든다. 이 함수는 인수로 가는 거리(km)를 숫자로 넣으면, 요금을 리턴한다.
* 지하철 요금계산법 10km 이내: 720원(청소년), 10~50km: 5km마다 100원, 50km 초과 시 8km마다 100원
'''


def get_subway_fare(km):
  fare = 0
  if km <= 10:
    fare += 720
  elif km <= 50:
    km -= 10
    fare += 720
    quotient = km // 5
    remainder = km % 5
    fare += quotient * 100
    if remainder != 0:
      fare += 100
  elif km > 50:
    km -= 10
    fare += 720
    km -= (50 - 10)
    fare += (50 - 10) // 5 * 100
    quotient = km // 8
    remainder = km % 8
    fare += quotient * 100
    if remainder != 0:
      fare += 100

  return fare


fare = get_subway_fare(5)
print(fare)  # 720
fare = get_subway_fare(26)
print(fare)  # 1120
fare = get_subway_fare(61)
print(fare)  # 1720


def get_three_six_nine(number):
  count = 0
  number_str = str(number)
  count += number_str.count('3')
  count += number_str.count('6')
  count += number_str.count('9')
  # for ch in str(number):
  #   if ch in '369':
  #     count += 1
  # count == 0이면 숫자, 아니면 count만큼 짝
  if count == 0:
    return number
  else:
    return '짝' * count


result = get_three_six_nine(1)
print(result)  # 1
result = get_three_six_nine(3)
print(result)  # 짝
result = get_three_six_nine(16)
print(result)  # 짝
result = get_three_six_nine(36)
print(result)  # 짝짝
