/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package ozdenfinalpractice;
import java.util.Arrays;
import java.util.Random;
/**
 *
 * @author aaronfeinberg
 */
public class MinMaxArray {
    public static void main (String[] args){
        Random rand = new Random();
        int[] nums = new int[10];
        int max=0;
        int min=100;
        
        //populate array
        for(int i = 0; i<nums.length;i++){
            nums[i]=rand.nextInt(100);
        }
        
        System.out.println(Arrays.toString(nums));

        for(int i=0;i<nums.length;i++){
            if(nums[i]>max){
                max=nums[i];
            }
            
            if(nums[i]<min){
                min=nums[i];
            }
        }
        
        System.out.println(max);
        System.out.println(min);
    
    }
    
}
