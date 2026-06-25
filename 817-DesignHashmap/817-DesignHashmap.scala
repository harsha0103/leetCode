// Last updated: 6/25/2026, 9:12:37 AM
class MyHashMap() {

    /** Initialize your data structure here. */
    
          val table = Array.fill[Int](1000001)(-1)
    /** value will always be non-negative. */
    def put(key: Int, value: Int) {
        table(key)=value
    }

    /** Returns the value to which the specified key is mapped, or -1 if this map contains no mapping for the key */
    def get(key: Int): Int = {
   
            table(key)
  
    }

    /** Removes the mapping of the specified value key if this map contains a mapping for the key */
    def remove(key: Int) {
        table(key)= -1
    }

}

/**
 * Your MyHashMap object will be instantiated and called as such:
 * var obj = new MyHashMap()
 * obj.put(key,value)
 * var param_2 = obj.get(key)
 * obj.remove(key)
 */