
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

# if문의 기본 구조
# 다음은 if와 else를 사용한 조건문의 기본 구조이다.
# if 조건문 :
#     수행할 문장1
#     수행할 문장2
# else:
#     수행핢 문장A
#     수행할 문장B

# 조건문을 테스트해서 참이면 if문 바로 다음 문장(if 블록)들을 수행하고, 조건문이 거짓이면 else문 다음 문장(else 블록)들을 수행하게 된다.
# 그러므로 else문은 if문 없이 독립적으로 사용할 수 없다.

# 들여쓰기
# if문을 만들 때는 if 조건문: 바로 아래 문장부터 if문에 속하는 모든 문장에 들여쓰기(indentation)를 해주어야 한다.
# 오른쪽에서 보는 것과 같이 조건문이 참일 경우 "수행할 문장1"을 들여쓰기했고 "수행할 문장2"와 "수행할 문장3"도 들여쓰기 해 주었다.
# 다른 프로그래밍 언어를 사용해 온 사람들은 파이썬에서 "수행할 문장"을 들여쓰기 하는 것을 무시하는 경우가 많으니 더 주의해야 한다.
# if 조건문:
#     수행할 문장1
#     수행할 문장2
#     수행할 문장3

# 만약 아래와같이 작성하면 오류가 발생한다.
# if 조건문:
#     수행할 문장1
# 수행할 문장2
#     수행할 문장3

# "수행할 문장2"를 들여쓰기 하지 않았기 때문이다.

# money = True
# if money:
#     print("택시를")
# print("타고")
#     print("가라")

# 위 예제를 실행하면 들여쓰기 오류가 발생하는 것을 확인 할 수 있다.
# 그렇다면 들여쓰기는 공백(Spacebar)로 하는 것이 좋을까? 아니면 탭(Tab)으로 하는 것이 좋을까? 이에 대한 논란은 파이써을 사용하는 사람들 사이에서 아직도 계속되고 있다.
# 탭으로 하자는 쪽과 공백으로 하자는 쪽 모두가 동의하는 내용은 단 하나이다.
# 2가지를 혼용해서 쓰지는 말자는 것.
# 공백으로 할 거면 항상 공백으로 통일하고, 탭으로 할 거면 항상 탭으로 통일해서 사용하자는 말이다.
# 탭이나 공백은 프로그램 소스에서 눈으로 보이는 것이 아니기 때문에 혼용해서 쓰면 오류의 원인이 되니 주의하도록 하자.
# 나는 탭을 이용하는 중이다.

# [조건문 다음에 콜론(:)을 잊지 말자!]
# if 조건문 뒤에는 반드시 콜론(:)이 붙는다. 어떤 특별한 의미가 있다기 보다는 파이썬의 문법 구조이다. 왜 하필 콜론(:)인지 궁굼하다면 파이썬을 만든 귀도에게 직접 물어봐야 할 것이다.
# 앞으로 리뷰해볼 while이나 for, def, class문에도 문장의 끝에 콜론(:)이 항상 들어간다.
# 초보자들은 이 콜론(:)을 빠뜨리는 경우가 많으니 특히 주의하자.

# 파이썬이 다른 언어보다 보기 쉽고 소스 코드가 간결한 이유는 바로 콜론(:)을 사용하여 들여쓰기(indentation)을 하도록 만들었기 떄문이다.
# 하지만 이는 숙련된 프로그래머들이 파이썬을 처음 접할 때 제일 혼란스러워 하는 부분이기도 하다. 다른 언어에서는 if문을 { }기호로 감싸지만 파이썬에서는 들여쓰기로 해결한다는 점을 기억하자.
# 참고로 나는 학부때 산업경영공학을 전공했는데, 웹프로그래밍, java등도 다뤄보긴 하였으나, 본격적인 프로그래밍은 파이썬을 이용한 데이터분석으로 시작해서그런지 파이썬이 가장 편하고 친숙하다.

# 조건문이란 무엇인가?
# if 조건문에서 "조건문"이란 참과 거짓을 판단하는 문장을 말한다.
# 앞에서 살펴본 택시 예제에서 조건문은 money가 된다.
moeny = True
if moeny:
    print("참입니다")

# 위 예제의 경우, money는 True이기 떄문에 조건이 참이 되어 if문 다음 문장을 수행한다.

