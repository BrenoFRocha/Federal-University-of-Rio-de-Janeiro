public class OrdemLimitada
{
	public int lots;
	public double price;
	public LivroDeOfertas.Direcao direction;

	public OrdemLimitada(int cliente, int numCorretora, LivroDeOfertas.Direcao d, int l, double p)
	{
		direction = d;
		lots = l;
		price = p;
	}
}
