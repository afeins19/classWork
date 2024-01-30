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
public class Cat implements Animal {
    public void makeSound(){
        System.out.println("Meow"); 
    }
    public void eat(){
        System.out.println("eat");
    }
    
    public void blepSound(){
        System.out.println("blepis"); 
    }
    
          public void move(){
          System.out.println("dog is walking");
      }
}
