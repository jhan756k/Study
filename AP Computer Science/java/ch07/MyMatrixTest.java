package ch07;
import chn.util.*;

public class MyMatrixTest {
    public static void main(String[] args)   {
        FileInput io = new FileInput("ch07\\matrix1.txt");
        int rows = io.readInt();
        int cols = io.readInt();
        double val[][] = new double[rows][cols];
        for (int i = 0; i < rows; i++)   {
            for (int j = 0; j < cols; j++)   {
                val[i][j] = io.readDouble();
            }
        }

        MyMatrix m1 = new MyMatrix("m1", rows, cols, 0);
        m1.setMatrix(val);

        io = new FileInput("ch07\\matrix2.txt");
        rows = io.readInt();
        cols = io.readInt();
        double val2[][] = new double[rows][cols];
        for (int i = 0; i < rows; i++)   {
            for (int j = 0; j < cols; j++)   {
                val2[i][j] = io.readDouble();
            }
        }

        MyMatrix m2 = new MyMatrix("m2", rows, cols, 0);
        m2.setMatrix(val2);
    
        // MyMatrix res = new MyMatrix();
        // res = m1.divideMatrix(m2);
        // Boolean check = m1.checkMult(res, m2);

        // m1.printMatrix();
        // m2.printMatrix();
        // res.printMatrix();
        // System.out.println(check);

        MyMatrix res = m1.multMatrix(m2);

        m1.printMatrix();
        m2.printMatrix();
        res.printMatrix();
    }
}