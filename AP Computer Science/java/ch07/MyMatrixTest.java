package ch07;
import chn.util.*;

public class MyMatrixTest {
    public static void main(String[] args)   {
        FileInput io = new FileInput("ch07\\matrix.txt");
        int rows = io.readInt();
        int cols = io.readInt();
        double val[][] = new double[rows][cols];
        for (int i = 0; i < rows; i++)   {
            for (int j = 0; j < cols; j++)   {
                val[i][j] = io.readDouble();
            }
        }

        MyMatrix test = new MyMatrix("test", 3, 4, 0);
        test.setMatrix(val);
        test.printMatrix();

        MyMatrix test1 = new MyMatrix("test1", 3, 3, 1);
        test1.divideMatrix(test);
    }
}