import java.util.ArrayList;
import java.util.Map;
import java.util.NavigableMap;
import java.util.TreeMap;

public class LivroDeOfertas
{
    public static enum Direcao
    {
        COMPRA, VENDA
    };

    private NavigableMap<Double, ArrayList<OrdemLimitada>> purchase, sale;

    public LivroDeOfertas(double variation)
    {
        purchase = new TreeMap<>();
        sale = new TreeMap<>();
    }

    public void registra(OrdemLimitada lOrder)
    {
        if(lOrder.direction == Direcao.COMPRA) //Purchase register
        {
            register(purchase, lOrder);
        }
        else //Sale register
        {
            register(sale, lOrder);
        }
        shopVerification();
    }

    public double getPrecoCompra()
    {
        if(purchase.size() > 0)
        {
            return purchase.lastKey();
        }
        return 0;
    }

    public double getPrecoVenda()
    {
        if(sale.size() > 0)
        {
            return sale.firstKey();
        }
        return 0;
    }

    public double getQuantidadeCompra(double p)
    {
        if(purchase.size() > 0)
        {
            return checkQuantity(purchase, p);
        }
        return 0;
    }

    public double getQuantidadeVenda(double p)
    {
        if(sale.size() > 0)
        {
            return checkQuantity(sale, p);
        }
        return 0;
    }

    private Double getKey(Map map, int index)
    {
        return new Double((map.keySet().toArray()[index]).toString());
    }

    private int verification(NavigableMap<Double, ArrayList<OrdemLimitada>> map, Double price)
    {
        for(int i = 0; i < map.size(); i++)
        {
            if(getKey(map, i).equals(price))
            {
                return i;
            }
        }
        return -1;
    }

    private void register(NavigableMap<Double, ArrayList<OrdemLimitada>> map, OrdemLimitada lOrder)
    {
        int id;
        id = verification(map, lOrder.price);
        if(id != -1)
        {
            map.get(lOrder.price).add(lOrder);
        }
        else
        {
            ArrayList<OrdemLimitada> nOrder;
            nOrder = new ArrayList<>();
            nOrder.add(lOrder);
            map.put(lOrder.price, nOrder);
        }
    }

    private int checkQuantity(NavigableMap<Double, ArrayList<OrdemLimitada>> map, Double p)
    {
        if(map.containsKey(p))
        {
            int lots;
            lots = 0;
            for(int i = 0; i < map.get(map.floorKey(p)).size(); i++)
            {
                lots += map.get(map.floorKey(p)).get(i).lots;
            }
            return lots;
        }
        return 0;
    }

    private void shopVerification()
    {
        while(getPrecoCompra() >= getPrecoVenda() && getPrecoCompra() != 0 && getPrecoVenda() != 0)
        {
            purchase.get(purchase.floorKey(getPrecoCompra())).get(0).lots -= 1;
            sale.get(sale.floorKey(getPrecoVenda())).get(0).lots -= 1;
            if(purchase.get(purchase.floorKey(getPrecoCompra())).get(0).lots == 0)
            {
                purchase.get(purchase.floorKey(getPrecoCompra())).remove(0);
            }
            if(sale.get(sale.floorKey(getPrecoVenda())).get(0).lots == 0)
            {
                sale.get(sale.floorKey(getPrecoVenda())).remove(0);
            }
            if(purchase.get(purchase.floorKey(getPrecoCompra())).size() <= 0)
            {
                purchase.remove(purchase.floorKey(getPrecoCompra()));
            }
            if(sale.get(sale.floorKey(getPrecoVenda())).size() <= 0)
            {
                sale.remove(sale.floorKey(getPrecoVenda()));
            }
        }
    }
}