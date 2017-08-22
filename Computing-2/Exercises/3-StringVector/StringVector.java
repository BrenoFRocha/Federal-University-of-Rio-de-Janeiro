//Developed by: Breno Rocha - github.com/BrenoFerreiraRocha
public class StringVector
{
	private int lastSize, vectorSize;
	private String[] savedText, lastText;
	public StringVector(int vectorCapacity)
	{
		vectorSize = vectorCapacity;
		savedText = new String[vectorSize];
		for(int i = 0; i < vectorSize; i++)
		{
			savedText[i] = "";
		}
	}
	public void newSize(int nS) throws VectorSizeException
	{
		int lastS;
		lastS = 0;
		if(nS > vectorSize)
		{
			lastText = savedText;
			lastS = vectorSize;
			vectorSize = nS;
			savedText = new String[vectorSize];
			for(int i = 0; i < vectorSize; i++)
			{
				if(i < lastS)
				{
					if(lastText[i] != "")
					{
						savedText[i] = lastText[i];
					}
					else
					{
						savedText[i] = ""; 
					}
				}
				else
				{
					savedText[i] = "";
				}
			}
		}
		else if(nS < vectorSize)
		{
			int quant;
			String[] testText;
			quant = 0;
			for(int i = 0; i < vectorSize; i++)
			{
				if(savedText[i] != "")
				{
					quant += 1;
				}
			}
			lastS = quant;
			if(lastS > nS)
			{
				throw new VectorSizeException(lastS,nS);
			}
			testText = new String[quant];
			quant = 0;
			for(int i = 0; i < vectorSize; i++)
			{
				if(savedText[i] != "")
				{
					testText[quant] = savedText[i];
					quant += 1;
				}
			}
			lastText = savedText;
			lastSize = vectorSize;
			vectorSize = nS;
			savedText = new String[vectorSize];
			for(int i = 0; i < vectorSize; i++)
			{
				savedText[i] = "";
			}
			for(int i = 0; i < testText.length; i++)
			{
				savedText[i] = testText[i];
			}
		}
	}
	public String at(int i)
	{
		return savedText[i];
	}
	public int find(String st)
	{
		for (int i = 0; i < vectorSize; i++)
		{
			if(savedText[i] == st)
			{
				return i;
			}			
		}
		return -1;
	}
	public void put(int i, String st)
	{
		savedText[i] = st;
	}
}