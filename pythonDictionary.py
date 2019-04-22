# setdefault: 키-값 쌍 추가
# update: 키의 값 수정, 키가 없으면 키-값 쌍 추가

powerlifter={'bench':10000, 'squart':23, 'deadlift':80}
powerlifter.setdefault('military press') # 밀리터리프레스 추가 값은 없으므로 None 값
powerlifter.setdefault('back extension',2000) # 키 값 쌍으로 추가

# 키의 값 수정
powerlifter.update(deadlift=8700, squart=21) # 여러개 수정
