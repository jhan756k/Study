public class Unit10 {
    public static void main(String[] args) {
        /*
        10. RECURSION

        Draw recursion Call tree

        Binary Search - iterative and recursive
        */
    }

    public static int binarySearch(int[] arr, int low, int high, int target) {
        int mid;

        while (low <= high) {
            mid = (low + high) / 2;

            if (arr[mid] < target) {
                low = mid + 1;
            } else if (arr[mid] > target) {
                high = mid - 1;
            } else {
                return mid;
            }
        }
        return -1;
    }

    public static int recurSearch(int []arr, int low, int high, int target){
        int mid = (low + high) / 2;
        if (low > high) return -1; 
        else if (arr[mid] > target) return recurSearch(arr, low, mid-1, target);
        else if (arr[mid] < target) return recurSearch(arr, mid+1, high, target);
        return mid;
    }
}
