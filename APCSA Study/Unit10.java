public class Unit10 {
    public static void main(String[] args) {
        /*
        10. RECURSION

        Draw recursion Call tree

        Binary Search - iterative and recursive
        Merge Sort - iterative and recursive
        */
        int[] arr = {1, 2, 3, 4, 5, 6, 7, 8};
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

    public static void mergeSort(int[] arr, int low, int high) {
        if (low < high) {
            int mid = (low + high)/2;
            mergeSort(arr, low, mid);
            mergeSort(arr, mid+1, high);
            merge(arr, low, mid, high);
        }
    }

    public static void merge(int[] arr, int low, int mid, int high) {
        int[] temp = new int[high-low+1];
        int i = low, j = mid+1, k = 0;

        while (i <= mid && j <= high) {
            if (arr[i] < arr[j]) temp[k++] = arr[i++];
            else temp[k++] = arr[j++];
        }

        while (i <= mid) temp[k++] = arr[i++];
        while (j <= high) temp[k++] = arr[j++];

        for (int l = low; l <= high; l++) {
            arr[l] = temp[l-low];
        }
    }
}
