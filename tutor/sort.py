# 정렬

# 1. bubble sort
# 2. selection sort
# 3. merge sort --> 재귀

a = [2, 3, 53, 6, 12, 21, 43, 123]

# 버블정렬
a = [2, 3, 53, 6, 12, 21, 17, 123]
a= [2, 3, 6, 12, 21, 17, 53, 123]

b = [123, 12, 25, 15]
b = [12, 25, 15, 123]

for b in range(len(a)-1):
    for c in range(len(a)-b-1):
        if a[c] > a[c+1]:
            a[c],a[c+1] = a[c+1],a[c]


# Selection sort

for b in range(len(a)):
    max_idx = b
    for c in range(b+1, len(a)):
        if a[c] > a[max_idx]:
            max_idx = c
    a[max_idx],a[b] = a[b],a[max_idx]


