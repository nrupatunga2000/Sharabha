// You are given an integer array arr[]. The task is to find the sum of it.

// Examples:

// Input: arr[] = [1, 2, 3, 4]
// Output: 10
// Explanation: 1 + 2 + 3 + 4 = 10.
// Input: arr[] = [1, 3, 3]
// Output: 7
// Explanation: 1 + 3 + 3 = 7.

public class gfg1 {
public static void main(String[] args) {
    int [] arr = {1,2,3,4};
    int result = 0;
    for(int i=0;i<arr.length;i++){
        result += arr[i];
        
    }
    System.out.println(result);
    
}
    
}