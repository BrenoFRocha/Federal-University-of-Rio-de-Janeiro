//Federal University of Rio de Janeiro
@SuppressWarnings( "serial" )

public class VectorSizeException extends Exception 
{
    public VectorSizeException( int tamanhoMinimo, int tamanhoNovo ) 
    {
        super("O tamanho minimo é " + tamanhoMinimo + " mas foi tentato redimensionar para " + tamanhoNovo);
    }
}