package ch08;

public class Image {
    private final int BLACK = 1;
    private final int WHITE = 0;
    private int[][] pixels;
    private int size;

    public Image(int size) {
        this.size = size;
        pixels = new int[size][size];
    }

    public void setPixel(int x, int y, int value) {
        pixels[x][y] = value;
    }

    public void display() {
        for (int i = 0; i < size; i++) {
            System.out.println();
            for (int j = 0; j < size; j++) {
                if (pixels[i][j] == BLACK) {
                    System.out.print("*");
                } else {
                    System.out.print(0);
                }
            }
        }
        System.out.println();
        System.out.println("----------------");
    }

    public void eraseBlob(int x, int y) {
        if (x >= 0 && x < size && y >= 0 && y < size) {
            if (pixels[x][y] == BLACK) {
                pixels[x][y] = WHITE;
                eraseBlob(x - 1, y);
                eraseBlob(x + 1, y);
                eraseBlob(x, y - 1);
                eraseBlob(x, y + 1);
            }
        }
    }
}
