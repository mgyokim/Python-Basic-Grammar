
# if문
# if문은 왜 필요할까?
# 다음과 같은 상상을 해보자.
# "돈이 있으면 택시를 타고, 돈이 없으면 걸어 간다."

# 우리 모두에게 일어날 수 있는 상황 중 하나이다.
# 프로그래밍도 사람이 하는 것이므로 위 문장처럼 주어진 조건을 판단한 후 그 상황에 맞게 처리해야 할 경우가 생긴다.
# 이렇듯 프로그래밍에서 조건을 판단하여 해당 조건에 맞는 상황을 수행하는데 쓰는 것이 바로 if 문이다.

# 위와 같은 상황을 파이썬에서는 다음과 같이 표현할 수 있다.
money = True
if money:
    print("택시를 타고 가라")
else:
    print("걸어 가라")

# money에 True를 입력했으므로 money는 참이다. 따라서 if문 다음 문장이 수행되어 '택시를 타고 가라'가 출력된다.


