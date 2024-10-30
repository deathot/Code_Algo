class Solution:
    def getSmallestString(self, s: str) -> str:

        t = list(s)
        
        for i in range(1, len(t)):
            x, y = t[i - 1], t[i]
            if x > y and ord(x) % 2 == ord(y) % 2:
                t[i - 1], t[i] = y, x
                break
        return ''.join(t)

s = "12345"
t = list(s)
print(f"list(s) = {t}")
x = t[1]
y = '7'
x1 = ord(y) % 2 
print(f"x = {x}, x1 = {x1}, y = {y}")
t[0], t[1] = t[1], t[0]
print(''.join(t))

for i in range(0, 10):
    print(i)

    for j in range(0, 9):
        print("ok")
        if i == 3:
            print(i)
            break