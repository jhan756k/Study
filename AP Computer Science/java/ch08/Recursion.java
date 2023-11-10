package ch08;
import chn.util.*;

public class Recursion {
    public static void stackWords() {
        ConsoleIO io = new ConsoleIO();
        String word = io.readLine();

        if (word.equals(".")) {
            System.out.println();
        } else {
            stackWords();
        }
        System.out.println(word);
    }

    public static void drawLine(int n) {
        if (n == 0) {
            System.out.println();
        } else {
            for (int i = 0; i < n; i++) {
                System.out.print("*");
            }
            System.out.println();
            drawLine(n - 1);
        }
    }

    public static int factorial(int n) {
        if (n < 0) {
            System.out.println("Invalid input");
            return 0;
        } 
        else if (n == 0 || n == 1) {
            return 1;
        } else {
            return n * factorial(n - 1);
        }
    }

    public static int fibonacci(int n) {
        if (n < 0) {
            System.out.println("Invalid input");
            return 0;
        }
        else if (n == 0 || n == 1) {
            return n;
        } else {
            return fibonacci(n - 1) + fibonacci(n - 2); // 계산값을 따로 저장해서 계속 불러오는 것이 연산 횟수를 줄일 수 있음
        }
    }

    private static int sum(int n) {
        if (n == 1) 
            return 1;
        else 
            return n + sum(n - 1);
    }

    public static int getSum(int n){ // Helper method
        if (n < 0) {
            System.out.println("Invalid input");
            return 0;
        }
        else if (n == 0) {
            return 0;
        } else {
            return sum(n);
        }
    }
    
    public static void main(String[] args) {
        stackWords();
        drawLine(5);
        System.out.println(factorial(5));
        System.out.println(fibonacci(5));
        System.out.println(getSum(5));
    }
}