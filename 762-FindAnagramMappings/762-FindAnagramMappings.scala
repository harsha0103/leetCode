// Last updated: 6/25/2026, 9:12:50 AM
object Solution {
    def anagramMappings(A: Array[Int], B: Array[Int]): Array[Int] = {
        print(A.length)
        for (i<- 0 to A.length-1){
            var temp=B.indexOf(A(i))
            A(i)=temp
        }
        
        return A
        
    }
}