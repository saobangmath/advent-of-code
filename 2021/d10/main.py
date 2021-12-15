d = {')' : 3, ']' : 57, '}' : 1197, '>' : 25137}
dd = {')' : 1, ']' : 2, '}' : 3, '>' : 4}

def f1(s):
    stack = []
    for _ in s:
        if _ in "({[<":
            stack.append(_)
        if _ == ')':
            if stack[-1]!='(':
                return d[_]
            stack.pop()
        if _ == '}':
            if stack[-1]!='{':
                return d[_]
            stack.pop()
        if _ == '>':
            if stack[-1]!='<':
                return d[_]
            stack.pop()
        if _ == ']':
            if stack[-1]!='[':
                return d[_]
            stack.pop()
    return 0

def f2(s):
    stack = []
    for _ in s:
        if _ in "({[<":
            stack.append(_)
        if _ == ')':
            if stack[-1] != '(':
                return d[_]
            stack.pop()
        if _ == '}':
            if stack[-1] != '{':
                return d[_]
            stack.pop()
        if _ == '>':
            if stack[-1] != '<':
                return d[_]
            stack.pop()
        if _ == ']':
            if stack[-1] != '[':
                return d[_]
            stack.pop()
    tot=0
    while stack:
        tot = tot*5
        if stack[-1] == '(': tot+=1
        if stack[-1] == '[': tot+=2
        if stack[-1] == '{': tot+=3
        if stack[-1] == '<': tot+=4
        stack.pop()
    return tot

def main():
    tot1 = 0
    l = []
    with open('input.txt.txt') as f:
        for x in f:
            if x[-1]=='\n': x = x[:-1:]
            t = f1(x)
            if t>0:
                tot1+=t
            else:
                l.append(f2(x))
    l.sort()
    print(l)
    print(tot1, l[len(l) // 2])
    pass


main()