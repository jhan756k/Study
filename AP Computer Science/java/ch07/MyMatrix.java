package ch07;

public class MyMatrix {
    private String myName;
    private int numRows;
    private int numCols;
    private double[][] myElements;

    public MyMatrix() {
        myName = "name";
        numRows = 10;
        numCols = 10;
        myElements = new double[numRows][numCols];
    }

    public MyMatrix(String name, int nR, int nC, double val) {
        myName = name;
        numRows = nR;
        numCols = nC;
        myElements = new double[numRows][numCols];
        for (int i = 0; i < numRows; i++) {
            for (int j = 0; j < numCols; j++) {
                myElements[i][j] = val;
            }
        }
    }   
    
    public MyMatrix(int n, double v) {
        myName = "identity matrix";
        numRows = n;
        numCols = n;
        myElements = new double[numRows][numCols];
        for (int i = 0; i < numRows; i++) {
            for (int j = 0; j < numCols; j++) {
                if (i == j) {
                    myElements[i][j] = v;
                }
            }
        }
    };

    public void setMatrix(double[][] val) {
        numRows = val.length;
        numCols = val[0].length;
        for (int i = 0; i < numRows; i++) {
            for (int j = 0; j < numCols; j++) {
                myElements[i][j] = val[i][j];
            }
        }
    }

    public void setVal(int i, int j, double v) {
        myElements[i][j] = v;
    }

    public double getVal(int i, int j) {
        return myElements[i][j];
    }

    public int getNumRows() {
        return numRows;
    }

    public int getNumCols() {
        return numCols;
    }

    public String getName() {
        return myName;
    }

    public void printMatrix() {
        System.out.println("Matrix: " + myName);
        for (int i = 0; i < numRows; i++) {
            System.out.print("[");
            for (int j = 0; j < numCols; j++) {
                if (myElements[i][j] == -0.0) System.out.print(0.0);
                else System.out.print(Math.round(myElements[i][j]*1000)/1000.0);
                if (j < numCols - 1) System.out.print(", ");
            }
            System.out.println("]");
        }
        System.out.println();
    }

    public MyMatrix addMatrix(MyMatrix m) {
        if (numRows != m.getNumRows()  || numCols != m.getNumCols()) {
            System.out.println("두 행렬의 크기가 다릅니다.");
            return null;
        }
        for (int i = 0; i < numRows; i++) {
            for (int j = 0; j < numCols; j++) { 
                myElements[i][j] += m.getVal(i, j);
            }
        }
        return m;
    }

    public MyMatrix subtractMatrix(MyMatrix m) {
        if (numRows != m.getNumRows() || numCols != m.getNumCols()) {
            System.out.println("두 행렬의 크기가 다릅니다.");
            return null;
        }
        for (int i = 0; i < numRows; i++) {
            for (int j = 0; j < numCols; j++) { 
                myElements[i][j] -= m.getVal(i, j);
            }
        }
        return m;
    }

    public MyMatrix multMatrix(MyMatrix m) {
        if (numCols != m.getNumRows()) {
            System.out.println("두 행렬은 곱할 수 없는 크기입니다.");
            return null;
        }
        MyMatrix result = new MyMatrix(myName + " x " + m.getName(), numRows, m.getNumCols(), 0.0);
        for (int i = 0; i < numRows; i++) {
            for (int j = 0; j < m.getNumCols(); j++) {
                for (int k = 0; k < numCols; k++) {
                    result.setVal(i, j, result.getVal(i, j) + myElements[i][k] * m.getVal(k, j));
                }
            }
        }
        return result;
    }

    public double determinant() {
        if (numRows != numCols) {
            System.out.println("square matrix가 아닙니다.");
            return 0.0;
        }
        if (numRows == 1) {
            return myElements[0][0];
        }
        else {
            double det = 0.0;
            for (int i = 0; i < numRows; i++) {
                if (myElements[0][i] == 0.0) {
                    continue;
                };
                MyMatrix subMatrix = new MyMatrix("sub", numRows - 1, numCols - 1, 0.0);
                for (int j = 1; j < numRows; j++) {
                    for (int k = 0; k < numRows; k++) {
                        if (k < i) {
                            subMatrix.setVal(j-1, k, myElements[j][k]);
                        }
                        else if (k > i) {
                            subMatrix.setVal(j-1, k-1, myElements[j][k]);
                        }
                    }
                }
                det += Math.pow(-1.0, i) * myElements[0][i] * subMatrix.determinant();
            }
            return det;
        }
    }

    public MyMatrix transpose() {
        MyMatrix result = new MyMatrix(myName, numCols, numRows, 0.0);
        for (int i = 0; i < numRows; i++) {
            for (int j = 0; j < numCols; j++) { 
                result.setVal(j, i, myElements[i][j]);
            }
        }
        return result;
    }

