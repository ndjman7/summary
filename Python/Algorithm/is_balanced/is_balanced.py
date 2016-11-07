test = input()
ans = [0,0]
def is_balanced(test,ans):
    for i in test:
        if i == '(':
            ans[0] += 1
        elif i == ')':
            ans[1] += 1
        if ans[1] > ans[0]:
            return False

    if ans[0] == ans[1]:
        return True
    else:
        return False

print(is_balanced(test,ans))
