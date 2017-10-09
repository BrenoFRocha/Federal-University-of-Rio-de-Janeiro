import java.lang.reflect.Method;
import java.lang.annotation.Annotation;

public class FormTranslator
{
	public String including(Class<?> formClass) throws Exception
	{
		String result = "", label = "", name = "", maxLength = "", required = "";      
		String auxLabel = "", auxName = "", auxLength = "", auxRequired = "";
		boolean newLine = false;
		for (Method m : formClass.getDeclaredMethods()) 
		{
			newLine = false;
			if (m.isAnnotationPresent(Field.class)) 
			{
				Field c = m.getAnnotation(Field.class);
				label = c.label();
				maxLength = Integer.toString(c.maxLength());
				required = String.valueOf(c.required());
				name = m.getName().substring(3).toLowerCase();
		 	}
		 	if(!label.equals("") && !label.equals(auxLabel))
		 	{
		 		result = result + label + "<input type=\"text\"";
		 		newLine = true;
		 	}
		 	if(!name.equals("") && !name.equals(auxName))
		 	{
		 		result = result + " name=\"" + name + "\"";
		 	}
		 	if(!maxLength.equals("0") && !maxLength.equals(auxLength))
		 	{
		 		result = result + " maxlength=\"" + maxLength + "\"";
		 	}
		 	if(required.equals("true") && !required.equals(auxRequired))
		 	{
		 		result = result + " required=\"" + required + "\"";
		 	}
		 	if(newLine)
		 	{
		 		result = result + ">" + System.getProperty("line.separator");
		 	}
		 	auxLabel = label;
		 	auxName = name;
		 	auxLength = maxLength;
		 	auxRequired = required;
		}
		return result;
    }

    public String editor(Object form) throws Exception
    {
		String result = "", label = "", name = "", maxLength = "", required = "", value = "";      
		String auxLabel = "", auxName = "", auxLength = "", auxRequired = "", auxValue = "";
		boolean newLine = false;
		Class<?> formClass = form.getClass();
		for (Method m : formClass.getDeclaredMethods()) 
		{
			newLine = false;
			if (m.isAnnotationPresent(Field.class)) 
			{
				Field c = m.getAnnotation(Field.class);
				String methodName = "";
				Method getValue;
				label = c.label();
				maxLength = Integer.toString(c.maxLength());
				required = String.valueOf(c.required());
				methodName = m.getName().substring(3);
				getValue = formClass.getMethod("get"+methodName);
				value = String.valueOf(getValue.invoke(form));
				name = m.getName().substring(3).toLowerCase();
		 	}
		 	if(!label.equals("") && !label.equals(auxLabel))
		 	{
		 		result = result + label + "<input type=\"text\"";
		 		newLine = true;
		 	}
		 	if(!name.equals("") && !name.equals(auxName))
		 	{
		 		result = result + " name=\"" + name + "\"";
		 	}
		 	if(!value.equals("") && !value.equals(auxValue))
		 	{
		 		result = result + " value=\"" + value +"\"";
		 	}
		 	if(!maxLength.equals("0") && !maxLength.equals(auxLength))
		 	{
		 		result = result + " maxlength=\"" + maxLength + "\"";
		 	}
		 	if(required.equals("true") && !required.equals(auxRequired))
		 	{
		 		result = result + " required=\"" + required + "\"";
		 	}
		 	if(newLine)
		 	{
		 		result = result + ">" + System.getProperty("line.separator");
		 	}
		 	auxLabel = label;
		 	auxName = name;
		 	auxLength = maxLength;
		 	auxRequired = required;
		 	auxValue = value;
		}
    	return result;
    }
}