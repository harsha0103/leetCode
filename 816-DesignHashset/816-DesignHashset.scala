// Last updated: 6/25/2026, 9:12:35 AM
class MyHashSet() {

    /** Initialize your data structure here. */
    
        import scala.collection.mutable.ListBuffer
        var list = new ListBuffer[Int]()
    def add(key: Int) {
    
        if (!list.contains(key))
        {list +=key}
        
    }

    def remove(key: Int) {
       list -=key
    }

    /** Returns true if this set contains the specified element */
    def contains(key: Int): Boolean = {

        list.contains(key)
    }

}

/**
 * Your MyHashSet object will be instantiated and called as such:
 * var obj = new MyHashSet()
 * obj.add(key)
 * obj.remove(key)
 * var param_3 = obj.contains(key)
 */