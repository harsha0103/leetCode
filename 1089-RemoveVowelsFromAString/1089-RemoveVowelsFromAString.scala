// Last updated: 6/25/2026, 9:11:59 AM
object Solution {
    def removeVowels(s: String): String = {
        var list=List("a","e","i","o","u")
        var x=s
        for (i <- list)
        {x=x.toLowerCase.replace(i,"")}
        x
    }
}