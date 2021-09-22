
# 06-3 게시판 페이징하기
# A 씨는 게시판 프로그램을 작성하고 있다.
# 그런데 게십물의 총 건수와 한 페이지에 보여 줄 게시물 수를 입력으로 주었을 때 페이지 수를 출력하는 프로그램이 필요하다고 한다.

# ※ 이렇게 게시판의 페이지 수를 보여 주는 것을 "페이징"한다고 부른다.

# ● 함수이름은?
# ● 입력받는 값은? 게시물의 총 건수(m), 한 페이지에 보여줄 게시물 수(n)
# ● 출력하는 값은? 총 페이지수

# A씨가 필요한 프로그램을 만들기 위해 입력값과 결과값이 어떻게 나와야 하는지 먼저 살펴보자.
# 게시물의 총 건수가 5이고 한 페이지에서 보여 줄 게시물 수가 10이면 총 페이지 수는 당연히 1이 된다.
# 만약 게시물의 총 건수가 15이고 한 페이지에서 보여 줄 게시물 수가 10이라면 총 페이지 수는 2가 될 것이다.

# 게시물의 총 건수(m)	페이지당 보여줄 게시물 수(n)	총 페이지 수
# 5	10	1
# 15	10	2
# 25	10	3
# 30	10	3

# 이 문제는 게시판 프로그램을 만들 떄 가장 처음 무자추닌 난관이라고 할 수 있는 총 페이지수를 구하는 문제이다.
# 사실 실제 업무에서 사용하는 페이징 기술은 훨씬 복잡한데 여기에서는 그중 가장 간단한 총 페이지 수를 구하는 방법에 대해서만 알아보겠다.

# 1. 다음과 같이 총 건수(m)를 한 페이지에 보여 줄 게시물 수(n)로 나누고 1을 더하면 총 페이지 수를 얻을 수 있다.

# 총 페이지 수 = (총 건수/ 한 페이지당 보여 줄 건수) + 1

# 2.  이러한 공식을 적용했을 경우 총 페이지가 표의 값처럼 구해지는지 확인해 보자(m을 n으로 나눌 때 소수점 아래 자리를 버리기 위해/ 대신 // 연산자를 사용하였다.)

def getTotalPage(m, n):
    return m // n + 1
print(getTotalPage(5, 10)) #1 출력
print(getTotalPage(15, 10)) #2 출력
print(getTotalPage(30, 10)) #3 출력
print(getTotalPage(55, 10)) #4 출력

# 첫 번째, 두 번째, 세 번째 케이스는 공식에 맞게 결과가 출력된다.
# 하지만 세 번째 케이스틑 총 건수가 55이고 한페이지에 보여줄 건수가 10인데 4가 출력되어 실패해 버렸다.
# 잘 생각해 보자.
# 총 건수가 30이고 한페이지에 보여 줄 건수가 10이라면 당연히 총 페이지 수는 3이 되어야 한다.

# 3. 실패 케이스는 총 게시물 수와 한 페이지에 보여 줄 게시물 수를 나눈 나머지 값이 0이 될 때 발생함을 유추할 수 있을 것이다.
# 이 실패 케이스를 해결하려면 다음과 같이 코드를 변경해야 한다.
def getTotalPage2(m, n):
    if m % n == 0:
        return m // n
    else:
        return m // n + 1

print(getTotalPage2(5, 10)) #1 출력
print(getTotalPage2(15, 10)) #2 출력
print(getTotalPage2(30, 10)) #3 출력
print(getTotalPage2(55, 10)) #4 출력

# 나누었을 떄 나머지가 0인 경우는 나누기의 몫만 돌려주고 그 이외의 경우에는 1을 더하여 돌려주도록 변경했다.

# 프로그램을 실행해 보면 모든 케이스가 원하던 결과를 출력함을 확인할 수 있다.

# Review complete.