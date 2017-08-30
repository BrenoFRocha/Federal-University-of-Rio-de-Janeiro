import java.util.ArrayList;

public class Main 
{
   public static void main( String[] args ) 
   {
      ArrayList<String> texto = new ArrayList<String>();

      texto.add( "Essa frase tem cinco palavras. Aqui estão mais cinco palavras. " );
      texto.add( "Cinco palavras são bastante razoáveis. Mas muitas juntas tornam-se monótonas." );
      texto.add( "Ouça o que está acontecendo. " );
      texto.add( "A escrita está virando chata. O som dela é desconfortável. " );
      texto.add( "É como um disco quebrado. O ouvido demanda alguma variedade." );
      texto.add( "Agora ouça. Eu vario o tamanho da frase e " + "crio música. Música. A escrita canta. "
              + "Tem um ritmo agradável, melodia, harmonia. " + "Eu uso períodos curtos. E eu uso frases de "
              + "duração média." );
      texto.add( "E às vezes, quando tempo certeza que o leitor " );
      texto.add( "está descansado, irei engaja-lo em uma frase " + "de tamanho considerável, uma frase que queima com "
              + "energia e criando um crescimento impetuoso, um "
              + "som de tambores, uma batida de sílabas - sons que dizem " + "para escutar isso, que é importante." );

      ArrayList<String> stopWords = new ArrayList<String>();

      stopWords.add( "de" );
      stopWords.add( "da" );
      stopWords.add( "do" );
      stopWords.add( "e" );
      stopWords.add( "a" );
      stopWords.add( "o" );
      stopWords.add( "um" );
      stopWords.add( "uma" );
      
      TextEvaluator avt = new TextEvaluator(texto, stopWords);
      
      System.out.println(avt.getFrequenciaDePalavras());
      System.out.println(avt.getFrequenciaDeStopWords());
      System.out.println(avt.getNumeroDeLinhas());
      System.out.println( avt.getNumeroDePalavras() );
      System.out.println(avt.getNumeroDePalavrasDistintas());
      System.out.println( avt.getPalavrasMaisFrequentes(5));
      System.out.println(avt.getStopWordsMaisFrequentes(5));
   }
}
