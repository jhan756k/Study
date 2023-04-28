public class Unit6 {
    public static void main(String[] args) {
        /*
        6. ARRAY
        
        you can create array of any object using [] keyword
        Array length --> arr.length
        String legth --> str.length()
        
        Enhanced for loop (each loop)
        for (Snack n : snacks) {
            System.out.println(n.getCalories());
        }

        Integer max value : Integer.MAX_VALUE
        Array left shift, right shift
        */
        int []x = {1, 2, 3, 4, 5};
        int shift = 3;
        int []y = new int[x.length];
        
        for (int i=0; i<x.length; i++){
            int place = (i + shift)%x.length;
            y[place] = x[i];
        }
    }
}
