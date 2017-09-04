public class Data 
{
    static private final int nDias[] = { 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31 };
    static private final String nome[] = { "Janeiro", "Fevereiro", "Março", "Abril", "Maio", "Junho", "Julho", "Agosto", "Setembro", "Outubro", "Novembro", "Dezembro" };

    private int dia = 1;
    private int mes = 1;
    private int ano = 1970;
    private int fTime = 0;
    private int comando = 2;

    public boolean verificador(Data comparer)
    {
    	if(this.ano < comparer.ano)
    	{
    		return true;
    	}
    	else if(this.mes < comparer.mes && this.ano <= comparer.ano)
    	{
    		return true;
    	}
    	else if(this.dia < comparer.dia && this.mes <= comparer.mes && this.ano <= comparer.ano)
    	{
    		return true;
    	}
    	return false;
    }

 	public Data anteriorDia()
    {
    	if(this.fTime == 0)
    	{
    		this.dia += 1;
    		this.fTime += 1;
    	}
    	this.dia -= 1;
    	if(criticaData(dia, mes, ano )) 
    	{
            this.dia = dia;
            this.mes = mes;
            this.ano = ano;
        }
        else
        {
        	this.mes -= 1;
        	if( mes == 2 ) 
        	{
                if( bissexto( ano ) )
                {
                	this.dia = 29;
                }
                else
                {
                	this.dia = 28;
                }
        	}
            else
            {
            	if(mes != 1)
            	{
            		this.dia = nDias[mes - 1];
            	}
            }
        	if(criticaData(dia, mes, ano )) 
    		{
    			this.dia = dia;
	            this.mes = mes;
	            this.ano = ano;
    		}
    		else
    		{
    			this.dia = 31;
    			this.mes = 12;
    			this.ano -= 1;
    		}
        }    	
    	return this;
    }


    public Data proximoDia()
    {
    	if(this.fTime == 0)
    	{
    		this.dia -= 1;
    		this.fTime += 1;
    	}
    	this.dia += 1;
    	if(criticaData(dia, mes, ano )) 
    	{
            this.dia = dia;
            this.mes = mes;
            this.ano = ano;
        }
        else
        {
        	this.dia = 1;
        	this.mes += 1;
        	if(criticaData(dia, mes, ano )) 
    		{
    			this.dia = dia;
	            this.mes = mes;
	            this.ano = ano;
    		}
    		else
    		{
    			this.dia = 1;
    			this.mes = 1;
    			this.ano += 1;
    		}
        }    	
    	return this;
    }

    public boolean comparaDia(Data cData)
    {
    	if(cData.dia != this.dia || cData.mes != this.mes || cData.ano != this.ano)
    	{
    		return true;
    	}
    	return false;
    }

    public String toString() 
    {
        return this.dia + "/" + this.mes + "/" + this.ano;
    }

    public void setData( int dia, int mes, int ano ) 
    {
        if( criticaData( dia, mes, ano ) ) 
        {
            this.dia = dia;
            this.mes = mes;
            this.ano = ano;
        }
    }

    private boolean criticaData( int dia, int mes, int ano ) 
    {
        if( mes < 1 || mes > 12 ) 
        {
            return false;
        } 
        else 
        {
            if( mes == 2 ) 
            {
                if( bissexto( ano ) )
                    if( 1 <= dia && dia <= 29 )
                    {
                        return true;
                    }
                    else 
                    {
                        return false;
                    }
                else if( 1 <= dia && dia <= 28 )
                {
                    return true;
                }
                else 
                {
                    return false;
                }

            } 
            else if( 1 <= dia && dia <= nDias[mes - 1] )
            {
                return true;
            }
            else 
            {
                return false;
            }
        }
    }

    private boolean bissexto( int ano ) 
    {
        if( ano % 400 == 0 )
        {
            return true;
        }

        if( ano % 100 == 0 )
        {
            return false;
        }

        return ano % 4 == 0;
    }
}