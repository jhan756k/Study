package ch08;

public class ImageTest {
    public static void main(String[] args) {
        Image image = new Image(9);
        for (int i = 0; i < 9; i++) {
            for (int j = 0; j < 9 ; j++) {
                if (Math.random() < 0.2)
                    image.setPixel(i, j);
            }
        }

        image.display();
        image.eraseBlob(0, 0);
        image.display();
    }
}
