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

public class Program {

    /**
     * @param args the command line arguments
     */
    public static void main(String[] args) {
        // TODO code application logic here
//        Dog d = new Dog(); 
//        d.eat();

//          //we created two reference variables of type Animal and pointed them to the CAT and DOG objects 
//          Animal a = new Dog();
//          Animal b = new Cat(); 
//          a.makeSound();
//          b.makeSound();
          
          //if we try a.barkSound();, because a is of type animal, we will not be able 
          //to access this method 
          
          //we must create a new class of type 'dog'
          Dog c = new Dog(); 
          c.barkSound();
          //a.move();
          
          
          //Animal animal = new Animal(); -- we changed animal to an abstract class so it cannot be instantiated 
          Animal cat = new Animal(); 
          
          
          
    }
    
    
}
