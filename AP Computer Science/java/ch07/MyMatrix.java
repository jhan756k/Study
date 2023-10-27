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

    public void setMatrix(double[][] val) {
        numRows = val.length;
        numCols = val[0].length;
        for (int i = 0; i < numRows; i++) {
            for (int j = 0; j < numCols; j++) {
                myElements[i][j] = val[i][j];
            }
        }
    }

    public void printMatrix() {
        System.out.println("Matrix: " + myName);
        for (int i = 0; i < numRows; i++) {
            System.out.print("[");
            for (int j = 0; j < numCols; j++) {
                System.out.print(Math.round(myElements[i][j]*1000)/1000.0);
                if (j < numCols - 1) {
                    System.out.print(", ");
                }
            }
            System.out.println("]");
        }
        System.out.println();
    }

    public MyMatrix addMatrix(MyMatrix m) {
        if (numRows != m.numRows || numCols != m.numCols) {
            System.out.println("두 행렬의 크기가 다릅니다.");
            return null;
        }
        for (int i = 0; i < numRows; i++) {
            for (int j = 0; j < numCols; j++) { 
                myElements[i][j] += m.myElements[i][j];
            }
        }
        return m;
    }

    public MyMatrix subtractMatrix(MyMatrix m) {
        if (numRows != m.numRows || numCols != m.numCols) {
            System.out.println("두 행렬의 크기가 다릅니다.");
            return null;
        }
        for (int i = 0; i < numRows; i++) {
            for (int j = 0; j < numCols; j++) { 
                myElements[i][j] -= m.myElements[i][j];
            }
        }
        return m;
    }

    public MyMatrix multMatrix(MyMatrix m) {
        if (numCols != m.numRows) {
            System.out.println("두 행렬은 곱할 수 없는 크기입니다.");
            return null;
        }
        MyMatrix result = new MyMatrix(myName + " x " + m.myName, numRows, m.numCols, 0.0);
        for (int i = 0; i < numRows; i++) {
            for (int j = 0; j < m.numCols; j++) {
                for (int k = 0; k < numCols; k++) {
                    result.myElements[i][j] += myElements[i][k] * m.myElements[k][j];
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
                            subMatrix.myElements[j - 1][k] = myElements[j][k];
                        }
                        else if (k > i) {
                            subMatrix.myElements[j - 1][k - 1] = myElements[j][k];
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
                result.myElements[j][i] = myElements[i][j];
            }
        }
        return result;
    }

    public MyMatrix subMatrix(int i, int j) {
        MyMatrix result = new MyMatrix(myName + "S", numRows - 1, numCols - 1, 0.0);
        for (int k = 0; k < numRows; k++) {
            for (int l = 0; l < numCols; l++) {
                if (k < i && l < j) {
                    result.myElements[k][l] = myElements[k][l];
                }
                else if (k < i && l > j) {
                    result.myElements[k][l - 1] = myElements[k][l];
                }
                else if (k > i && l < j) {
                    result.myElements[k - 1][l] = myElements[k][l];
                }
                else if (k > i && l > j) {
                    result.myElements[k - 1][l - 1] = myElements[k][l];
                }
            }
        }
        return result;
    }

    public MyMatrix adjointMatrix() {
        MyMatrix cof = new MyMatrix("Inverse of mult", numRows, numCols, 0.0);
        for (int i = 0; i < numRows; i++) {
            for (int j = 0; j < numRows; j++) {
                cof.myElements[i][j] = subMatrix(i, j).determinant() * Math.pow(-1.0, i + j);
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
                x.myElements[i][j] *= detinv;
                if (x.myElements[i][j] == -0.0) {
                    x.myElements[i][j] = 0.0;
                }
            }
        }
        return x;
    }

    public MyMatrix divideMatrix(MyMatrix m) {
        return multMatrix(m.inverseMatrix());
    }
}