// Leetcode 83

package LinkedList;

public class RemoveDuplicates {
    public ListNode deleteDuplicates(ListNode head) {
        if (head == null || head.next == null)
            return head;
        if (head.val == head.next.val)
            head.next = head.next.next;

        ListNode left = head;
        while (left != null && left.next != null) {
            if (left.val != left.next.val)
                left = left.next;
            else
                left.next = left.next.next;
        }

        return head;
    }

    public static void main(String[] args) {
        
    }
}
