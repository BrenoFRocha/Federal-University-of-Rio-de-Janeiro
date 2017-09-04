import java.util.Arrays;
import java.util.Comparator;

public class Main 
{
    public static void main( String[] args ) 
    {
        Data d[] = { new Data(), new Data(), new Data(), new Data() };

        d[0].setData( 2, 4, 2016 );
        d[1].setData( 12, 3, 2016 );
        d[2].setData( 3, 3, 2016 );
        d[3].setData( 7, 9, 2015 );

        for( Data x : new RangeData( d[2], d[1] ) )
        {
            System.out.println( x );
        }
    }
}