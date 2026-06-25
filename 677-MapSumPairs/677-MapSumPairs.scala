// Last updated: 6/25/2026, 9:13:06 AM
class MapSum() {

    /** Initialize your data structure here. */
    import scala.collection.mutable.HashMap 
         val hashMap1= new HashMap[String, Int]()

    def insert(key: String, `val`: Int) {
      hashMap1 += (key->`val`)
        hashMap1.foreach{
            case(key,value)=> println(key,value)
        }
    }

    def sum(prefix: String): Int = {
        var sum=0
        hashMap1.filterKeys(_.startsWith(prefix)).values.sum     
        
    }

}

/**
 * Your MapSum object will be instantiated and called as such:
 * var obj = new MapSum()
 * obj.insert(key,`val`)
 * var param_2 = obj.sum(prefix)
 */