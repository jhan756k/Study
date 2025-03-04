package ch07;
import chn.util.*;

public class MyMatrixTest {
    public static void main(String[] args)   {
        FileInput io = new FileInput("ch07\\matrix.txt");
        int rows, cols;
        MyMatrix []m = new MyMatrix[10];
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

        MyMatrix solve[] = m[0].gaussianElimination(m[1]);
        solve[1].printMatrix();

        MyMatrix inv[] = m[0].reduced(m[1]);
        inv[1].printMatrix();

        solve[0].printMatrix();
        inv[0].printMatrix();

        m[1].checkMult(m[0], solve[1]);
        m[1].checkMult(m[0], inv[1]);

        solve[1].compareMatrix(inv[1]);

        // inverse
        // MyMatrix inverse = m[0].inverseMatrix();
        // inverse.printMatrix();
        // inverse.multMatrix(m[1]).printMatrix();

        // ---------------------------------------------------------------
        MyMatrix big = new MyMatrix("big", 100, 100, 0.0);
        big.randomMatrix(-100, 100);

        MyMatrix bigans = new MyMatrix("bigans", 100, 100, 0.0);
        bigans.randomMatrix(-100, 100);

        MyMatrix gauss = big.gaussianElimination(bigans)[1];
        gauss.printMatrix();

        MyMatrix inverse[] = big.reduced(bigans);
        inverse[1].printMatrix();

        bigans.checkMult(big, gauss);
        bigans.checkMult(big, inverse[1]);

        gauss.compareMatrix(inverse[1]);
    }
}