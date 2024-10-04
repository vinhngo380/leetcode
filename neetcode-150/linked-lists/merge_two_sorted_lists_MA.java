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
    public ListNode mergeTwoLists(ListNode list1, ListNode list2) {
        // we want to make sure we are adding the nodes with the lowest val checking both lists
        ListNode dummy = new ListNode();
        ListNode curr = dummy;

        while (list1 != null && list2 != null) {
            if (list1.val > list2.val) {
                curr.next = list2;
                list2 = list2.next;
            } else {
                curr.next = list1;
                list1 = list1.next;
            }
            curr = curr.next;
        }

        curr.next = (list1 != null) ? list1 : list2;

        return dummy.next;
    }
}

/*

TLDR: Using a dummy node and a pointer curr. basic conditional logic for selecting which node to set as the pointers next, with proper updates.

TC: worst O(n) best case O(1)
SC: created a new linked list for the output so O(N)

*/
