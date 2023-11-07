package ch07;

public class ShuffleTest {
    
    public static void main(String[] args) {
        Deck deck = new Deck();
        deck.writeDeck();
        deck.shuffle();
        deck.writeDeck();
    }
}
