// Last updated: 6/25/2026, 9:18:20 AM
object Solution {
    def romanToInt(s: String): Int = {
        var length= s.length
        var result=0

        for ( i <- 0 to length-1)
        { 
          var number= test(s.charAt(i).toString)
            if(i!=length-1)
            {
              if(number<test(s.charAt(i+1).toString)){
               number= -1* number
              } 

            }
          result =result+number
        }
        result

      }
      def test(s:String):Int={
            var number= s match{
            case "I" => 1
            case "V" => 5
            case "X" => 10
            case "L" => 50
            case "C" => 100
            case "D" => 500
            case "M" => 1000
            case _=> 24
          }
        number 
   
  }
}