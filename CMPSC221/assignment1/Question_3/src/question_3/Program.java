/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package question_3;

/**
 *
 * @author aaronfeinberg
 */
public class Program {

    /**
     * @param args the command line arguments
     */
    public static void main(String[] args) {
        
        Account barisManco = new Account("Baris Manco", -10.95);    //creating account for baris
        Account sezenAksu = new Account("Sezen Aksu", 1000.12);     // creating account for sezen
        
        System.out.println("\nUsers: "); //printing users below
        barisManco.printAccount();  //printing baris' account details from printAccount() method
        sezenAksu.printAccount();  //printing sezen's account details from printAccount() method
        
        System.out.println("<Depositing 100 into Boris' account: >"); //depositing test below
        barisManco.deposit(100);    //depositing 100 into Baris' Account
        barisManco.printAccount();  //printing Name and Balance to screen
            
        System.out.println("<Attempting to withdraw 1500 form Sezen's account: >");   //preforming overdraft test
        sezenAksu.withdraw(1500);   //Trying to withdraw more than current balance should void the withdrawl
        sezenAksu.printAccount();  //printing Sezen's Name and Balance to screen
        
        System.out.println("<Withdrawing 200 from Sezen's Account: >");   //preforming a valid withdrawl
        sezenAksu.withdraw(200);  //this is a valid withdrawl and should be reflected in the new blance 
        sezenAksu.printAccount();  //printing Name and Balance to screen
        
    }
    
}
