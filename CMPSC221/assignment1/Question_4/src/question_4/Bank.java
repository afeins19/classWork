/*
 *This class will facilitate the transfer of funds between accounts and will 
 *function as a bank. It also collects revenue from each transaction and
 *tracks said revenue with the variable collectedFees 
 */
package question_4;



/**
 *
 * @author aaronfeinberg
 */

    /*******************
     * This class facilitates the transfer of 
     * funds between accounts 
     */


public class Bank {
   
    //Bank class constructor 
    public Bank(){
        this.collectedFees=0; //initializing fees which bank collects from transactions to 0
    }
   
    private static final double transFee=5;   //setting a 5 dollar transfer fee
    private double collectedFees;   //tracks revenue from transfers 

    //method which returns value of collectedFees
    public double getCollectedFees() {
        return collectedFees;
    }

    //method which updates value of collectedFees 
    public void setCollectedFees(double collectedFees) {
        this.collectedFees = collectedFees;
    }
   
    //method which transfers money between account holders 
    public void transfer(Account send, Account recieve, double amount){ //taking in 2 account objects and a double as input 
        if(amount+transFee>send.getBalance()) //making sure that the sender has suffiecient funds for the transaction and the bank fee
        {
            System.out.println("ERROR: Insufficient Funds"); //erro message regarding low funds
            System.out.println("->Transfer Void\n"); //erro message regarding low funds
        }
       
        //withdrawl procedure 
        else{
            send.withdraw(amount+transFee);                  //withdraws selected amount AND banks transfer fee
            recieve.deposit(amount);                        //deposits amount into recieving account
            setCollectedFees(getCollectedFees()+5);        //adds 5 dollars to banks fee account (collectedFees)
            System.out.println("\nSuccesfully Deposited "
                    +amount+" into "+ 
                    recieve.getName()+"'s"+" account.\n");   //outputs the nature of the transaction 
        }
    
    }
    
    
}
