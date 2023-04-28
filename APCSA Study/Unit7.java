import java.util.ArrayList;
public class Unit7 {
    public static void main(String[] args) {
        /*
        7. ARRAYLIST

        Arrays are static in size (once initialized) - primitive data type
        Arraylists are dynamic in size (can be changed) - object
        - Arraylist is made with the array class.

        import java.util.ArrayList;
        ArrayList<Integer> num = new ArrayList<Integer>(n);
        - n is the initial size of the arraylist (not required)
        Arraylists can only store objects, so Wrapper classes are a workaround.

        new ArrayList<E>(); where E is object type


        -- ArrayList Methods -- 

        .size() --> returns the size of the arraylist
        .add(E) --> adds an element to the end of the arraylist (returns true)
        .add(int index, E) --> adds an element to the specified index (max_index+1 still works since it means adding E to the end, returns true)
        .remove(int index) --> removes the element at the specified index (returns removed element)
        .set(int index, E) --> replaces the element at the specified index with E (returns former element of index)
        .get(int index) --> returns the element at the specified index


        -- ArrayList Methods (Wrapper Classes) --

        When passing ArrayList as a parameter, you should specify the type of object it stores. ( public static void m(ArrayList<Integer> arr) )
        When not specified (ArrayList arr), the program can change the values into a different type of object that the ArrayList was not intialized with. (ex: ["hello", 0, 1, 2])
        ==> It doesn't cause a error, which is problematic.

        When returning ArrayList, if cases like above (different objects in one ArrayList) happens, an error will occur. 
        That's why you need to specify the type of object in both the parameter and return type.

        ==> ArrayList<E> is more preferred than ArrayList (without specifying the type of object) since it prevents errors.


        While traversing and removing elements, start from the end of the ArrayList and end at the start.
        
        Enhanced for loops make a copy of each entry. Therefore, changing values in a for-each loop does not change the values in the ArrayList.
        Also, you cannot update the ArrayList in a for-each loop. (ex: remove elements)


        -- Searching --
        int --> ==
        double --> Math.abs(a-b) < delta
        object --> .equals()

        -- Sorting --
        1. Selection Sort
        2. Insertion Sort
        
        Why is Insertion Sort better than Selection Sort?
        --> It provides sorted list up to that point even if the program was terminated during the sorting process.
        Both have O(n^2) time complexity.

        int identifier = fullName.hashCode(); --> hashCode is a Object class method that returns a unique integer for each object.
        */

        // Selection Sort
        int []arr = {5, 4, 3, 2, 1};

        for (int outerLoop = 0; outerLoop < arr.length; outerLoop++) {
            int minIndex = outerLoop;
            for (int inner = outerLoop + 1; inner < arr.length; inner++) {
                if (arr[inner] < arr[minIndex]) {
                    minIndex = inner;
                }
            }
            if (minIndex != outerLoop) {
                swapItems(minIndex, outerLoop, arr);
            }
        }

        // Insertion Sort
        for (int outerLoop = 1; outerLoop < arr.size(); outerLoop++) {
            int innerLoop = outerLoop-1;
            while (innerLoop > 0 && arr[innerLoop] < arr[innerLoop - 1]) {
                swapItems(innerLoop, innerLoop - 1, arr);
                innerLoop--;
            }
        }

    }

    private void swapItems(int index1, int index2, Object[] arr) {
        Object thirdHand = arr[index1];
        arr[index1] = arr[index2];
        arr[index2] = thirdHand;
    }
}