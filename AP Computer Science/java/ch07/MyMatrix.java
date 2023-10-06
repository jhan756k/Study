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
            return;
        }
        for (int i = 0; i < numRows; i++) {
            for (int j = 0; j < numCols; j++) { 
                myElements[i][j] += m.myElements[i][j];
            }
        }
    }

    public MyMatrix subMatrix(MyMatrix m) {
        if (numRows != m.numRows || numCols != m.numCols) {
            System.out.println("Error: cannot subtract matrices of different sizes");
            return;
        }
        for (int i = 0; i < numRows; i++) {
            for (int j = 0; j < numCols; j++) { 
                myElements[i][j] -= m.myElements[i][j];
            }
        }
    }
}