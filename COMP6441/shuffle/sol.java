import java.io.File;
import java.io.FileNotFoundException;
import java.lang.reflect.Array;
import java.util.ArrayList;
import java.util.Scanner;

public class system {
    
	public static void main (String []args){
	File file = new File(args[0]);
	
	try {
		Scanner input = new Scanner(file);
		String sortedArray[] = new String[600];
		while(input.hasNextLine()){
			String currentLine = input.nextLine();
			int number = Integer.parseInt(drawDigitsFromString(currentLine));
			//currentLine.replaceAll("^[0-9]", "");
			//System.out.println(number);
			sortedArray[number] = currentLine;
			for(int i = 0; i < 593;i++){
				System.out.println(sortedArray[i]);
			}
			
		}
		input.close();
	} catch (FileNotFoundException e) {
		// TODO Auto-generated catch block
		e.printStackTrace();
	}
	}
	
	
    //Separate words from String which has gigits
        public static String drawDigitsFromString(String strValue){
            String str = strValue.trim();
            String digits="";
            for (int i = 0; i < str.length(); i++) {
                char chrs = str.charAt(i);              
                if (Character.isDigit(chrs))
                    digits = digits+chrs;
            }
            return digits;
        }
	
}