// Last updated: 6/25/2026, 9:11:55 AM
object Solution {
    def calculateTime(keyboard: String, word: String): Int = {
        val hashmap = keyboard.zipWithIndex.toMap
        var sum = keyboard.indexOf(word(0))
        for (i <- 0 until word.length - 1)
        {
            print(word(i))
            sum += math.abs( keyboard.indexOf(word(i + 1))-keyboard.indexOf(word(i)))
        }
        sum
    }
}