public class Data
{
	private int day, month, year;

	public String toString()
	{
			switch(month)
			{
				case 1:
					return verifier(32, "Janeiro");
				case 2:
					if((year % 400 == 0) || (year % 4 == 0 && year % 100 != 0))
					{
						return verifier(30, "Fevereiro");
					}
					else
					{
						return verifier(29, "Fevereiro");
					}
				case 3:
					return verifier(32, "Março");
				case 4:
					return verifier(31, "Abril");
				case 5:
					return verifier(32, "Maio");
				case 6:
					return  verifier(31, "Junho");
				case 7:
					return  verifier(32, "Julho");
				case 8:
					return  verifier(32, "Agosto");
				case 9:
					return  verifier(31, "Setembro");
				case 10:
					return  verifier(32, "Outubro");
				case 11:
					return  verifier(31, "Novembro");
				case 12:
					return  verifier(32, "Dezembro");
				default:
					return  "Mês inválido: "+month;
			}
	}

	private String verifier(int a, String c)
	{
		if(day < a && day > 1)
		{
			return day + "/" + month + "/" + year;
		}
		else
		{
			if(c.equals("Fevereiro"))
			{
				if(a == 30)
				{
					return year+" é um ano bissexto. Para " + c + ", o dia deve estar entre 1 e " + (a-1) + ", mas foi passado " + day;
				}
				else
				{
					return year+" não é ano bissexto. Para " + c + ", o dia deve estar entre 1 e " + (a-1) + ", mas foi passado " + day;
				}
			}
			else
			{
				return "Para " + c + ", o dia deve estar entre 1 e " + (a-1) + ", mas foi passado " + day;
			}
		}
	}
	
	public void setData(int d, int m, int y)
	{
			this.day = d;
			this.month = m;
			this.year = y;
	}
}
