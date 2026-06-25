// Last updated: 6/25/2026, 9:10:53 AM
object Solution {
    def kidsWithCandies(candies: Array[Int], extraCandies: Int): Array[Boolean] = {
        candies.map(x=> x*x).foreach(println)
        candies.map(_+extraCandies >= candies.max)
    }
}