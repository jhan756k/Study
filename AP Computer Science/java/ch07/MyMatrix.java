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
                System.out.print(myElements[i][j]);
                if (j < numCols - 1) {
                    System.out.print(", ");
                }
            }
            System.out.println("]");
        }
    }

    public MyMatrix addMatrix(MyMatrix m) {
        if (numRows != m.numRows || numCols != m.numCols) {
            System.out.println("Error: cannot add matrices of different sizes");
            return null;
        }
        for (int i = 0; i < numRows; i++) {
            for (int j = 0; j < numCols; j++) { 
                myElements[i][j] += m.myElements[i][j];
            }
        }
        return m;
    }

    public MyMatrix subMatrix(MyMatrix m) {
        if (numRows != m.numRows || numCols != m.numCols) {
            System.out.println("Error: cannot subtract matrices of different sizes");
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
            System.out.println("Error: cannot multiply matrices of these sizes");
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
            System.out.println("Error: cannot compute determinant of a non-square matrix");
            return 0.0;
        }
        if (numRows == 1) {
            return myElements[0][0];
        }
        else {
            double det = 0.0;
            for (int i = 0; i < numRows; i++) {
                MyMatrix subMatrix = new MyMatrix(myName + " sub " + i, numRows - 1, numCols - 1, 0.0);
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
}