# 비교연산자
# 이번에는 조건문에 비교연산자 (<, >, ==, !=, >=, <=)를 쓰는 방법에 대해 알아보자.
# 다음 표는 비교연산자를 잘 설명해 준다.

# 비교연산자	설명
# x < y	x가 y보다 작다
# x > y	x가 y보다 크다
# x == y	x와 y가 같다
# x != y	x와 y가 같지 않다
# x >= y	x가 y보다 크거나 같다
# x <= y	x가 y보다 작거나 같다

# 이제 위 연산자를 어떻게 사용하는지 알아보자.
x = 3
y = 2
print(x > y)

# x에 3을, y에 2를 대입한 다음 x > y 라는 조건문을 수행하면 True를 돌려준다. x > y 조건문이 참이기 때문이다.
print(x < y)
# 위 조건문은 거짓이기 떄문에 False를 돌려준다.
print(x == y)
# x와 y는 같지 않다. 따라서 위 조건문은 거짓이다.
print(x != y)
# x와 y는 같지 않다. 따라서 위 조건문은 참이다.
# 앞에서 살펴본 택시 에제를 다음처럼 바꾸려면 어떻게 해야 할까?

# 만약 3000원 이상의 돈을 가지고 있으면 택시를 타고 그렇지 않으면 걸어 가라."

# 위 상황은 다음처럼 프로그래밍 할 수 있다.
money = 2000
if money >= 3000:
    print("택시를 타고 가라")
else:
    print("걸어가라")

# 위 예제를 보면 돈이 2000원인데, 참이되는 조건은 money >= 3000이기 떄문에 False로 판정되어 else문 다음 문장을 수행하게 된다.

# and, or not
# 조건은 판단하기 위해 사용하는 다른 연산자로는 and, or, not이 있다. 각각의 연산자는 다음처럼 동작한다.

# 연산자	설명
# x or y	x와 y 둘중에 하나만 참이어도 참이다
# x and y	x와 y 모두 참이어야 참이다
# not x	x가 거짓이면 참이다

# 다음 예를 통해 or 연산자의 사용법을 알아보자.
# "돈이 3000원 이상 있거나 카드가 있다면 택시를 타고 그렇지 않으면 걸어 가라."
money = 2000
card = True
if money >= 3000 or card:
    print("택시를 타고 가라")
else:
    print("걸어가라")
# money는 2000이지만 card가 True이기 때문에 money >= 3000 or card 조건문이 참이 된다. 따라서 if문 다음 "택시를 타고 가라" 문장이 출력된다.

# x in s, x not in s
# 더 나아가 파이썬은 다른 프로그래밍 언어에서 쉽게 볼 수 없는 재미있는 조건문을 제공한다.
# 바로다음과 같은 것들이다.

# in	not in
# x in 리스트	x not in 리스트
# x in 튜플	x not in 튜플
# x in 문자열	x not in 문자열

# 영어 단어 in의 뜻이 "~안에"라는 것을 생각해 보면 다음 예가 쉽게 이해될 것이다.
print(1 in [1, 2, 3])
print(1 not in [1, 2, 3])
# 앞에서 첫 번째 예는 "[1, 2, 3]이라는 리스트 안에 1이 있는가?" 조건문 이다.
# 1은 [1, 2, 3]안에 있으므로 참이 되어 True를 돌려준다.
# 두 번째 예는 "[1, 2, 3] 리스트 안에 1이 없는가?" 조건문이다.
# 1은 [1, 2, 3]안에 있으므로 거짓이 되어 False를 돌려준다.

# 다음은 튜플과 문자열에 적용한 예이다. 각각의 결과가 나온 이유는 쉽게 유추 할 수 있다.
print('a' in ('a', 'b', 'c'))
print('j' not in 'python')

# 이번에는 우리가 계속 사용해 온 택시 예제에 in을 적용해 보자.

# "만약 주머니에 돈이 있으면 택시를 타고, 없으면 걸어 가라."
pocket = ['paper', 'cellphone', 'money']
if 'money' in pocket:
    print('택시를 타고 가라')
else:
    print("걸어가라")
# ['paper', 'cellphone', 'money'] 리스트 안에 'money'가 있으므로 'money' in pocket은 참이 된다. 따라서 if문 다음 문장이 수행된다.

