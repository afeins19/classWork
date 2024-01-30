/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package question_4;

/**
 * @author aaronfeinberg
 */

/****************************************
*this class describes the account of a  *
*user. It stores vars such as name      *
* and account balance                   *
*/

public class Account {
   
    private String name;        //stores account holders name 
    private double balance;    //stores account holders balance 

    public Account(String name, double balance) {
        //forces assignment of vars through setter methods 
        setName(name);  //passes name to name setter method 
        setBalance(balance); //passes balance to balance setter method 
    }
    
    //this method will print the account holders name and balance 
    public void printAccount(){ 
        System.out.println("\n"+this.getName()+": ");   //printing name 
        System.out.printf("$%.2f",this.getBalance());   //printing balance in currency format 
       System.out.println("\n");    //newline 
    }
    
    //returns private variable name
    public String getName() {
        return name;
    }
    
    //sets value of name
    public void setName(String name) {
        if(name=="")    //defaults name to "jerry" if no name is given
        {
            this.name = "Jerry";   //setting name to jerry 
        }
        
        else{
            this.name = name;   //otherwise sets name to the given value
        }
    }

    //returns private variable balance
    public double getBalance() {
        return balance; //returns balance
    }
    
    //sets balance of current account 
    private void setBalance(double balance) {
        if(balance < 0){    //prevents user from setting negative balance
            this.balance=0; 
            System.out.println("ERROR: Balance Cannot be a Negative Value");    //error message to user  
            System.out.println("-> Balance was set to 0");      //informs major to zero 
        }
        
        else{
            this.balance=balance; //sets balance if it value > 0
        }
           
    }
    
    //method for depositing funds int o account
    public void deposit(double depositAmount){
        //notifies user if input value less than 0
        if(depositAmount <= 0){     
            System.out.println("ERROR: Deposit Must be greater than 0 "); //informs user that value must be greater than 0
            System.out.println("-> Deposit was voided");    //informs user deposit was voided 
        }
        
        else{
            setBalance(getBalance()+depositAmount); //sets the new balance value as old balance plus deposited amount 
        }
    }
    
    //method for withdrawing funds 
    public void withdraw(double withdrawAmount){
        //checks to see if withdraw amount is valid (>0) 
        if(withdrawAmount <= 0)
        {
           //error, informs user that they must input a value greater than 0 
           System.out.println("ERROR: Please enter a value greater than 0");
        }
        
        //makes sure that user cannot withdraw more than his or her current balance
        else if(withdrawAmount > getBalance()){  
            System.out.println("ERROR: Insufficient Funds");    //informs user about insufficient funds 
            System.out.println("->Withdrawl Voided");           //informs user withdrawl is voided 
        }
        
        //sets the balance to the current balance minus amount withdrawn 
        else{
            setBalance(getBalance()-withdrawAmount);
        }
    
    }
}
