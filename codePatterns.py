
# Modified Binary Search

def binary_search(arr: List[int], target: int) -> int: 
  left, right = 0, len(arr) - 1 
  first_true_index = -1 

# Perform binary search until left and right pointers meet 
  while left <= right: 
    mid = (left + right) // 2 
    if feasible(mid): 
        # If the condition is true at mid index, update first_true_index 
        first_true_index = mid 
        right = mid - 1 
    else: 
        # If the condition is false at mid index, narrow down the search space 
      .  left = mid + 1
      
  return first_true_index

# Java implementation

# public class Solution {
#     public int findMin(int[] num) {
#         if (num == null || num.length == 0) {
#             return 0;
#         }
#         if (num.length == 1) {
#             return num[0];
#         }
#         int start = 0, end = num.length - 1;
#         while (start < end) {
#             int mid = (start + end) / 2;
#             if (mid > 0 && num[mid] < num[mid - 1]) {
#                 return num[mid];
#             }
#             if (num[start] <= num[mid] && num[mid] > num[end]) {
#                 start = mid + 1;
#             } else {
#                 end = mid - 1;
#             }
#         }
#         return num[start];
#     }
# }

# Python implementation

class Solution:
  findMIn( num ):
    if(num==null or num.len == 0):
      return 0
    elif( num.len == 1):
      return num[0]
    start, end = 0, num.len-1
    while( start < end ):
      mid = (start+end) / 2
      if(mid > 0 and num[mid] < num[mid-1]):
        return num[mid]
      elif( num[start] <= num[mid] and num[mid] > num[end]):
        start = mid+1
      else:
        end=mid-1
    return num[start]


# Sliding Window Approach

# class Solution {
#     public int[] maxSum(int[] arr, int k) {
#         // Calculate Sum of initial Window.
#         int res = 0; 
#         for (int i=0; i<k; i++) 
#            res += arr[i]; 


#         /**
#         * Slide for remaining elements and add new element to previous result and remove last element of the previous window.
#         */
#         int curr_sum = res; 
#         for (int i=k; i<n; i++) 
#         { 
#            curr_sum += arr[i] - arr[i-k]; 
#            res = Math.max(res, curr_sum); 
#         } 

#         return res; 
#     }
# }

# Python implementation

class Solucion:
  def maxSum(self, arr, k):
      n = len(arr)

      # Calcular la suma de la ventana inicial.
      res = sum(arr[:k])

      # Deslizarse para los elementos restantes, agregar el nuevo elemento al resultado                anterior y eliminar el último elemento de la ventana anterior.
      curr_sum = res
      for i in range(k, n):
          curr_sum += arr[i] - arr[i - k]
          res = max(res, curr_sum)

      return res















