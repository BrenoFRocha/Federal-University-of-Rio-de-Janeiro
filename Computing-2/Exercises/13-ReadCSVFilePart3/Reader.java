import java.sql.Timestamp;
import java.util.ArrayList;
import java.io.IOException;
import java.nio.charset.Charset;
import java.util.Arrays;
import java.nio.file.Files;
import java.nio.file.Path;
import java.nio.file.Paths;
import java.util.List;

public class Reader
{
	public static class Data 
	{
		Timestamp[] ts;
		String[] nameColumn;
		double[][] columns;

		public void setTimeStamp(Timestamp[] newTS)
		{
			this.ts = newTS;
		}
		public void setColumnName(String[] newCN)
		{
			this.nameColumn = newCN;
		}
		public void setColumn(double[][] newC)
		{
			this.columns = newC;
		}
	}
	
	public Data readFromFile(String fileName, String separatorChar) throws IOException
	{
		Data result = new Data();
		Path p = Paths.get("", fileName);
		Charset c = Charset.forName("UTF-8");
		List<String> file = Files.readAllLines(p, c);
		ArrayList<Timestamp> timeStamp = new ArrayList<>();
		boolean start = false, sWrong = true;
		String[] fields = null;
		double[][] columns = null;
		int currentID = 0, lowPos = 0, highPos = 0;
		for(String line : file) 
		{  
			if(start)
			{
				String[] parts = line.split("[" + separatorChar + "]");
				int indexF = 0;
				for(int i = 0; i < parts.length; i++)
				{
					if(fields[i].equals("ts"))
					{
						timeStamp.add(Timestamp.valueOf(parts[i]));
					}
					else
					{
						columns[indexF][currentID] = Double.parseDouble(parts[i]);
						indexF += 1;
					}
				}
				currentID += 1;
			}
			else
			{
				fields = line.split("[" + separatorChar + "]");
				for(int i = 0; i < fields.length; i++)
				{
					if(fields[i].equals("timestamp") || fields[i].equals("datahora") || fields[i].equals("time-stamp"))
					{
						fields[i] = "ts";
					}
					else if(fields[i].equals("average") || fields[i].equals("media") || fields[i].equals("média") || fields[i].equals("preco_medio"))
					{
						fields[i] = "avg";
					}
					else if(fields[i].equals("abertura") || fields[i].equals("o"))
					{
						fields[i] = "open";
					}
					else if(fields[i].equals("max") || fields[i].equals("máximo") || fields[i].equals("maximo"))
					{
						fields[i] = "high";
					}
					else if(fields[i].equals("min") || fields[i].equals("mínima"))
					{
						fields[i] = "low";
					}
					else if(fields[i].equals("fecho") || fields[i].equals("fechamento"))
					{
						fields[i] = "close";
					}
					else if(fields[i].equals("volume"))
					{
						fields[i] = "vol";
					}
				}
				columns = new double[fields.length-1][file.size()-1];
				start = true;
			}
		}
		ArrayList<String> formatFields = new ArrayList<String>(Arrays.asList(fields));
		Timestamp[] formatTS = timeStamp.toArray(new Timestamp[0]);
		formatFields.remove("ts");
		fields = formatFields.toArray(new String[0]);
		for(int i = 0; i < fields.length; i++)
		{
			if(fields[i].equals("low"))
			{
				lowPos = i;
			}
			else if(fields[i].equals("high"))
			{
				highPos = i;
			}
		}
		if(highPos > lowPos)
		{
			double[] hC = columns[highPos];
			double[] lC = columns[lowPos];
			columns[lowPos] = hC;
			columns[highPos] = lC;
			fields[lowPos] = "high";
			fields[highPos] = "low";
		}
		int mainPos = -1;
		int secundaryPos = -1;
		for(int i = 0; i < fields.length; i++)
		{
			if(fields[i].equals("vol") || fields[i].equals("close") || fields[i].equals("open") || fields[i].equals("low") || fields[i].equals("high") || fields[i].equals("avg"))
			{
				mainPos = i;
			}
			else if(secundaryPos == -1)
			{
				secundaryPos = i;
			}
		}
		if(mainPos > secundaryPos && secundaryPos != -1)
		{
			String[] auxS = new String[fields.length];
			auxS[0] = fields[mainPos];
			int aux = 1;
			for(int i = 0; i < fields.length; i++)
			{
				if(!fields[i].equals(fields[mainPos]))
				{
					auxS[aux] = fields[i];
					aux += 1;
				}
			}
			fields = auxS;
			double[][] auxC = new double[fields.length][file.size()-1];
			auxC[0] = columns[mainPos];
			aux = 1;
			for(int i = 0; i < columns.length; i++)
			{
				if(columns[i] != columns[mainPos])
				{
					auxC[aux] = columns[i];
					aux += 1;
				}
			}
			columns = auxC;
		}
		if(fields.length >= 8)
		{
			if(fields[6].equals("ts_min"))
			{
				String[] auxS = fields;
				int aux = 0;
				for(int i = 1; i < 6; i++)
				{
					auxS[aux] = fields[i];
					aux += 1; 
				}
				auxS[5] = "vol";
				fields = auxS;
				double[][] auxC = columns;
				aux = 0;
				double[] fix = columns[0];
				for(int i = 1; i < 6; i++)
				{
					auxC[aux] = columns[i];
					aux += 1;
				}
				auxC[5] = fix;
				columns = auxC;
			}
		}
		result.setTimeStamp(formatTS);
		result.setColumnName(fields);
		result.setColumn(columns);
		return result;
	}
}