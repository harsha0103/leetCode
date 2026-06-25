// Last updated: 6/25/2026, 9:15:04 AM
object Solution {
    def isAnagram(s: String, t: String): Boolean = {
    var first=s.groupBy(identity).map{case(a,b)=>(a.toString+b.size)}.mkString("")
    var second=t.groupBy(identity).map{case(a,b)=>(a.toString+b.size)}.mkString("")

    return first==second
    }
}