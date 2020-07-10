from itertools import permutations
def permutationEquation(p):
    maxi = max(p)
    mini = min(p)
    per = permutations(p)
    for i in list(p):
        p[i] = i
    # for j in range(1,n):
    #     if j


if __name__ == '__main__':
    n = int(input())

    p = list(map(int, input().rstrip().split()))
    permutationEquation(p)
