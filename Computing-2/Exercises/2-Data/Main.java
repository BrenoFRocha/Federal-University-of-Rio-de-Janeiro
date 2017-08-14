import java.util.Scanner;
public class Main
{
	public static void main(String args[])
	{
			Scanner scan = new Scanner(System.in);
			int l, m , n;
			Data data = new Data();

			l = scan.nextInt();
			m = scan.nextInt();
			n = scan.nextInt();
			
			data.setData(l,m,n);
			System.out.println(data.toString());
	}
}
