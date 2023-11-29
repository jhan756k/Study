package ch09;
import java.util.*;

public class SortTest
{
	public static void main(String[] args) 
	{
		Random rand = new Random();
		int size;
		int[] array;

		if(args.length == 0)
			size = 10;
		else
			size = Integer.parseInt(args[0]);

		array = new int[size];
		for(int i = 0; i < array.length; i++)
			array[i] = i + 1;
		AllSorts.print(array);

		randomInitialize(array, rand);
		AllSorts.print(array);
		System.out.println("Merge Sort...");
		MergeSort.Merge(array, 'a');
		// SelectionSort.sort(array);
		AllSorts.print(array);
	}

	public static void randomInitialize(int[] a, Random rand)
	{
		rand = new Random(1);
		for(int i = a.length - 1; i > 0; i--)
		{
			int swap = rand.nextInt(i);
			int temp = a[i];
			a[i] = a[swap];
			a[swap] = temp;
		}
	}
}
