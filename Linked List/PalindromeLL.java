// Leetcode 234

package Linked List;

public class PalindromeLL {
    public boolean isPalindrome(ListNode head) {
        ListNode left = head;
        List<Integer> numList = new ArrayList<>();

        while(left != null){
            numList.add(left.val);
            left = left.next;
        }
        
        int l = 0, r = numList.size() - 1;
        while (l < r){
            if (numList.get(l) != numList.get(r)) return false;
            l++;
            r--;
        }
        return true;
    }

    public static void main(String[] args) {
        
    }
}
