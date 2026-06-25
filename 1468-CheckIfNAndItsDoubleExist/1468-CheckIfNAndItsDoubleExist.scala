// Last updated: 6/25/2026, 9:10:59 AM
import scala.util.control.Breaks._
object Solution {
    def checkIfExist(arr: Array[Int]): Boolean = {

        
        for(i<- 0 to arr.length-1; j<-0 to arr.length-1)
         { 
          if( i!=j && arr(i)== 2*arr(j) )
             {  
                 println(i+","+j)
                println(arr(i)+","+arr(j))
                 return true
             }
         
        }
        return false
         
    }
}
