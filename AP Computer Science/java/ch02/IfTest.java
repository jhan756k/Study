public class IfTest {
    public static void main(String[] args) {
        int n = -10;
        if (n > 0)
            if (n % 2 == 1)
                System.out.println("n is positive odd number");
        else
            System.out.println("n is positive even number"); // 두번째 if문에 속하는 else문
            else 
                System.out.println("n is negative number"); // 첫번째 if문에 속하는 else문
    }
}