    public MyMatrix subMatrix(int i, int j) {
        MyMatrix result = new MyMatrix(myName + "S", numRows - 1, numCols - 1, 0.0);
        for (int k = 0; k < numRows; k++) {
            for (int l = 0; l < numCols; l++) {
                if (k < i && l < j) {
                    result.setVal(k, l, myElements[k][l]);
                }
                else if (k < i && l > j) {
                    result.setVal(k, l - 1, myElements[k][l]);
                }
                else if (k > i && l < j) {
                    result.setVal(k - 1, l, myElements[k][l]);
                }
                else if (k > i && l > j) {
                    result.setVal(k - 1, l - 1, myElements[k][l]);
                }
            }
        }
        return result;
    }

    public MyMatrix adjointMatrix() {
        MyMatrix cof = new MyMatrix("Inverse of mult", numRows, numCols, 0.0);
        for (int i = 0; i < numRows; i++) {
            for (int j = 0; j < numRows; j++) {
                cof.setVal(i, j, subMatrix(i, j).determinant() * Math.pow(-1.0, i + j));
            }
        }
        MyMatrix adj = cof.transpose();

        return adj;
    }

    public MyMatrix inverseMatrix() {
        if (determinant() == 0.0) {
            System.out.println("singular matrix입니다");
            return null;
        }
        double detinv = 1.0 / determinant();
        MyMatrix x = adjointMatrix();

        for (int i = 0; i < numRows; i++) {
            for (int j = 0; j < numRows; j++) {
                x.setVal(i, j, x.getVal(i, j) * detinv);
            }
        }
        return x;
    }

    public MyMatrix divideMatrix(MyMatrix m) {
        return multMatrix(m.inverseMatrix());
    }

    public void swapRows(int r1, int r2) {
        if (r1 == r2) return;
        double[] tmp = myElements[r1];
        myElements[r1] = myElements[r2];
        myElements[r2] = tmp;
    }

    public MyMatrix[] gaussianElimination(MyMatrix sol) {
        
        // Augmented Matrix 생성
        MyMatrix res = new MyMatrix("ref", numRows, numCols + sol.numCols, 0.0);
        MyMatrix x = new MyMatrix("sol", numCols, sol.numCols, 0.0);
        for (int i = 0; i < numRows; i++) {
            for (int j = 0; j < numCols; j++) {
                res.setVal(i, j, myElements[i][j]);
            }
        }

        for (int i = 0; i < sol.numRows; i++) {
            for (int j = 0; j < sol.numCols; j++) {
                res.setVal(i, numCols + j, sol.getVal(i, j));
            }
        }

        // Gaussian Elimination
        double ratio;
        for (int i = 0; i < numRows; i++) { // 각 행 돌면서 
            for (int j = i + 1; j < numRows; j++) { // 그 밑 행들중
                if (res.getVal(i, i) == 0) { // 대각선 원소가 0이면
                    for (int k = i + 1; k < numRows; k++) { // 아닌거 찾을때까지 for
                        if (res.getVal(k, i) != 0) { 
                            res.swapRows(i, k);
                            break;
                        }
                        if (k == numRows - 1) { // 다돌았는데도 못찾으면 singular matrix or infinite solutions
                            System.out.println("해를 구할 수 없습니다.");
                            return null;
                        }
                    }
                }
                ratio = res.getVal(j, i) / res.getVal(i, i); // 대각행마다 아래 원소 0 만듬
                for (int k = 0; k < numCols + sol.numCols; k++) { // 각 행의 원소들을 계산
                    res.setVal(j, k, res.getVal(j, k) - ratio * res.getVal(i, k));
                }
            }
        }  

        // Back Substitution
        for (int i = 0; i < sol.numCols; i++) {
            for (int j = numRows - 1; j >= 0; j--) {
                double sum = 0.0;
                for (int k = j + 1; k < numRows; k++) { // 대각선 위 원소들 빼줌
                    sum += res.getVal(j, k) * x.getVal(k, i);
                }
                x.setVal(j, i, (res.getVal(j, numCols + i) - sum) / res.getVal(j, j));
            }
        }

        MyMatrix ret[] = new MyMatrix[2];
        ret[0] = res;
        ret[1] = x;
        return ret;
    }

    public boolean checkMult(MyMatrix res, MyMatrix div) {
        MyMatrix tmp = res.multMatrix(div);
        for (int i = 0; i < numRows; i++) {
            for (int j = 0; j < numCols; j++) {
                if (Math.abs(tmp.getVal(i, j) - myElements[i][j]) > 1e-6) {
                    return false;
                }
            }
        }
        return true;
    }
}