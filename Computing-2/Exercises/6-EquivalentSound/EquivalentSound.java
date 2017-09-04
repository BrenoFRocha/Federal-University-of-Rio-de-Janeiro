import java.util.Map;
import java.util.TreeMap;

public class EquivalentSound
{
	private Map<String,String> phonemes;

	public EquivalentSound(Map<String,String> p)
	{
		phonemes = p;
	}

	public boolean equivalent(String x, String y)
	{
		String word1, word2;
		if(x == null && y == "" || x == "" && y == null || x == null && y == null)
		{
			return true;
		}
		else
		{
			word1 = x;
			word2 = y;
			int index = 0;
			String letters1, letters2;
			word1 = word1.toLowerCase();
			word2 = word2.toLowerCase();
			while(index < phonemes.size())
			{
				if(word1.contains(getKey(index)))
				{
					word1 = word1.replaceAll(getKey(index),getValue(index));
				}
				if(word2.contains(getKey(index)))
				{
					word2 = word2.replaceAll(getKey(index),getValue(index));
				}
				index++;
			}
		}
		if(word1.equals(word2))
		{
			return true;	
		}
		else
		{
			return false;	
		}
	}

	private String getKey(int index)
	{
		return (phonemes.keySet().toArray()[index]).toString();
	}

	private String getValue(int index)
	{
		return (phonemes.get(phonemes.keySet().toArray()[index])).toString();
	}
}