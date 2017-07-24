boolean convertString(String s, String t) {
    String cp ="";
    boolean rt = false;
    char tChar2 = '\0';
    int saveIndex = 0;
    if(s.equals(t)) return true;
    if(s.length() < t.length()) return false;
    for(int i = 0; i < t.length(); i++){
        char tChar1 = t.charAt(i);
        if(i < t.length()-1){
             tChar2 = t.charAt(i+1);
        }
        for( int j = saveIndex; j < s.length() ; j++){
            char temp = '\0';
            char sChar = s.charAt(j);
            if(temp == tChar2) return false;
            if(sChar == tChar1){
                cp+=sChar;
                saveIndex = j;
                break;
            }
        }
    }
    System.out.println(cp);
    System.out.println(t);
    if(cp.compareTo(t) == 0) return true;
    return false;
}
