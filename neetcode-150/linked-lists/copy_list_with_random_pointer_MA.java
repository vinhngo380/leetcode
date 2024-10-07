/*
// Definition for a Node.
class Node {
    int val;
    Node next;
    Node random;

    public Node(int val) {
        this.val = val;
        this.next = null;
        this.random = null;
    }
}
*/

class Solution {
    public Node copyRandomList(Node head) {
        // empty
        if (head == null) {
            return null;
        }

        // iterate through and point each node to a new Node that is that node copied 'new Node(n.val)'
        Node n = head;
        while (n != null) {
            Node next = n.next;
            n.next = new Node(n.val);
            n.next.next = next;
            n = next;
        }

        // point the random pointers of the copy nodes (every other) to the respective copy node of the orignal
        n = head;
        while (n != null) {
            if (n.random != null) {
                n.next.random = n.random.next;
            }
            n = n.next.next;
        }

        // disconnecting the copy list vs the regular list, going every other node aka copy.next.next
        n = head;
        Node copyHead = head.next;
        Node copy = copyHead;
        while (copy.next != null) {
            n.next = n.next.next;
            n = n.next;

            copy.next = copy.next.next;
            copy = copy.next;
        }
        n.next = n.next.next;
        return copyHead;
    }
}
/*
TLDR: 3 step process, add the new copy nodes to the orignal ll, redirect new nodes random pointers correctly, seperate the two linked lists - then return copy

TC: O(N)
SC: O(1)
*/
