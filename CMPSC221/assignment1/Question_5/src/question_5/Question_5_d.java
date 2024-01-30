/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package question_5;
/**
 *
 * @author aaronfeinberg
 */


public class Question_5_d {

    /**
     * @param args the command line arguments
     */
    
         /*********************************
        *Part D: Program will loop over   *
        * values from -2 to 2 and preform *      
        *preform some operations on them  *
        ***********************************
        */
    public static void main(String[] args) {
        // TODO code application logic here
        
      
        
        System.out.println("Table of Values: \n");  //prints "Table of Values"
        System.out.println("|i    | i*10| |i| | i^2 |"); //prints table header 
        System.out.print("--------------------------"); //separating table header  
        for(int i=-2; i<=2; i++)  //decalring loop to run from -2 to 2
        {
           if(i==0){    //case when i==9
               continue;    //breaks one iteration of the loop thus skiping i=0
           }
           else{ //for all cases except i=0, the code bellow is executed 
               System.out.print("\n");        //newline 
               System.out.print("|");        //wall
               System.out.printf("%-5s",i);  //printing i
               System.out.print("|");        //wall 
               System.out.printf("%-5s",i*10);  //printing i*10
               System.out.print("|");           //wall 
               System.out.printf("%-5s",Math.abs(i));  //printing absolute value of i
               System.out.print("|");                   //wall
               System.out.printf("%-5s",(int)Math.pow(i,2));        //printing i^2
               System.out.print("|");       //wall 
           }
        }
        
    }
    
}
