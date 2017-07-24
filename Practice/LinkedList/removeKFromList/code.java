// Definition for singly-linked list:
/*
class ListNode<T> {
   ListNode(T x) {
     value = x;
   }
   T value;
   ListNode<T> next;
 }
*/
ListNode<Integer> removeKFromList(ListNode<Integer> l, int k) {
    if(l == null) return null;
    else if(l.next == null && l.value == k) return null;
    else{
        ListNode<Integer> curr = l;
        ListNode<Integer> prev = null;
        ListNode<Integer> next = null;
        while(curr!=null){
            next = curr.next;
            if(curr.value == k){
                if(prev == null){
                    l = curr.next;
                    curr = l;
                }else{
                    curr = next;
                    prev.next = curr;
                }  
            }else{
            prev = curr;
            curr = next;
            }
        }
        
    }
    
    return l;

}
