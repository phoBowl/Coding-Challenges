int firstDuplicate(int[] a) {
    Set<Integer> set = new HashSet<Integer>();
    for(int i =0 ; i < a.length; i++){
        if(set.contains(a[i])){
            return a[i];
        }
        set.add(a[i]);
    }
    return -1;
}
