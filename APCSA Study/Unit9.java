public class Unit9 {
    public static void main(String[] args) {
        /*
        9. INHERITANCE

        superclass - parent class
        subclass - child class
        subclass IS A superclass

        extends keyword - subclass inherits from superclass
        the subclass inherits all the methods and variables from the superclass

        Constructors are not inherited
        However, after creating a child class instance, when the constructor of the child is called, the constructor of the parent is immediately called(The one with no parameter by default)

        if no super() is called, Java adds super() to the first line of the constructor

        super() keyword MUST be the first line of the constructor
        

        all public and protected methods and variables are inherited
        Methods may be overloaded or overridden

        Overloading - same method name, different parameters
        Overriding - same method name, same parameters, different implementation (by a subclass)

        super.methodName() - calls the method of the superclass
        since this is not a constructor, it can be called anywhere in the subclass

        Be careful of subclass accessing private variables of the superclass (Error)

        Performer p = new Musician();
        --> IS A relationship, se we can declare it like this
        We use this technique to create an array of objects of different subclasses

        This supports polymorphism
        Polymorphism - the ability of an object to take on many forms

        A reference variable is polymorphic if it can refer to objects of multiple classes
        A method is polymorphic if it is overridden in at least one subclass
        
        Look at the tellJoke method below. It is only declared in the subclass, so when I declare it as 

        Performer p = new Musician();
        System.out.println(p.tellJoke()); 

        IT DOES NOT COMPILE Since at compile time, the compiler only knows that Object p is a Performer, and Performer does not have a tellJoke method.(So it checks the Performer class)

        --> Compile time: reference type | Runtime: object type

        To fix this, we have to downcast.
        --> System.out.println(((Musician)p).tellJoke());

        
        All classes in Java inherit from the Object class (java.lang.Object)
        toString method is inherited from the Object class
        toString method is called when we print an object

        public String toString(){}
        public boolean equals(Object o){}

        --> Overriding these methods (Also in subclasses)
        */
    }
    class Performer{
        private String name;
        private int age;

        public Performer(){
            name = "unknown";
            age = 0;
        }
        public Performer(String n, int a){
            name = n;
            age = a;
        }

        public void perform(){
            System.out.println("Performer is performing");
        }

        public String toString(){
            return name + " " + age;
        }
    }

    class Musician extends Performer{
        private String instrument;

        public Musician(){
            super();
            instrument = "unknown";
        }
        public Musician(String inst){
            super();
            instrument = inst;
        }
        public Musician(String n, int a, String inst){
            // name = n; --> causes error since name is private
            super(n, a);
            instrument = inst;
        }

        public void perform(){ // Overridden method
            super.perform(); // calls the perform method of the superclass
            System.out.println("Musician is performing");
        }

        public String tellJoke(){  // Exists only in the subclass
            return "Why did the chicken cross the road?";
        }

        public String toString(){
            return super.toString() + " " + instrument;
        }
    }
}
