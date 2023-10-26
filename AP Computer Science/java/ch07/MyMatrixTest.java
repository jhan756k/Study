package ch07;
import chn.util.*;

public class MyMatrixTest {
    public static void main(String[] args)   {
        FileInput io = new FileInput("ch07\\matrix.txt");
        String name = io.readLine();
        int rows = io.readInt();
        int cols = io.readInt();
        double val[][] = new double[rows][cols];
        for (int i = 0; i < rows; i++)   {
            for (int j = 0; j < cols; j++)   {
                val[i][j] = io.readDouble();
            }
        }

        MyMatrix test = new MyMatrix(name, 3, 4, 0);
        test.setMatrix(val);
        test.printMatrix();
        
        System.out.println(test.determinant());

        // MyMatrix A = new MyMatrix("A", 3, 4, 1.0);
        // A.printMatrix();

        // MyMatrix B = new MyMatrix("B", 4, 4, 2.0);
        // B.printMatrix();

        // MyMatrix x = A.multMatrix(B);
        // x.printMatrix();

        // MyMatrix sq = new MyMatrix("sq", 3, 3, 3.0);
        // sq.printMatrix();
    }
}