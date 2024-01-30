/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */

/**
 *
 * @author aaronfeinberg
 */
public class Main {

    /**
     * @param args the command line arguments
     */
    public static void main(String[] args) {
        // TODO code application logic here
       
        
        int total = 0; 
        for(int i = 0; i <= 10; i++)
        {
            //we are skipping the number 3 here 
            if(i%3==0){
                continue;
            }
            total+=i;
        }
        System.out.println(total);
    }
    
}
