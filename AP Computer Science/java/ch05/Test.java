import java.util.Random;

public class Test {
    public static void main(String[] args) {
        Random r = new Random(100);
        for (int i=0; i<10; i++){
            System.out.println(r.nextInt(100));
        }   
        // Flat 한지 확인 
    }
}
