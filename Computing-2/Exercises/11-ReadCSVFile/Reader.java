import java.nio.charset.Charset;
import java.nio.file.Path;
import java.util.ArrayList;
import java.util.List;
import java.lang.reflect.Method;
import java.nio.file.Files;

public class Reader
{
	ArrayList<Object> readFile(Path p, Charset c, String separator, Class<?> clazz) throws Exception
	{
		ArrayList<Object> finalResult = new ArrayList<>();
		List<String> file = Files.readAllLines(p, c);
		boolean start = false;
		String[] fields = null;
		for(String line : file) 
		{   
			if(start)
			{
				String[] parts = line.split(separator);
				Object currentObj = clazz.newInstance();
				for(int i = 0; i < parts.length; i++)
				{
					String cField = fields[i];
					String cPart = parts[i];
					try
					{
						Method m;
						if(cField.equals("email"))
						{
							m = clazz.getMethod("setEMail", String.class);
						}
						else
						{
							m = clazz.getMethod("set"+(cField.substring(0,1).toUpperCase() + cField.substring(1)), String.class);
						}
						m.invoke(currentObj, cPart);
					}
					catch(Exception e)
					{
						throw new Exception("Campo " + cField + " não encontrado na classe " + clazz.getName());
					}
				}
				finalResult.add(currentObj);
			}         
			else
			{
				fields = line.split(separator);
				start = true;
			}
		}
		return finalResult;
	}
}