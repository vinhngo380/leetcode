// Initiate the Node class for LL - each node has a key,value attribute and prev,next pointer
class ListNode {
    int key;
    int val;
    ListNode next;
    ListNode prev;

    public ListNode(int key, int val) {
        this.key = key;
        this.val = val;
    }
}

// initiate the lru cache class; capacity, map for tracking data (key, node(key, value))
class LRUCache {

    private int capacity;
    private Map<Integer,ListNode> dic;
    private ListNode head;
    private ListNode tail;

    public LRUCache(int capacity) { // set capcity when making an lru cache
        this.capacity = capacity;
        dic = new HashMap<>();
        head = new ListNode(-1, -1);
        tail = new ListNode(-1, -1);
        head.next = tail;
        tail.prev = head;
    }

    public void add(ListNode node) { // add node to end of linked list
        ListNode previousEnd = tail.prev; // using our blank head/tail references (-1,-1)
        previousEnd.next = node;
        node.prev = previousEnd;
        node.next = tail;
        tail.prev = node;
    }

    public void remove(ListNode node) { // remove specific node from list
        node.prev.next = node.next;
        node.next.prev = node.prev;
    }

    public int get(int key) {
        if (!dic.containsKey(key)) {
            return -1;
        }

        ListNode node = dic.get(key); // taking node removing it adding it to end most recently used
        remove(node);
        add(node);
        return node.val;
    }

    public void put(int key, int value) { // updating if key exists, use add to add to end, most recently used 
        if (dic.containsKey(key)) {
            ListNode oldNode = dic.get(key);
            remove(oldNode);
        }
        ListNode node = new ListNode(key, value);
        dic.put(key, node);
        add(node);

        if (dic.size() > capacity) {
            ListNode nodeToDelete = head.next;
            remove(nodeToDelete);
            dic.remove(nodeToDelete.key);
        }
    }
}

/**

TLDR: used doubly linked list for optimized search, specific removal, and removal/addition to both ends

TC: O(n)
SC: O(n^2)
      
-------------------------------------------------------------------
 * Your LRUCache object will be instantiated and called as such:
 * LRUCache obj = new LRUCache(capacity);
 * int param_1 = obj.get(key);
 * obj.put(key,value);
 */
