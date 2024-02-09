
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

  
















