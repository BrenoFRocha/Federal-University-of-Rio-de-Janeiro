public class Main 
{
    public static void main(String[] args) 
    {
        LivroDeOfertas livro = new LivroDeOfertas(0.5);
        int numCorretora = 45;
        int cliente = 23;
        //Purchase
        livro.registra( new OrdemLimitada(cliente, numCorretora, LivroDeOfertas.Direcao.COMPRA, 500, 14.97));
        livro.registra( new OrdemLimitada(cliente, numCorretora, LivroDeOfertas.Direcao.COMPRA, 350, 14.97));
        livro.registra( new OrdemLimitada(cliente, numCorretora, LivroDeOfertas.Direcao.COMPRA, 500, 20.97));
        livro.registra( new OrdemLimitada(cliente, numCorretora, LivroDeOfertas.Direcao.COMPRA, 500, 21.97));
        //Sale
        livro.registra( new OrdemLimitada(cliente, numCorretora, LivroDeOfertas.Direcao.VENDA, 500, 12.42));
        livro.registra( new OrdemLimitada(cliente, numCorretora, LivroDeOfertas.Direcao.VENDA, 20, 12.42));
        livro.registra( new OrdemLimitada(cliente, numCorretora, LivroDeOfertas.Direcao.VENDA, 500, 5.12));
        livro.registra( new OrdemLimitada(cliente, numCorretora, LivroDeOfertas.Direcao.VENDA, 500, 59.99));
        //Results
        System.out.println(livro.getPrecoCompra());
        System.out.println(livro.getPrecoVenda());
        System.out.println(livro.getQuantidadeCompra(14.97));
        System.out.println(livro.getQuantidadeVenda(5.12));
    }
}