/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package question_4;

/**
 *
 * @author aaronfeinberg
 */
public class Program {

    /**
     * @param args the command line arguments
     */
    public static void main(String[] args) {
        // TODO code application logic here
        
        Bank pnc = new Bank(); //instantiating new bank to handle transfers 
        Account barisManco = new Account("Baris Manco", 500.00);    //creating account for baris
        Account sezenAksu = new Account("Sezen Aksu", 400.00);     // creating account for sezen
        
        //testing to check if transfer is blocked due to insufficient funds 
        System.out.println("<Testing Invalid transfer (overdraft): >");
        pnc.transfer(barisManco, sezenAksu, 600.00);    //transfering 600.00 from baris to sezen
        barisManco.printAccount();      //outputing account information for baris
        sezenAksu.printAccount();       //outputing account information for sezen
        System.out.println("Fees Collected: "+pnc.getCollectedFees()); //printing collected fees to screen
        
        //testing a valid transfer
        System.out.println("\n<Testing valid Transfer: >");
        pnc.transfer(sezenAksu, barisManco, 50.52);     //transfering 50.52 from sezen to baris
        barisManco.printAccount();      //outputing account information for baris
        sezenAksu.printAccount();       //outputing account information for sezen
        System.out.println("Fees Collected: "+pnc.getCollectedFees());//printing collected fees to screen
        
        
        //testing a valid transfer
        System.out.println("\n<Testing valid Transfer (opposite direction): >");
        pnc.transfer(barisManco, sezenAksu, 50.52);     //trhansfering 50.52 from baris to sezen
        barisManco.printAccount();      //outputing account information for baris
        sezenAksu.printAccount();       //outputing account information for sezen
        System.out.println("Fees Collected: "+pnc.getCollectedFees()); //printing collected fees to screen
    }
         
}
