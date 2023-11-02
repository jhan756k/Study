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

        MyMatrix solve = m[0].gaussianElimination(m[1])[1];
        solve.printMatrix();
        
        m[1].checkMult(m[0], solve);

        MyMatrix det = m[0].divideMatrix(m[1]);
        det.printMatrix();

        solve = m[0].inverseAlgorithm(m[1]);
        solve.printMatrix();

        // ---------------------------------------------------------------
        // MyMatrix big = new MyMatrix("big", 1000, 1000, 0.0);
        // big.randomMatrix(-100, 100);

        // MyMatrix bigans = new MyMatrix("bigans", 1000, 1000, 0.0);
        // bigans.randomMatrix(-100, 100);

        // MyMatrix bigSolve = big.gaussianElimination(bigans);
        // bigSolve.printMatrix();

        // bigans.checkMult(big, bigSolve);
    }
}