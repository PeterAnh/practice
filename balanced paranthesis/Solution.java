import java.util.*;
import java.util.StringTokenizer;

public class Solution {


    // Complete the braces function below.
    static String[] braces(String[] values) {
    	
    	int l = values.length;
    	String[] result = new String[l];
        HashMap<Character, Character> brackets = new HashMap<>();
        brackets.put('(',')');
        brackets.put('[',']');
        brackets.put('{','}');
        
        for(int i = 0; i < l; i++)
        {
        	Stack<Character> s = new Stack<>();
        	for(int j = 0; j < values[i].length(); j++)
        	{
        		char current = values[i].charAt(j);
        		if(brackets.containsKey(current))
        		{
        			s.push(current);
        		} else if(brackets.get(s.pop()) != current)
        		{
        			result[i] = "NO";
        			break;
        		}
        		
        		if(s.empty())
        		{
        			result[i] = "YES";
        		} else {
        			result[i] = "NO";
        		}
        	}
        }
        
        return result;
    }

    private static final Scanner scanner = new Scanner(System.in);
    
    public static void main (String[] args)
    {
    	System.out.println("Enter number of Strings: ");
    	int s = scanner.nextInt();
    	scanner.nextLine();

    	String input = "";
    	input += scanner.nextLine();
    	
    	String[] test = new String[s];
    	
    	StringTokenizer st = new StringTokenizer(input);
    	
    	int index = 0;
    	while(st.hasMoreTokens())
    	{
    		test[index] = st.nextToken();
    		++index;
    	}
    	
    	for(int i = 0; i < test.length; i++)
    	{
    		System.out.println(test[i]);
    	}
    	
    	String[] result = braces(test);
    	for(int i = 0; i < test.length; i++)
    	{
    		System.out.println(result[i]);
    	}
    }
}