import java.util.Iterator;

public class RangeData implements Iterable<Data> 
{
    private Data a;
    private Data b;
    private boolean proximo;

    public RangeData( Data a, Data b ) 
    {
        this.a = a;
        this.b = b;
        proximo = a.verificador(b);
    }

    @Override
    public Iterator<Data> iterator() 
    {
        return new Iterator<Data>() 
        {
            private Data atual = a;

            @Override
            public boolean hasNext() 
            {
                return atual.comparaDia(b);
            }

            @Override
            public Data next() 
            {
                if(proximo)
                {
                    return atual.proximoDia();
                }
                else
                {
                    return atual.anteriorDia();
                }
            }
        };
    }
}