int[][] rotateImage(int[][] a) {
    int[][] rt = new int[a.length][a.length]; 
    for(int i = 0 ; i < a.length ; i++){
        for(int j = 0 ; j < a.length; j++){
            rt[i][j] = a[a.length-1-j][i];
        }
    }
    return rt;
}
