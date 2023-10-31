package ch07;
import chn.util.*;

public class MyMatrixTest {
    public static void main(String[] args)   {
        FileInput io = new FileInput("ch07\\matrix.txt");
        int rows, cols;
        MyMatrix m[] = new MyMatrix[10];
        String stop;

        for (int k = 0; k < 10; k++) {
            rows = io.readInt();
            cols = io.readInt();
            double val[][] = new double[rows][cols];
            for (int i = 0; i < rows; i++)   {
                for (int j = 0; j < cols; j++)   {
                    val[i][j] = io.readDouble();
                }
            }
            m[k] = new MyMatrix("m" + k, rows, cols, 0);
            m[k].setMatrix(val);
            stop = io.readLine();

            if (stop.equals("stop")) {
                break; 
            }
        }
        
        m[0].printMatrix();
        m[1].printMatrix();

        MyMatrix []solve = m[0].gaussianElimination(m[1]);
        solve[0].printMatrix();
        solve[1].printMatrix();
        
        System.out.println(m[1].checkMult(m[0], solve[1]));
    }
}