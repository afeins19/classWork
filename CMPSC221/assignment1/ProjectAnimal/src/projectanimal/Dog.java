/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package projectanimal;

/**
 *
 * @author aaronfeinberg
 */
public class Dog extends Animal{
    Dog(){
        legs = 4;
    }
    public void makeSound(){
        System.out.println("Woof");
    }
    
    public void barkSound(){
        System.out.println("Bark"); 
    }
    
          public void move(){
          System.out.println("dog is walking");
      }
}
