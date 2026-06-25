// Last updated: 6/25/2026, 9:14:15 AM
object Solution {
    def intersection(nums1: Array[Int], nums2: Array[Int]): Array[Int] = {
        List(nums1,nums2).reduce((a,b) => a intersect b).toSet.toArray
        
    }
}