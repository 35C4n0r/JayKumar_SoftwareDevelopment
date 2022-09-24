from collections import Counter
for i in range(int(input())):
    
    s = input()
    if '"'in s:
        s = s.replace('"', "")
    s = list(s)
    arr2 = Counter(s)
    z = 0
    ans = ""
    arr = {0: Counter(list("zero")), 1: Counter(list("one")), 2: Counter(list("two")), 3: Counter(list("three")),4: Counter(list("four")),5: Counter(list("five")),6: Counter(list("six")),7: Counter(list("seven")),8: Counter(list("eight")),9: Counter(list("nine")),10: Counter(list("ten"))}
    # print(arr)
    while True:
        if z == 0:
            a = 1
        else:
            a = 0
        z += 1
        atLeastOnce = False
        for i in range(a, 9):
            can = True
            for k in arr[i]:
                if arr[i][k] > arr2[k]:
                    can = False
                    break
            if can:
                atLeastOnce = True
                ans += str(i)
                for k in arr[i]:
                    arr2[k] -= arr[i][k]
                break
        if atLeastOnce == False:
            break
    print(ans)
            
