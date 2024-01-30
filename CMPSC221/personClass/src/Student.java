/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */

/**
 *
 * @author aaronfeinberg
 */
public class Student extends Person{
    public String major;
    
    public Student(String name, int age, String major){
        super(name, age);
        this.major = major;
    }
}
