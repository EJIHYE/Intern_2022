"""
n개의 정수(n>0)로 이루어진 수열에 대해 서로 인접해 있는 두 수의 차가
1에서 n-1까지의 값을 모두 가지면 그 수열을 유쾌한 점퍼(jolly jumper)라고 부른다.
예를 들어 다음과 같은 수열에서
1 4 2 3
앞 뒤에 있는 숫자 차의 절대 값이 각각 3,2,1이므로 이 수열은 유쾌한 점퍼가 된다. 어떤 수열이 유쾌한 점퍼인지 판단할 수 있는 프로그램을 작성하라.

Input : 각 줄 맨 앞에는 3000 이하의 정수가 있으며 그 뒤에는 수열을 나타내는 n개의 정수가 입력된다. 맨 앞 숫자가 0이면 출력하고 종료한다.
output : 입력된 각 줄에 대해 "Jolly" 또는 "Not Jolly"를 한 줄씩 출력한다

[Sample Input] ※ 주의: 각 줄의 맨 앞의 숫자는 수열의 갯수이다. 첫번째 입력인 4 1 4 2 3 의 맨 앞의 4는 뒤에 4개의 숫자가 온다는 것을 의미함
4 1 4 2 3
5 1 4 2 -1 6

[Sample Output]
Jolly
Not jolly
"""
"""
=============================================================================
과제 1. 수열이 유쾌한 점퍼인지 판단할 수 있는 프로그램을 작성하라.
       input = ["4 1 4 2 3", "5 1 3 2 -1 6"]
       출력 : Jolly
             Not Jolly
=============================================================================
"""

def do(xs):     # jolly 여부를 판단하는 함수
    return (abs(x[0] - x[1]) for x in zip(xs, xs[1:])) == set(range(1, len(xs))) # 인접한 두수의 차
                # jolly jump 인 값은  1, 2, 3, ..., n - 1 이기 때문에 set과 비교
                # abs(x[0] - x[1]) -> (x의 첫번째 수)와 (x의 두번째 수)의 차
                # 1부터 xs-1 까지의 집합
                # [:] : 문자열 반복 연산자
                # [1:] : 맨마지막 값 생략, 지정된 글자(1)부터 끝까지
data = []

while len(data) < 2 :
    i = [int(x) for x in input().split()]
    if i[0] == 0:
        break
    data.append(i[1:])              # i의 2번째 값부터부터 끝까지 데이터에 추가

for d in data:
    if do(d):
        print("Jolly")
    else:
        print("Not Jolly")
        
"""
=============================================================================
과제 2. 수열이 jolly jumper인지 판단할 수 있는 프로그램을 작성하시오.
       input = ["4 1 4 2 3", "5 1 3 2 -1 6", "0"]
       출력 : Jolly
             Not Jolly
             0
=============================================================================
"""

def do(xs):
    return (abs(x[0] - x[1]) for x in zip(xs, xs[1:])) == set(range(1, len(xs)))

data = []

while True:
    i = [int(x) for x in input().split()]
    if i[0] == 0:
      data.append('0')
      break
    data.append(i[1:])              

for d in data:
    if d != '0' :
        if do(d):
           print("Jolly")
        else :
            print("Not Jolly")
    else :
        print('0')
