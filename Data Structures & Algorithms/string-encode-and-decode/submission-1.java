class Solution {

    public String encode(List<String> strs) {
        String encoded = "";
        for(String i : strs){
            encoded = encoded + i;
            encoded = encoded + "#*";
        }
        return encoded;

    }

    public List<String> decode(String str) {
        char[] arr = str.toCharArray();
        String word = "";
        ArrayList<String> names = new ArrayList<>();
          for(int i = 0; i<arr.length; i++){
            if(arr[i] == '#' && arr[i+1] == '*') {
                i++;
                names.add(word);
                word = "";
            }
            else{
                word = word + arr[i];
            }
        }

        return names;

    }
}
