// Last updated: 6/25/2026, 9:17:52 AM
object Solution {
    def search(nums: Array[Int], target: Int): Int = {
        
        if(nums.indexOf(target)!= -1)
        {
            return nums.indexOf(target)
        }
        else
        {
            return -1
        }
        
    }
}