// Last updated: 6/25/2026, 9:12:26 AM
object Solution {
    def binaryGap(N: Int): Int = {
        var m =N
        var s=List[Int]()
        var x=""
        while (m>=1)
        {
            if (m%2==0)
            {
                //print("0")
                
                s=0::s
                x= "0"+x
            }
            else {
                //print("1")
                s=1::s
                x="1"+x
            }
            m=m/2
        }
        var result=0
        while(x.indexOf("1") != -1)
        {
            var pre=x.indexOf("1")
            x=x.substring(pre+1)
            println("substring="+x)
            var bre=x.indexOf("1")
            println("bre="+bre)
            if(pre!= -1 && bre != -1 && bre>= result )
            {
                result = bre+1
                println("result = "+result)
                x=x.substring(bre)
            }
        }
        result
 
    }
}