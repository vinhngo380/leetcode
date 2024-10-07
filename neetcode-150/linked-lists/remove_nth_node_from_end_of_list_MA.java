import java.util.LinkedList;
import java.util.Collections;
/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode() {}
 *     ListNode(int val) { this.val = val; }
 *     ListNode(int val, ListNode next) { this.val = val; this.next = next; }
 * }
 */
class Solution {
    public ListNode removeNthFromEnd(ListNode head, int n) {
        // size 0
        if (head == null) {
            return head;
        }

        if (head.next == null) {
            return null;
        }

        ListNode counter = head;
        int count = 0;
        while (counter != null) {
            counter = counter.next;
            count += 1;
        }

        int index = count - n;

        if (count == n) {
            return head.next;
        }

        ListNode curr = head;
        for (int i = 1; i < index; i++) {
            curr = curr.next;
        }

        curr.next = curr.next.next;
        return head;
    }
}

/*

TLDR: used a pointer method with curr, evaluated the index to remove with simple difference calculation

TC: O(N - x) where x is the index, so ultimatley O(n)
SC: O(N + x) where x is the creation of new LL nodes curr so ultimately O(n)

*/
