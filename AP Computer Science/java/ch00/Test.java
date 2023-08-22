class Test {
    public static void main(String[] args) {
        int[][] b = new int[4][];
        b[0] = new int[] { 1 };
        b[1] = new int[] { 1, 2 };
        b[2] = new int[] { 1, 2, 3 };
        b[3] = new int[] { 1, 2, 3, 4 };

        for (int i = 0; i < b.length; i++) {
            for (int j = 0; j < b[i].length; j++) {
                System.out.print(b[i][j] + " ");
            }
            System.out.println();
        }
    }
}
