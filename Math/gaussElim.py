import sys
import numpy as np

def gauss(A,x):
    n = len(A)
    # 입력받은 행렬 A 의 크기만큼 loop을 돌면서,
    for i in range(n):
    	# A[i][i] 가 같게되면 가우스 소거법이 불가능한 행렬로, division error 수행
        if a[i][i] == 0.0:
            sys.exit('Divide by zero detected!')
        # i+1열의 A에 대해 i행과 j행의 비율을 구해 준후, 그 ratio만큼을 j-i*ratio 해준다.
        # 결과는 A[i][i] 좌측의 행 전부 0이 되게 된다.
        for j in range(i+1, n):
            ratio = A[j][i]/A[i][i]
            for k in range(n+1):
                A[j][k] -=ratio*A[i][k]
                
    # A 를 구해주고, 맨끝 X[n-1] == A[n-1][n]/A[n-1][n-1] 취해준다.
    x[n-1] = A[n-1][n]/A[n-1][n-1]
    for i in range(n-2,-1,-1):
    	# x[i] 를 구하기 위해 back substitution 시행
        x[i]=A[i][n]
        for j in range(i+1,n):
            x[i] = x[i] - A[i][j]*x[j]
        x[i] = x[i]/a[i][i]
        
    return [A,x]

a = [[2,1,-1,8],[-3,-1,2,-11],[-2,1,2,-3]]

a=np.array(a)
a =a.astype(float)
x = np.zeros(len(a))

a,b = gauss(a,x)
print(a)
print(b)