package ch07;
import chn.util.*;

public class MyMatrixTest {
    public static void main(String[] args)   {
        FileInput io = new FileInput("java\\ch07\\matrix.txt");
        String name = io.readLine();
        int rows = io.readInt();
        int cols = io.readInt();
        

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