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

        Even if a overloaded Constructer's paramter doesn't recieve a value of a instance variable, the programmer MUST provide a default value.
        
        If no constructor is provided, JAVA will provide a default constructor.
        --> int 0, double 0, other objects null


        Javadoc Comments
        @params, @author, @version

        Precondition
        - Comments for a method
        - Conditions that must be met for the method to work
        - Code in method is based on precondition being true
        - precondition, postcondition
        
        Accessor Methods
        - get methods
        - must be public 
        - return type should match
        - camelCase
        - No parameters

        toString method 
        - returns a string representation of the object

        Mutator Methods
        - set methods
        - must be public
        - return type is void
        - camelCase
        - parameter type should match instance variable type
        
        Method Header
        - Access Level (public/private)
        - Ownership (static/non-static) static - class owns method non-static - individual object owns method
        - Return Type (void, int, double, String, boolean, etc.)
        - Identifier (name of method)
        - Parameters (type and name of parameters)
        
        Static methods can only access static variables
        Non-static methods can access static and non-static variables

        Local variables can be declared in the body of constructor or method

        This keyword
        - can be used to refer to methods of a class --> optional
        - specify the object being constructed
        - this as object parameter

        

        Look at Code below!
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
        public Snack(String n, int c){ // Since n,c is local, other methods cannot use it.
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

        /**
         * Method to set value of calories
         * @param c - value to set calories
         * Precondition: c must be greater than 0
         * Postcondition: calories is set to c
         */
        public void setCalories(int c){
            this.calories = c;
        }

        private Boolean canEat(){
            return(this.calories < 150);
        }

        // Snack cookie = new Snack("Oreo", 140);
        // System.out.println(cookie);
        // --> toString method is called automatically
        public String toString(){ 
            // This is printed
            return "Name: " + this.name + " Calories: " + this.calories;
        }

        public boolean isSameName(Snack other){
            return(getName().equals(other.name));
            // Snack class 내부이므로 getName()도 되고 
            // private 변수 직접 접근 가능
        }
    }
}
