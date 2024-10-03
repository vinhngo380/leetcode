/**
 * Definition for singly-linked list.
 * class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode(int x) {
 *         val = x;
 *         next = null;
 *     }
 * }
 */
import java.util.Set;
import java.util.HashSet;
public class Solution {
    // given a cycle i know that the tail does not point to null
    // i cannot just use a LL loop to determine this becuase of possible the cylce
    // if i use a set of the nodes to capture passed nodes i should be able to identify if the next node is actually a node we have already passed (indicating a cycle)
    public boolean hasCycle(ListNode head) {
        ListNode curr = head;
        Set<ListNode> myset = new HashSet<>();

        while (curr != null) {
            if (myset.contains(curr.next)) {
                return true; //cycle
            }
            myset.add(curr);
            curr = curr.next;
        }
        return false; // no cycle
    }
}

/* 
TLDR: I knew that a basic LL curr loop would be redundant, drew it out on paper and realized using a set<listnode> would work to find duplicate nodes (cycle's).
TC: Optimal O(1) Worst O(N)
SC: O(N) added a set
*/
