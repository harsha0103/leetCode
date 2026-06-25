// Last updated: 6/25/2026, 9:17:14 AM
import scala.util.{Failure, Success, Try}
object Solution {
    def isNumber(s: String): Boolean = {

 Try(s.toDouble) match {
      case Success(_) =>
        s.filter(_.isLetter).forall(_.toLower == 'e')
      case Failure(_) => false
    }
}
}