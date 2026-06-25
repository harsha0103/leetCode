// Last updated: 6/25/2026, 9:11:07 AM
object Solution {
    def freqAlphabets(s: String): String = {
      var len= s.length
        print(len)
        var res=""
        var i= len-1
        while (i>=0)
        {
            if(s(i)!= '#')
            {
            print(i+"=")
            var x=s(i).toInt+48
            println(x.toChar)
             res=res+x.toChar
            i=i-1   
                
            }
            else
            {
                print(i+"=")
               var x=(s(i-2)+""+s(i-1)).toInt+96
                 println(x.toChar)
                res=res+x.toChar
                i=i-3
            }
        }
        
        res.reverse
    }
}