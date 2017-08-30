import java.util.ArrayList;
import java.util.HashMap;
import java.util.TreeMap;
import java.util.Map;
import java.util.Comparator;
import java.util.Map.Entry;
import java.util.Set;

public class TextEvaluator
{
  private ArrayList<String> textWords;
  private ArrayList<Entry<String, Integer>> textArray, stopArray;
  private ArrayList<String> stopWords;
  private Map<String,Integer> textMap, stopMap;

  public TextEvaluator(ArrayList<String> lineW, ArrayList<String> stopW)
  {
    textWords = lineW;
    stopWords = stopW;
    String[] sentence;
    boolean isStop, exist;
    ArrayList<String> allWords, realText, textFinal, stopFinal, realStop;
    allWords = new ArrayList<>();
    realText = new ArrayList<>();
    realStop = new ArrayList<>();
    textFinal = new ArrayList<>();
    stopFinal = new ArrayList<>();
    for(int i = 0; i < textWords.size(); i++)
    {
    	sentence = textWords.get(i).split("[. ,;!?\t-:]+");
    	for(int j = 0; j < sentence.length; j++)
    	{
    		sentence[j] = sentence[j].toLowerCase();
    		allWords.add(sentence[j]);
    	}
    }
    for(int i = 0; i < allWords.size(); i++)
    {
    	isStop = false;
    	for(int j = 0; j < stopWords.size(); j++)
    	{
    		if(allWords.get(i).equals(stopWords.get(j)))
    		{
    			isStop = true;
    		}
    	}
    	if(!isStop)
		{
			realText.add(allWords.get(i));	
		}
		else
		{
			realStop.add(allWords.get(i));
		}
    }
    for(int i = 0; i < realText.size(); i++)
    {
    	exist = false;
    	for(int j = 0; j < textFinal.size(); j++)
    	{
    		String x, y;
    		x = realText.get(i).toString();
    		y = textFinal.get(j).toString();
    		if(x.equals(y))
    		{
    			exist = true;
    		}
    	}
    	if(!exist)
    	{
    		textFinal.add(realText.get(i));
    	}
    }
    for(int i = 0; i < realStop.size(); i++)
    {
    	exist = false;
    	for(int j = 0; j < stopFinal.size(); j++)
    	{
    		String x, y;
    		x = realStop.get(i).toString();
    		y = stopFinal.get(j).toString();
    		if(x.equals(y))
    		{
    			exist = true;
    		}
    	}
    	if(!exist)
    	{
    		stopFinal.add(realStop.get(i));
    	}
   	}
   	int[] theSameWord, theSameStop;
   	theSameWord = new int[textFinal.size()];
   	theSameStop = new int[stopFinal.size()];
   	for(int i = 0; i < realText.size(); i++)
   	{
   		for(int j = 0; j < textFinal.size(); j++)
   		{
   			if(realText.get(i).equals(textFinal.get(j)))
   			{
   				theSameWord[j] += 1;
   			}
   		}
   	}
   	for(int i = 0; i < realStop.size(); i++)
   	{
   		for(int j = 0;j < stopFinal.size(); j++)
   		{
   			if(realStop.get(i).equals(stopFinal.get(j)))
   			{
   				theSameStop[j] += 1;
   			}
   		}
   	}
   	textMap = new TreeMap<>();
    for(int i = 0; i < textFinal.size(); i++)
    {
    	textMap.put(textFinal.get(i), theSameWord[i]);
    }
    Set<Entry<String, Integer>> entradasText = textMap.entrySet();
    textArray = new ArrayList<>();
    textArray.addAll(entradasText);
    textArray.sort( new Comparator<Entry<String, Integer>>() {
        @Override
        public int compare( Entry<String, Integer> o1, Entry<String, Integer> o2 ) {
            return -o1.getValue().compareTo( o2.getValue() );
        }
    });
    stopMap = new TreeMap<>();
    for(int i = 0; i < stopFinal.size(); i++)
    {
    	stopMap.put(stopFinal.get(i), theSameStop[i]);
    }
    Set<Entry<String, Integer>> entradasStop = stopMap.entrySet();
    stopArray = new ArrayList<>();
    stopArray.addAll(entradasStop);
    stopArray.sort( new Comparator<Entry<String, Integer>>() {
        @Override
        public int compare( Entry<String, Integer> o1, Entry<String, Integer> o2 ) {
            return -o1.getValue().compareTo( o2.getValue() );
        }
    });
  }

  public int getNumeroDeLinhas()
  {
    int result;
    result = 0;
    String[] lines;
    for(int i = 0; i < textWords.size(); i++)
    {
    	lines = textWords.get(i).split("\n");
        result += lines.length;
    }
    return result;
  }

  public int getNumeroDePalavras()
  {
    int result;
    result = 0;
    String[] words;
    for(int i = 0; i < textWords.size(); i++)
    {
    	words = textWords.get(i).split("[. ,;!?\t-:]+");
        result += words.length;
    }
    return result;
  }

  public int getNumeroDePalavrasDistintas()
  {
    int result;
    boolean exist;
    String[] words;
    ArrayList<String> allText, finalText;
    result = 0;
    allText = new ArrayList<>();
    finalText = new ArrayList<>();
    for(int i = 0; i < textWords.size(); i++)
    {
    	words = textWords.get(i).split("[. ,;!?\t-:]+");
    	for(int j = 0; j < words.length; j++)
    	{
    		words[j] = words[j].toLowerCase();
    		allText.add(words[j]);	
    	}
    }
    for(int i = 0; i < allText.size(); i++)
    {
    	exist = false;
    	for(int j = 0; j < finalText.size(); j++)
    	{
    		String x, y;
    		x = allText.get(i).toString();
    		y = finalText.get(j).toString();
    		if(x.equals(y))
    		{
    			exist = true;
    		}
    	}
    	if(!exist)
    	{
    		result += 1;
    		finalText.add(allText.get(i));
    	}
    }
    return result;
  }

  public ArrayList<String> getPalavrasMaisFrequentes(int n)
  {
   	ArrayList<String> result;
   	result = new ArrayList<>();
   	for(int i = 0; i < n; i++)
   	{
   		result.add(textArray.get(i).getKey());
   	}
    return result;
  }

  public ArrayList<String> getStopWordsMaisFrequentes(int n)
  {
    ArrayList<String> result;
    result = new ArrayList<String>();
    for(int i = 0; i < n; i++)
   	{
   		result.add(stopArray.get(i).getKey());
   	}
    return result;
  }

  public Map<String,Integer> getFrequenciaDePalavras()
  {
    Map<String,Integer> result;
    result = new TreeMap<>();
    result = textMap;
    return result;
  }

  public Map<String,Integer> getFrequenciaDeStopWords()
  {
    Map<String,Integer> result;
    result = new TreeMap<>();
    result = stopMap;
    return result;
  }
}
