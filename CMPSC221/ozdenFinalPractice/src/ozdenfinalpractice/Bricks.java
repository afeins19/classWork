/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package ozdenfinalpractice;
import java.util.Scanner;
/**
 *
 * @author aaronfeinberg
 */
public class Bricks {
    public static void main (String[] args){
        Scanner reader = new Scanner(System.in);
        
        System.out.println("Please input tower height: ");
        
        int height = reader.nextInt();
        int largeBricks = height / 5;
        int smallBricks = height % 5;
        
        System.out.println(largeBricks);
        System.out.println(smallBricks);
        
    }
}
