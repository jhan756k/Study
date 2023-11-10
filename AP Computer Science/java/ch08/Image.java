package ch08;

public class Image {
    private final int BLACK = -1;
    private int[][] pixels;
    private int size;
    public static int cnt = 1;

    public Image(int size) {
        this.size = size;
        pixels = new int[size][size];
    }

    public void setPixel(int x, int y) {
        pixels[x][y] = BLACK;
    }

    public void display() {
        for (int i = 0; i < size; i++) {
            System.out.println();
            for (int j = 0; j < size; j++) {
                if (pixels[i][j] == BLACK) {
                    System.out.print("* ");
                } else {
                    System.out.print(pixels[i][j] + " ");
                }
            }
        }
        System.out.println();
        System.out.println();
        for (int i = 0; i < size*2-1; i++) System.out.print("-");
        System.out.println();
    }

    public void eraseBlob(int x, int y) {
        if (x >= 0 && x < size && y >= 0 && y < size) {
            if (pixels[x][y] == BLACK) {
                pixels[x][y] = cnt;
                cnt++;
                eraseBlob(x - 1, y);
                eraseBlob(x + 1, y);
                eraseBlob(x, y - 1);
                eraseBlob(x, y + 1);
            }
        }
    }
}
