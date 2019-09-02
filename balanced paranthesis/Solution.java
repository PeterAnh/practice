import java.io.*;
import java.math.*;
import java.security.*;
import java.text.*;
import java.util.*;
import java.util.concurrent.*;
import java.util.regex.*;
import java.util.StringTokenizer;

public class Solution {


    // Complete the braces function below.
    static String[] braces(String[] values) {
    	
    	int l = values.length;
    	String[] result = new String[l];
        
        for(int i = 0; i < l; i++)
        {
        	Stack<Character> s = new Stack<>();
        	int open = 0;
        	int close = 0;
        	for(int j = 0; j < values[i].length(); j++)
        	{
        		char current = values[i].charAt(j);
        		
        		if(current == '{' || current == '(' || current == '[' )
        		{
        			s.push(current);
        			open++;
        			continue;
        		}
        		
        		if(current == '}')
        		{
        			close++;
        			if(!s.isEmpty() && s.peek() == '{')
        			{
        				s.pop();
        			}
        		}
        		
        		if(current == ']')
        		{
        			close++;
        			if(!s.isEmpty() && s.peek() == '[')
        			{
        				s.pop();
        			}
        		}
        		
        		if(current == ')')
        		{
        			close++;
        			if(!s.isEmpty() && s.peek() == '(')
        			{
        				s.pop();
        			}
        		}
        	}
        	
        	if(s.isEmpty())
        	{
        		if(open - close == 0)
        		{
        			result[i] = "YES";
        		} else {
        			result[i] = "NO";
        		}
        	} else {
        		result[i] = "NO";
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