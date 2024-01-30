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
public class shuffleArray {
    public static void main(String[] args){
        int[] nums = {1,2,3,4,5,6};
        Random rand = new Random();
        
        for(int i = 0; i<nums.length-1; i++){
            int r = rand.nextInt(nums.length);
            int temp = nums[i];
            nums[i]=nums[r];
            nums[r]=temp;
            System.out.println(Arrays.toString(nums));
        }
        
    
    }
          
}
