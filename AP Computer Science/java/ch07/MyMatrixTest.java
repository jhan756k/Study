package ch07;

public class MyMatrixTest {
    public static void main(String[] args) {
        MyMatrix m = new MyMatrix();
        m.printMatrix();

        MyMatrix m2 = new MyMatrix("m2", 3, 4, 1.0);
        m2.printMatrix();
    }
}
