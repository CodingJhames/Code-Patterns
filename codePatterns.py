
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

# Two Pointers Approach

# Java implemetation

# class Solution {
#     public int[] twoSum(int[] numbers, int target) {
#         int lo=0, hi=numbers.length-1;

#         while (numbers[lo]+numbers[hi]!=target){
#             if (numbers[lo]+numbers[hi]<target){  // sum < target move lo pointer
#                 lo++;
#             } else {                              //else move high pointer
#                 hi--;
#             }
#         }
#         return new int[]{lo+1,hi+1};
#     }
# }

#Python implementation

class Solution:
  def twoSum(self, numbers, target):
      lo, hi = 0, len(numbers) - 1

      while numbers[lo] + numbers[hi] != target:
          if numbers[lo] + numbers[hi] < target:
              lo += 1
          else:
              hi -= 1

      return [lo + 1, hi + 1]


# Prefix Sum 

# Java implemetation

class Solution {
    public int pivotIndex(int[] nums) {
        int sum = 0, leftsum = 0;
        for (int x: nums) sum += x;
        for (int i = 0; i < nums.length; ++i) {
            if (leftsum == sum - leftsum - nums[i]) return i;
            leftsum += nums[i];
        }
        return -1;
    }
}

#Python implementation

class Solution:
  def pivotIndex(self, nums):
      total_sum = sum(nums)
      left_sum = 0

      for i, num in enumerate(nums):
          if left_sum == total_sum - left_sum - num:
              return i
          left_sum += num

      return -1

# Ejemplo de uso:
# solution = Solution()
# nums = [1, 7, 3, 6, 5, 6]
# resultado = solution.pivotIndex(nums)
# print(resultado)

# RollingHash

# Java implemetation

# public class RollingHash 
# { 
#   // d is the number of characters in the input alphabet 
#   public final static int d = 26; 

#   static void search(String pat, String txt, int q) 
#   { 
#     int M = pat.length(); 
#     int N = txt.length(); 
#     int i, j; 
#     int p = 0; // hash value for pattern 
#     int t = 0; // hash value for txt 
#     int h = Math.pow(d,M-1)%q; 

#     // Calculate the hash value of pattern and first 
#     // window of text 
#     for (i = 0; i < M; i++) 
#     { 
#       p = (d*p + pat.charAt(i))%q; 
#       t = (d*t + txt.charAt(i))%q; 
#     } 

#     // Slide the pattern over text one by one 
#     for (i = 0; i <= N - M; i++) 
#     { 

#       // Check the hash values of current window of text 
#       // and pattern. If the hash values match then only 
#       // check for characters on by one 
#       if ( p == t ) 
#       { 
#         /* Check for characters one by one */
#         for (j = 0; j < M; j++) 
#         { 
#           if (txt.charAt(i+j) != pat.charAt(j)) 
#             break; 
#         } 

#         // if p == t and pat[0...M-1] = txt[i, i+1, ...i+M-1] 
#         if (j == M) 
#           System.out.println("Pattern found at index " + i); 
#       } 

#       // Calculate hash value for next window of text: Remove 
#       // leading digit, add trailing digit 
#       if ( i < N-M ) 
#       { 
#         t = (d*(t - txt.charAt(i)*h) + txt.charAt(i+M))%q; 
#       } 
#     } 
#   } 

#   public static void main(String[] args) 
#   { 
#     String txt = "ABCCDEAAB"; 
#     String pat = "CDE"; 
#     int q = 53;
#     search(pat, txt, q); 
#   } 
# }

#Python implementation

class RollingHash:
  # d is the number of characters in the input alphabet
  d = 26

  @staticmethod
  def search(pat, txt, q):
      M = len(pat)
      N = len(txt)
      i, j = 0, 0
      p = 0  # hash value for pattern
      t = 0  # hash value for txt
      h = pow(RollingHash.d, M - 1, q)

      # Calculate the hash value of pattern and the first window of text
      for i in range(M):
          p = (RollingHash.d * p + ord(pat[i])) % q
          t = (RollingHash.d * t + ord(txt[i])) % q

      # Slide the pattern over text one by one
      for i in range(N - M + 1):

          # Check the hash values of the current window of text
          # and pattern. If the hash values match, then only
          # check for characters one by one
          if p == t:
              # Check for characters one by one
              for j in range(M):
                  if txt[i + j] != pat[j]:
                      break

              # If p == t and pat[0...M-1] = txt[i, i+1, ...i+M-1]
              if j == M:
                  print("Pattern found at index", i)

          # Calculate hash value for the next window of text: Remove
          # the leading digit, add the trailing digit
          if i < N - M:
              t = (RollingHash.d * (t - ord(txt[i]) * h) + ord(txt[i + M])) % q


# Example of usage
txt = "ABCCDEAAB"
pat = "CDE"
q = 53
RollingHash.search(pat, txt, q)



