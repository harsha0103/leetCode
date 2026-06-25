// Last updated: 6/25/2026, 9:14:14 AM
object Solution {
    def intersect(nums1: Array[Int], nums2: Array[Int]): Array[Int] = {
            List(nums1,nums2).reduce((a, b) => a intersect b)
    }
}