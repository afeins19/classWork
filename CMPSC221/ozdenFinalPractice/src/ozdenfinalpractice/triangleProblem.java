/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package ozdenfinalpractice;

/**
 *
 * @author aaronfeinberg
 */
public class triangleProblem {

    /**
     * @param args the command line arguments
     */
    public static void main(String[] args) {
        // TODO code application logic here
        //point p
        int px=1;
        int py=2;
        
        double abc = area(0,0,0,5,5,0);
        double pbc = area(1,2,0,5,5,0);
        double pac = area (0,0,1,2,0,5);
        
    }
    
    public static double area(int x1, int y1, int x2, int y2, int x3, int y3){
        return Math.abs((x1*(y2-y3) + x2*(y3-y1)+ 
                                    x3*(y1-y2))/2.0); 
    }
    
    
}
