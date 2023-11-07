package ch07;

public class Deck {
    private int[] deck = new int[52];

    public Deck() {
        for (int i = 0; i < deck.length; i++) {
            deck[i] = i;
        }
    }

    public void writeDeck() {
        for (int i = 0; i < deck.length; i++) {
            System.out.print(deck[i] + " ");
        }
        System.out.println();
    }

    private void swap(int[]arr, int i, int j) {
        int temp = arr[i];
        arr[i] = arr[j];
        arr[j] = temp; 
    }

    public void shuffle() {
        for (int i = 0; i < deck.length; i++) {
            int j = (int)(Math.random() * deck.length);
            swap(deck, i, j);
        }
    }
} 
