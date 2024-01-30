/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package question_1;

/**
 *
 * @author aaronfeinberg
 */
public class InvoiceTest {

    /**
     * @param args the command line arguments
     */
    public static void main(String[] args) {
        // TODO code application logic here
        Invoice myInvoice = new Invoice();      //instantiates new invoice object
        
        /******************************
         * Testing Invoice Class Below*
         ******************************/
        
        //****Sample part****
        myInvoice.setPartNumber("plumbus01");   //setting part number
        myInvoice.setPartDescription("Everyone has a plumbus in thier home...");    //setting a short description
        myInvoice.setQuantity(100);     //setting quantity sold
        myInvoice.setPrice(500);        //setting price per item 
        
        //****Printing Sample part****
        System.out.println("\nPart Number: "+myInvoice.getPartNumber());
        System.out.println("Desciption: "+myInvoice.getPartDescription());
        System.out.println("Price per Item: "+myInvoice.getPrice());
        System.out.println("Amount: "+myInvoice.getQuantity());
       
        
        //Ensuring that the user cannot set a negative price for the item
        myInvoice.setPrice(-10);        //setting item price to -10
        System.out.println("\nPrice:" +myInvoice.getPrice());  //printing item's price
        
        
        //Ensuring user cannot set quantity to a negative value
        myInvoice.setQuantity(-500);    //Setting item quantity to -500
        System.out.println("\nQuantity: "+myInvoice.getQuantity());  //printing item's quantity 
        
       
        //Testing the getInvoiceAmount() method (returngs price * qauntity)
        myInvoice.setPrice(10);     //setting price per item to 10
        myInvoice.setQuantity(50);  //setting total items sold to 50
        //shoud output 500.0 
        System.out.println("\nInvoice Amount: "+myInvoice.getInvoiceAmount()); //prints the output of getInvoiceAmount() to screen
       
        
        
        
        
      
    }
    
}
