public class Main
{
	public static void main(String[] args) throws VectorSizeException
	{
		//Test examples

		StringVector v = new StringVector( 10 );
	    v.put( 1, "January ");
	    v.put( 2, "February" );
	    System.out.println( v.find( "Fevereiro" ) ); // prints 2
	    System.out.println( v.at( 1 ) ); // prints Janeiro
	    System.out.println( v.at( 13 ) ); // prints exception
	    v.newSize( 2 ); // Ok
	    v.newSize( 1 ); // prints exception
	}
}