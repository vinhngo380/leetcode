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
    public ListNode reverseList(ListNode head) {
        // use two pointers prev, curr, next
        // make curr.next > prev, update positions and repeat until curr = null
        // return the previous aka the head of the newly ordered LL

        ListNode prev = null;
        ListNode curr= head;

        while (curr != null) {
            ListNode next = curr.next;
            curr.next = prev;
            prev = curr;
            curr = next;
        }
        return prev;
    }
}

/*

TLDR: Used two pointer method in conjunction with LL curr loop to flip the next pointers for the linked list nodes

TC: worst O(N) best O(N)
SC: O(1) - no added space

*/
