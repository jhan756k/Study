public class Unit3 {
    public static void main(String[] args) {
        /*
        3. BOOLEAN EXPRESSIONS AND IF STATEMENTS

        JAVA DOESN'T CARE ABOUT INDENTATION

        -- DANGLING ELSE --
        if (a > 20)
            if (b > 20) System.out.println("A");
        else System.out.println("B");

        --> the else goes to the SECOND IF!!! (always to the closest if)

        That's why you should always use curly braces

        if (a > 20) 
        {
            if (b > 20) System.out.println("A");
        }
        else System.out.println("B");

        --> this forces the else to go to the first if

        
        -- Short-Circuited Evaluation --
        - In the Case of &&, ||
        - Java only evaluates the second part if the statement cannot be determined by the first part
        if (score > 0 && sum/score > 80) --> Doesn't create ArithmeticException
        if (sum/score > 80 && score > 0) --> Creates ArithmeticException if score == 0


        -- De Morgan's Laws --
        !(a && b) --> !a || !b
        !(a || b) --> !a && !b
        
        ! flips all operators
        ex) !(x > 0) --> x <= 0

        !(x<-5 || x>10)
        (!(x<-5) && !(x>10))
        (x>=-5 && x<=10)

        We can assure De Morgan's Laws by using the truth table
        --> Equations are equivalent if they have the same truth table


        -- Object Referencing --
        House myHouse = new House("Green", 1850, 3);
        House annasHouse = new House("Green", 1850, 3);
        House bobsHouse;
        House momsHouse = myHouse;

        --> Only 2 House objects are created (myHouse and annasHouse)
        - myHouse and momsHouse point to the same object (Aliases)
        - bobsHouse does not reference any object (null)

        If a class has it's own equals method and overrides it (public boolean equals(Object other))
        then it will return true if parameters are same and false when two objects are different
        */
    }
}
