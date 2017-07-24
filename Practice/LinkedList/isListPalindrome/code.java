// Definition for singly-linked list:
// class ListNode<T> {
//   ListNode(T x) {
//     value = x;
//   }
//   T value;
//   ListNode<T> next;
// }
/*
 * 1) Get the middle of the linked list.
   2) Reverse the second half of the linked list.
   3) Check if the first half and second half are identical.
   4) Construct the original linked list by reversing the second half again and attaching it back to the first half
 */

static boolean isListPalindrome(ListNode<Integer> l){
    ListNode fast = l;
    ListNode slow = l;
    
    ListNode prev_slow = null;
    
    ListNode head = l;
    ListNode middle = null;
    
    ListNode secondhalf = null;
    
    boolean check = false;
    if(head == null) return true;
    if(head.next == null) return true;
    //Find the middle of the list
    if(head!= null && head.next !=null){
        while(fast!=null && fast.next!=null){
            fast = fast.next.next;
            prev_slow = slow;
            slow = slow.next;
        }
    }
    //handle when list size is odd
    if(fast!=null){
        middle = slow;
        slow = slow.next;
    }
    secondhalf = slow;
    prev_slow.next = null;
    
    secondhalf = reverse(secondhalf);
    ListNode tempS = secondhalf;
    ListNode tempL = l;
    /*
    while(tempS!=null){
        System.out.print(tempS.value+" ");
         tempS= tempS.next;
    }
    System.out.println("\n");
    while(tempL!=null){
        System.out.print(tempL.value+ " ");
        tempL= tempL.next;
    }
    */
    check = compareList(l,secondhalf);
    
    return check;
}

//reverse the second half
static ListNode reverse(ListNode secondhalf){
    ListNode prev = null;
    ListNode curr = secondhalf;
    ListNode next = null;
    while(curr!=null){
        next = curr.next;
        curr.next = prev;
        prev = curr;
        curr = next;
    }
    secondhalf = prev;
    return secondhalf;
}

static boolean compareList(ListNode one, ListNode two){
    ListNode curr1 = one;
    ListNode curr2 = two;
   
    while(curr1!=null && curr2 != null){
        if(curr1.value.equals(curr2.value)){
            curr1 = curr1.next;
            curr2 = curr2.next;
        }else{ 
            return false;
        }
    }
    if(curr1 == null && curr2 == null){
        return true;
    }
    return false;
}




