class Solution {
    public boolean isAnagram(String s, String t) {
        if(s.length() != t.length()) return false;

        HashMap<Character, Integer> sLetters = new HashMap<Character, Integer>();
        HashMap<Character, Integer> tLetters = new HashMap<Character, Integer>();

        for(int i = 0; i < s.length(); i++){
            if(sLetters.containsKey(s.charAt(i))) sLetters.put(s.charAt(i), sLetters.get(s.charAt(i)) + 1);
            else sLetters.put(s.charAt(i), 1);

            if(tLetters.containsKey(t.charAt(i))) tLetters.put(t.charAt(i), tLetters.get(t.charAt(i)) + 1);
            else tLetters.put(t.charAt(i), 1);
        }

        return sLetters.equals(tLetters);

    }
}
