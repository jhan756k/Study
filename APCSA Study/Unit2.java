public class Unit2 {
    public static void main(String[] args) {
        /*
        2. USING OBJECTS

        Objects and Classes

        Class - blueprint for objects
        Object - instance of a class

        public Person(String nm, int ag, boolean ad) {
            name = nm;
            age = ag;
            isAdult = ad;
        }

        Person p1 = new Person("John", 20, true);

        Signature & Overloading
        Which Constructor was used?

        null - reference is not pointing to an object

        Procedural Abstraction

        Person p1; --> declaration
        p1.talk(); --> Null Pointer Exception

        immutable - unchangeable
        String is immutable in Java

        \ --> escape sequence
        \", \\, \n --> ", \, new line


        Java Quick Reference (JQR)

        -- IndexOf --
        import java.lang.String; --> not needed
        "monkey".indexOf("e") --> 4
        "monkey".indexOf("e", 5) --> -1
        IndexOutOfBoundsException

        java.lang is automatically imported

        -- Substring -- 
        "monkey".substring(2) --> "nkey"
        "monkey".substring(2, 4) --> "nk"

        -- Length --
        "monkey".length() --> 6

        -- Equals --
        "monkey".equals("monkey") --> true

        -- CompareTo --
        https://mine-it-record.tistory.com/133
        "monkey".compareTo("monkey") --> 0
        "monkey".compareTo("monkeys") --> -1


        Integer is a wrapper class, int is a primitive type

        intValue(), doubleValue(), ... --> return the value of primitive data type of the wrapper class

        Double d = new Double(3.141592);
        double d2 = d.doubleValue();
        System.out.println(d2);


        AutoBoxing & Unboxing
        
        int num = 157;
        Integer num2 = num; --> AutoBoxing
        int num3 = num2; --> Unboxing
        int sum = num + num2; --> Unboxing

        Math Class
        - Methods are static

        1. int abs (int x)
        2. double abs (double x)
        3. double pow (double x, double y) --> x^y
        4. double sqrt (double x)
        5. double random ()

        (int)(Math.random()*51) + 50; --> 50 ~ 100 inclusive
        (int)(Math.random()*101) --> 0 ~ 100 inclusive
        */
    }
}
