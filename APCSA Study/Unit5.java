public class Unit5 {
    public static void main(String[] args) {
        /*
        5. WRITING CLASSES

        public --> Access Modifier
        - no restriction on access 
        - other classes can access this class

        private --> Access Modifier
        - restricts access 
        - only accessible in given class

        For APCSA classes and constructors should always be public
        Instance variables should always be private
        Methods can be public or private depending on the situation

        -- Encapsulation --
        Wrap the data (instance variables) and the methods that operate on the data (accessor and mutator methods) into a single unit (class)
        We do this in APCSA by:
        1. Writing a class
        2. Declaring instance variables as private
        3. Providing accessor and mutator methods to view and modify

        
        */
    }

    public class Snack{

        // Private Instance Variables
        private String name;
        private int calories;

        // Default Constructor
        public Snack(){
            this.name = "";
            this.calories = 0;
        }

        // Overloaded Constructor
        public Snack(String n, int c){
            this.name = n;
            this.calories = c;
        }

        // Accessor Methods
        public String getName(){
            return this.name;
        }

        public int getCalories(){
            return this.calories;
        }

        // Mutator Methods
        public void setName(String n){
            this.name = n;
        }

        public void setCalories(int c){
            this.calories = c;
        }

        private Boolean canEat(){
            return(this.calories < 150);
        }
    }
}
