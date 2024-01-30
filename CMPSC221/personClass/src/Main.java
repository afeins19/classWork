/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
import java.util.*;
/**
 *
 * @author aaronfeinberg
 */
public class Main {
    public static void main(String[] args){
        
        Person mark = new Person("1",2);
        Person jannet = new Person("jannet",35);
        mark = new Person("Mark",22);
        
        List<Person> plist = new ArrayList<Person>(); 
        for(int i =0; i<10; i++){
            plist.add(new Person(Integer.toString(i),i));
        }
        
        for(Person p: plist){
            System.out.println(p.getName()+", "+p.getAge());
        }
    
    }
}
