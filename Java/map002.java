public class map002 {
    
// Given an array of integers, return a new array with each value doubled.
// For example:
// [1, 2, 3] --> [2, 4, 6]

    public static int[] map(int[] arr) {
  
      int[] dblArr = new int [arr.length];
      
      for (int i=0; i<arr.length; i++) {
        
        dblArr [i] = 2*arr[i];
      }
      return dblArr;
    }
    
  }