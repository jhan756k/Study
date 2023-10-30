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
        double[] tmp = myElements[r1];
        myElements[r1] = myElements[r2];
        myElements[r2] = tmp;
    }

    public MyMatrix solveMatrix(MyMatrix sol) {
        
        // Augmented Matrix 생성
        MyMatrix res = new MyMatrix("sol", numRows, numCols + 1, 0.0);

        for (int i = 0; i < numRows; i++) {
            for (int j = 0; j < numCols; j++) {
                res.setVal(i, j, myElements[i][j]);
            }
        }

        for (int i = 0; i < numRows; i++) {
            res.setVal(i, numCols, sol.getVal(i, 0));
        }
        
        // Gaussian Elimination
        double lead, prev;
        for (int r = 0; r < numRows; r++) { // 각 행마다 돌아가면서 대각으로 만들기
            while (res.getVal(r, r) == 0) {
                for (int i = r + 1; i < numRows; i++) {
                    if (res.getVal(i, r) != 0) {
                        res.swapRows(r, i);
                        break;
                    }
                }
            }
            
            if (r != 0) { // 첫 행이 아닌 경우
                for (int x = 0; x < r; x++) { // 대각선 아래 행들을 0으로 만들기
                    lead = res.getVal(r, x);
                    prev = res.getVal(x, x);
                    if (lead == 0 || prev == 0) continue;
                    
                    for (int y = 0; y < numCols + 1; y++) { // 각 행의 원소들을 계산
                        res.setVal(r, y, res.getVal(r, y) - ((lead/prev) * res.getVal(x, y)));
                    }
                }
            }
        }
        return res;
    }

    public boolean checkMult(MyMatrix res, MyMatrix div) {
        MyMatrix tmp = res.multMatrix(div);
        for (int i = 0; i < numRows; i++) {
            for (int j = 0; j < numCols; j++) {
                // System.out.println(Math.abs(tmp.getVal(i, j) - myElements[i][j]));
                if (Math.abs(tmp.getVal(i, j) - myElements[i][j]) > 0.0001) {
                    return false;
                }
            }
        }
        return true;
    }
}