// Last updated: 6/25/2026, 9:12:53 AM
object Solution {
    def numJewelsInStones(J: String, S: String): Int = {
        
    var result=0
        
    println (S.filter(J.contains(_)).length())
        
    for( x<- J ;y <-  S)
        {
            if (x==y)
            {
                result = result+1
            }
            
        }
    result
    }
}