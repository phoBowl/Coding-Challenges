class Element {
    int index;
    int counter;
    public Element(int id){
        this.index = id;
        this.counter = 1;
    }
}

char firstNotRepeatingCharacter(String s) {
    Map<Character,Element> map = new HashMap<Character,Element>();
    for(int i = 0 ; i < s.length(); i++){
        char k = s.charAt(i);
        if(map.containsKey(k)){
            map.get(k).counter++;
        }else{
            map.put(k,new Element(i));
        }
    }
    
    for(int i = 0 ; i < s.length(); i++){
        if(map.get(s.charAt(i)).counter == 1){
            return s.charAt(map.get(s.charAt(i)).index);
        }
    }
    return '_';
}
