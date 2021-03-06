import sys
sys.stdin = open("07_input.txt", "rt")

# 소수(에라토스테네스 체 - 소수를 구하는 가장 빠른 알고리즘)
# 자연수 N이 입력되면 1부터 N까지의 소수의 개수를 출력하는 프로그램을 작성하세요. 
# 만약 20이 입력되면 1부터 20까지의 소수는 2, 3, 5, 7, 11, 13, 17, 19로 총 8개입니다.
# 제한시간은 1초입니다.

# 모든 리스트는 초기에 0으로 초기화되어 있음.
# 인덱스 2부터 시작하여, 인덱스 2의 값은 0이므로 소수 카운트 +1을 하고 2의 배수를 모두 1로 표시함.
# 그 다음인 인덱스 3도 0이므로 같은 방법으로 소수 카운트 +1을 하고, 3의 배수를 모두 1로 표시함.
# 인덱스 4는 1이므로 넘어감. 이 과정을 반복한다.

n = int(input())
cnt_list = [0] * (n+2)

num = 0
for i in range(2, n+1):
    if(cnt_list[i] == 0):
        num += 1
        for j in range(i, n+1, i):
            cnt_list[j] = 1

print(num)