# [조건문에서 아무 일도 하지 않게 설정하고 싶다면?]
# 가끔 조건문의 참, 거짓에 따라 실행할 행동을 정의할 때, 아무런 일도 하지 않도록 설정하고 싶을 때가 있다.

# 다음 예를 보자.
# "주머니에 돈이 있으면 가만히 있고 주머니에 돈이 없으면 카드를 꺼내라."

# 이럴 때 사용하는 것이 바로 pass이다. 위 예를 pass를 적용해서 구현해 보자.
pocket = ['paper', 'money', 'cellphone']
if 'money' in pocket:
    pass
else:
    print("카드를 꺼내라")
# pocket 리스트 안에 money 문자열이 있기 때문에 if문 다음 문장인 pass가 수행되고 아무 결괏값도 보여 주지 않는다.

# 다양한 조건을 판단하는 elif
# if와 else만으로는 다양한 조건을 판단하기 어렵다. 다음 예를 보더라도 if와 else만으로는 조건을 판단하는 데 어려움 겪게 된다.

# "주머니에 돈이 있으면 택시를 타고, 주머니에 돈은 없지만 카드가 있으면 택시를 타고, 돈도 없고 카드도 없으면 걸어 가라."

# 위 문장을 보면 조건을 판단하는 부분이 두 군데가 있다. 먼저 돈이 있는지를 판단해야 하고, 주머니에 돈이 없으면 다시 카드가 있는지 판단해야 한다.

# if 와 else만으로 위 문장을 표현하려면 다음과 같이 할 수 있다.
pocket = ['paper', 'handphone']
card = True
if 'money' in pocket:
    print('택시를 타고 가라')
else:
    if card:
        print("택시를 타고 가라")
    else:
        print("걸어가라")
# 언뜻 보기에도 이해하기 어렵고 산만한 느낌이 든다. 이런 복잡함을 해결하기 위해 파이썬에서는 다중 조건 판단을 가능하게 하는 elif를 사용한다.
# 위 예를 elif를 사용하면 다음과 같이 바꿀 수 있다.
pocket = ['papaer', 'cellphone']
card = True
if 'money' in pocket:
    print("택시를 타고 가라")
elif card:
    print("택시를 타고 가라")
else:
    print("걸어가라")
# 즉 elif는 이전 조건문이 거짓일 때 수행된다. if, elif, else를 모두 사용할 때 기본 구조는 다음과 같다.

# If <조건문>:
#     <수행할 문장1>
#     <수행할 문장2>
#     ...
# elif <조건문>:
#     <수행할 문장1>
#     <수행할 문장2>
#     ...
# elif <조건문>:
#     <수행할 문장1>
#     <수행할 문장2>
#     ...
# ...
# else:
#    <수행할 문장1>
#    <수행할 문장2>
#    ...

# 위에서 볼 수 있듯이 elif는 개수에 제한 없이 사용할 수 있다.

# [if문을 한 줄로 작성하기]
# 앞의 pass를 사용한 예를 보면 if문 다음에 수행할 문장이 한 줄이고, else문 다음에 수행할 문장도 한 줄밖에 되지 않는다.
if 'money' in pocket:
    pass
else:
    print('카드를 꺼내라')
# 이렇게 수행할 문장이 한 줄일 때 조금 더 간략하게 코드를 작성하는 방법이 있다.
pocket = ['paper', 'money', 'cellphone']
if 'money' in pocket: pass
else: print("카드를 꺼내라")
# if문 다음 수행할 문장을 콜론(:)뒤에 바로 적어 주었다. else문 역시 마찬가지이다.

# 조건부 표현식
# 다음과 같은 코드를 보자.
score = 99
if score >= 60:
    message = 'soccess'
else:
    message = "falure"
print(message)
# 위 코드는 score가 60 이상일 경우 message에 문자열 "success'를, 아닐 경우에는 'failure'를 대입하는 코드이다.
# 파이썬의 조건부 표현식(conditional expression)을 사용하면 위 코드를 다음과 같이 간단히 표현할 수 있다.
message = "success" if score >= 60 else "failure"
print(message)
# 조건부 표현식은 다음과 같이 정의한다.
# 조건문이 참인 경우 if 조건문 else 조건문이 거짓인 경우

# 조건부 표현식은 가독성에 유리하고 한 줄로 작성할 수 있어 활용성이 좋다.

# Review complete