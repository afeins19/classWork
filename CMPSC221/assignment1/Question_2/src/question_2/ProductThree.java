/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package question_2;
import java.util.Scanner;

/**
 *
 * @author aaronfeinberg
 * This program will allow the user to enter 3 variables and output their product 
 */
public class ProductThree {

    /**
     * @param args the command line arguments
     */
    
    //main method for question_2
    public static void main(String[] args) {
        //local vars
        int x;          //first var
        int y;          //second var
        int z;          //third var
        int result;     //stores result 
        
        //instantiate scanner object for reading user input
        Scanner input = new Scanner(System.in);
        
        //prompts user to input first value and assigns value to x (also indicates the stored value)
        System.out.println("Please Enter First Value: ");
        x = input.nextInt(); 
        System.out.println("x = "+x);
       
        //prompts user to input second value and assigns value to y (also indicates the stored value)
        System.out.println("\nPlease Enter Second Value: ");
        y = input.nextInt();
        System.out.println("y = "+y);
        
        //prompts user to input third value and assigns value to z (also indicates the stored value)
        System.out.println("\nPlease Enter Third Value: ");
        z = input.nextInt();
        System.out.println("z = "+z);
        
        //calculates the product x*y*z and stores value in result
        result = x * y * z; 
        System.out.printf("\nProduct is: "+result+"\n");
        

    }
    
}
