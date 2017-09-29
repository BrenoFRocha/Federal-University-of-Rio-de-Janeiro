import java.lang.reflect.Array;
import java.lang.reflect.Constructor;
import java.lang.reflect.InvocationTargetException;
import java.util.ArrayList;

public class Ambient
{
	public static Object instanciar(String className, Object... parameters) throws ClassNotFoundException, InstantiationException,
				IllegalAccessException, NoSuchMethodException, SecurityException, IllegalArgumentException, InvocationTargetException
	{
		try
		{
			Class<?> c = Class.forName(className);
			Class<?>[] classType = new Class<?>[parameters.length];
			Object finalObject;
			Constructor<?> construtor;
			try
			{
				for(int i = 0; i < parameters.length; i++)
				{
					if(parameters[i].getClass() == ArrayList.class)
					{
						classType[i] = java.util.Collection.class;
					}
					else if(parameters[i].getClass() == Integer.class)
					{
						classType[i] = int.class;
					}
					else
					{
						classType[i] = parameters[i].getClass();
					}
				}
				construtor = c.getConstructor(classType);
			}
			catch(Exception e)
			{
				for(int i = 0; i < parameters.length; i++)
				{
					if(parameters[i].getClass() == ArrayList.class)
					{
						classType[i] = java.util.Collection.class;
					}
					else if(parameters[i].getClass() == int.class)
					{
						classType[i] = Integer.class;
					}
					else
					{
						classType[i] = parameters[i].getClass();
					}
				}
				construtor = c.getConstructor(classType);
			}
			finalObject = construtor.newInstance(parameters);
			return finalObject;
		}
		catch(NoSuchMethodException e) 
		{
			return null;
		}
	}
}