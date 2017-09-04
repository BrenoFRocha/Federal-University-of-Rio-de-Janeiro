import java.util.Map;
import java.util.TreeMap;

public class Main 
{
    public static void main(String[] args) 
    {
        Map<String, String> equivalentP = new TreeMap<>();

        equivalentP.put("ch", "x");
        equivalentP.put("ç", "s");
        equivalentP.put("s", "z");
        
        EquivalentSound bySound = new EquivalentSound(equivalentP);

        System.out.println(bySound.equivalent("chuchu", "chuxu")); // Equivalent
        System.out.println(bySound.equivalent("atrás", "atraz")); // Not Equivalent

        //EquivalentSound.equivalent returns true if the sound of the words is equivalent.
    }
}