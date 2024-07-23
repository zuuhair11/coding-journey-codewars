public class ArrayPlusArray001 {
    
  public static int arrayPlusArray(int[] arr1, int[] arr2) {
    
    int arraySum = 0;
    
    for (int i=0; i<arr1.length; i++) {
      
      arraySum = arraySum + (arr1[i]) + (arr2[i]);
      
    }
    
    return arraySum;
  }
}
    
  