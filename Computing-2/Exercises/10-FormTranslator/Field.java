import java.lang.annotation.Retention;
import java.lang.annotation.Target;
import java.lang.annotation.ElementType;
import java.lang.annotation.RetentionPolicy;

@Target({ElementType.METHOD})
@Retention(RetentionPolicy.RUNTIME)
public @interface Field 
{
    int maxLength() default 0;
    boolean required() default false;
    String label();
}