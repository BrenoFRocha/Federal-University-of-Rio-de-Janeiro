public class BubbleSort
{
    public static void main(String args[]) 
    {
        int v[] = { 4, 7, 1, 8, 23, 3, 9, 6 };
    	v = sorter(v);
    	for(int i = 0; i < v.length; i++)
    	{
    		if(i == v.length-1)
    		{
    			System.out.println(v[i]);
    		}
    		else
    		{
    			System.out.print(v[i] + " ");
    		}
    	}
    }
    public static int[] sorter(int[] numbers)
    {
    	int sorted[];
    	sorted = numbers;
        for (int i = 0; i < sorted.length - 1; i++)
        {
            for (int j = i + 1; j < sorted.length; j++)
            {
                if (sorted[i] > sorted[j])
                {
                    int keep = sorted[i];
                    sorted[i] = sorted[j];
                    sorted[j] = keep;
                }
            }
        }
        return sorted;
    }
}