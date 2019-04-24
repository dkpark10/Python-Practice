# 딕셔너리
# dictionary = {'key1':value1, 'key2':value2}
# key = int, float, str, bool but list, dictionary can't 키값에 넣을 수 있느거
# value = all type ex)int, float, str, bool, class, list, ditionary 값에 넣을 수 있는거 

powerlifter={'bench press':120,'squart':210,'deadlift':230}

dic1={} # empty dictionary
dic2=dict() # empty dictionary

print(powerlifter['bench press'], powerlifter['squart'],sep=",") # 120 210
powerlifter['bench press']= 140 # bench press alloc
powerlifter['squart']= 240 # squart alloc

powerlifter['military press']= 100 # there are no 'military press' in dic so new key alloc(???)

# when find key use 'in'
# 'not in' =>
print('bench press'in powerlifter) # true
print('arm curl'in powerlifter) # false

# when find dictionary key size
print(len(powerlifter)) # 4







# setdefault: 키-값 쌍 추가
# update: 키의 값 수정, 키가 없으면 키-값 쌍 추가

powerlifter={'bench':10000, 'squart':23, 'deadlift':80}
powerlifter.setdefault('military press') # 밀리터리프레스 추가 값은 없으므로 None 값
powerlifter.setdefault('back extension',2000) # 키 값 쌍으로 추가 
#굳이 이렇게 쓸 필요는 없을듯..

# 키의 값 수정
powerlifter.update(deadlift=8700, squart=21) # 여러개 수정
