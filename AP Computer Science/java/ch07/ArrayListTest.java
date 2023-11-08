package ch07;
import java.util.ArrayList;

public class ArrayListTest {
    public static void main(String[] args) {
        ArrayList<Integer> list = new ArrayList<Integer>();

        for (int i = 0; i < 11; i+=2) {
            list.add(i); 
        }

        int n = list.get(3); // auto unboxing (Integer -> int)

        int na = list.set(3, 100); // Set 은 값 반환
        
        na = list.remove(2); // Remove 도 값 반환

        System.out.println(n);
        System.out.println(na);

        list.add(2, -201); // 2번째 index에 200 추가

        print(list);

        for (int i : list) {
            if (i % 2 == 0) {
                System.out.printf("%d ", i);
            }
        }
    }

    public static void swap(ArrayList<Integer> list, int i, int j) {
        int temp = list.get(i);
        list.set(i, list.get(j));
        list.set(j, temp);
    }

    public static void print(ArrayList<Integer> list) {
        for (int i = 0; i < list.size(); i++) {
            System.out.printf("%d ", list.get(i));
        }
        System.out.println();
    }

    public static ArrayList<Integer> getRandomIntList(int n) {
        ArrayList<Integer> list = new ArrayList<Integer>();
        for (int i = 0; i < n; i++) {
            list.add((int)(Math.random() * 100));
        }
        return list;
    }

    public static void insert(ArrayList<Integer> list, int index, int value) {
        int ind = 0;
        for (int i = 0; i < list.size(); i++) {
            if (list.get(i) > value) {
                ind = i;
                break;
            }
        }
        list.add(ind, value);
    }

    public static void removeAll(ArrayList<Integer> list, int value) {
        for (int i = 0; i < list.size(); i++) {
            if (list.get(i) == value) {
                list.remove(i);
                i--;
            }
        }
    }
}
