import java.util.Map;
import java.util.Scanner;
import java.util.TreeMap;
import java.lang.reflect.Method;
import java.lang.reflect.InvocationTargetException; 
import java.util.Set;

public class HandleForm
{
    public static Object processInputs() throws Exception
    {
        try(Scanner scan = new Scanner(System.in);)
        {
            Object completeForm = null;
            Map<String, String> kValues = new TreeMap<>();
            String inputs = scan.nextLine();
            String[] parts = inputs.split("[:,]");
            int counter = 0;
            for(int i = 0; i < parts.length; i++)
            {
              parts[i] = parts[i].replaceAll("\"", "");
            }
            while(counter < parts.length-1)
            {
              kValues.put(parts[counter], parts[counter+1]);
              counter += 2;
            }
            completeForm = instantiateForm(kValues.get("class"), kValues);
            return completeForm;
        }
    }

    public static Object instantiateForm(String className, Map<String, String> fields) throws Exception
    {
      Class<?> c;
      try 
      {
        c = Class.forName(className);
      } 
      catch (ClassNotFoundException e) 
      {
        return null;
      }
      String methodName = "";
      try
      {
        Set<String> kMap = fields.keySet();
        Object finalObj = c.newInstance();
        for(String key: kMap)
        {
          if(!key.equals("class"))
          {
            methodName = key; 
            methodName = methodName.substring(0,1).toUpperCase() + methodName.substring(1);
            Method m = c.getMethod("set"+methodName, String.class);
            m.invoke(finalObj, fields.get(key));
          }
        }
        return finalObj;
      }
      catch(Exception e)
      {
        methodName = methodName.toLowerCase();
        throw new Exception("Field not find " + methodName + " in " + className);
      }
    }
}
