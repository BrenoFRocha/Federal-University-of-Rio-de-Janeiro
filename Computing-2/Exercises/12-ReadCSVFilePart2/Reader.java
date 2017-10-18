import java.nio.charset.Charset;
import java.nio.file.Path;
import java.util.Map;
import java.util.TreeMap;
import java.util.List;
import java.lang.reflect.Method;
import java.nio.file.Files;

public class Reader
{
	Map<String, Map<Integer, ?>> readFile(Path p, Charset c, String separator) throws Exception
	{
		Map<String, Map<Integer, ?>> result = new TreeMap<>();
		Map<Integer, Object> tempMap = new TreeMap<>();
		List<String> file = Files.readAllLines(p, c);
		String[] fields = null;
		Class<?> clazz = null;
		boolean start = false;
		Object currentObj = null;
		String className = null;
		String cField = null;
		String cPart = null;
		int cID = 0;

		for(String line : file) 
		{   
			if(line.isEmpty())
			{
				start = false;
			}
			else
			{
				if(start)
				{
					String[] parts = line.split(separator);	
					for(int i = 0; i < parts.length; i++)
					{
						cField = fields[i];
						cPart = parts[i];
						if(cField.equals("class"))
						{
							clazz = Class.forName(cPart);
							className = cPart;
							currentObj = clazz.newInstance();
						}
						else if(cField.equals("id"))
						{
							cID = Integer.parseInt(cPart);
						}
					}					
					for(int i = 0; i < parts.length; i++)
					{
						cField = fields[i];
						cPart = parts[i];
						if(!cField.equals("class"))
						{
							try
							{
								Method m;
								if(cField.equals("email"))
								{
									m = clazz.getMethod("setEMail", String.class);
								}
								else if(cField.equals("id"))
								{
								    m = clazz.getMethod("setId", Integer.class);
								}
								else
								{
									m = clazz.getMethod("set"+(cField.substring(0,1).toUpperCase() + cField.substring(1)), String.class);
								}
								if(cField.equals("id"))
								{
								    m.invoke(currentObj, cID);
								}
								else
								{
								    m.invoke(currentObj, cPart);
								}
							}
							catch(Exception e)
							{
								throw new Exception("Campo " + cField + " não encontrado na classe " + clazz.getName());
							}
						}
					}
					if(result.containsKey(className))
					{
						@SuppressWarnings("unchecked")
						Map<Integer, Object> temp = (Map<Integer,Object>) result.get(className);
						tempMap = temp;
					}
					else
					{
						tempMap = new TreeMap<>();
					}
					tempMap.put(cID, currentObj);
					result.put(className, tempMap);
				}         
				else
				{
					fields = line.split(separator);
					start = true;
				}
			}
		}
		return result;
	}
}