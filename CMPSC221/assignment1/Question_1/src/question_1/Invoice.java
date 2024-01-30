package question_1;

/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */

/**
 *
 * @author aaronfeinberg
 */

//Invoice class which keeps data on a specific part such as number, price, description etc.
public class Invoice {
    
    private String partNumber;         //stores part number 
    private String partDescription;   //stores a short description of part
    private int quantity;            //stores quantity of parts puchased
    private double price;           //stores price per item
    
    //constuctor which intializes class vars with starting values
    public Invoice(){
        this.setPartNumber("0");    //intial partnumber
        this.setPrice(0);           //intial price
        this.setQuantity(0);        //initial quantity
        this.setPartDescription("<part_description>");      //intial description
    }   
    
    //returns the total cost of this invoice as a double
    public double getInvoiceAmount(){
        return (this.price * this.quantity);    //returns price * amount
    }
    //returns the private variable partNumber
    public String getPartNumber() {
        return partNumber;
    }
    
    //sets the value of partNumber
    public void setPartNumber(String partNumber) {
        this.partNumber = partNumber;
    }
    
    //returns the private variable partDescription 
    public String getPartDescription() {
        return partDescription;
    }
    
    //sets the value of partNumber
    public void setPartDescription(String partDescription) {
        this.partDescription = partDescription;
    }
   
    //returns the private variable quantity 
    public int getQuantity() {
        return quantity;
    }
    
    //sets the value of quantity
    public void setQuantity(int quantity) {
        //sets quantity to 0 if method recieves a negative input for quantity 
        if(quantity < 0){   
            this.quantity = 0; 
        }
        //if method recieves value > 0, it sets quantity as this value
        else{
            this.quantity = quantity;
        }    
    }
  
    //returns the private variable price
    public double getPrice() {
        return price;
    }
    //sets the value of price
    public void setPrice(double price) {
        //sets price to 0 if user inputs a negative price 
        if(price < 0){   
            this.price = 0; 
        }
        //if method recieves value > 0, it sets price as this value
        else{
            this.price = price;
        } 
    }
    
   
    
}
