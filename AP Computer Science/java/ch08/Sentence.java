package ch08;

public class Sentence {
    
    private String sentence;
    private int numWords;

    public Sentence(String arr) {
        sentence = arr;
        for (int i = 0; i < arr.length(); i++) {
            if (arr.charAt(i) == ' ') numWords++;
        }
    }

    public int getNumWords() {
        return numWords;
    }

    public String getSentence() {
        return sentence;
    }
    
    private String removeBlanks(String s) {
        String result = "";
        for (int i = 0; i < s.length(); i++) {
            if (s.charAt(i) != ' ') result += s.charAt(i);
        }
        return result;
    }

    private String lowerCase(String s) {
        String result = ""; 
        for (int i = 0; i < s.length(); i++) {
            if (s.charAt(i) >= 'A' && s.charAt(i) <= 'Z') result += (char)(s.charAt(i) + 32);
            else result += s.charAt(i);
        }
        return result;
    }

    private String removePunctuation(String s) {
        String result = "";
        for (int i = 0; i < s.length(); i++) {
            if (Character.isLetter(s.charAt(i))) result += s.charAt(i);
        }
        return result;  
    }

    private boolean isPalindrome(String s, int start, int end) {
        if (start >= end) return true;
        if (s.charAt(start) != s.charAt(end)) return false;
        return isPalindrome(s, start + 1, end - 1);
    }

    public boolean isPalindrome() { // Helper Method
        String tmp = removeBlanks(sentence);
        tmp = removePunctuation(tmp);
        tmp = lowerCase(tmp);
        return isPalindrome(tmp, 0, tmp.length() - 1);
    }

}
