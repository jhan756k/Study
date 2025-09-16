import random

# a[4] < 244
# a[6] < 244
# a[7] = 244

a = [5, 16, 21, 47, 130, 185, 186, 244, 344]
x = 244

start = 0 
end = len(a) - 1

while start <= end:
    mid = (start + end) // 2
    if a[mid] == x:
        print("찾았다!: " + str(mid))
        break
    elif a[mid] < x:
        start = mid + 1
    else:
        end = mid - 1

# found = False

# for i in range(0, len(a)):
#     if a[i] == x:
#         print(i)
#         found = True
#         break

# if not found:
#     print("숫자가 없습니다")
