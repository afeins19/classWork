/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package hello_world;

/**
 *
 * @author aaronfeinberg
 */
public class SayHello{
    
    public SayHello(){
        System.out.println("Sezek Turkman");
}
    private static double total_value = 123.50;
    
    public double getValue(){
        return total_value; 
    }
    
    public void setValue(double val){
        total_value = val; 
    }   
    public void printAccount(){
        System.out.println();
    }
    
}
