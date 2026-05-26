class Solution {
    public List<List<String>> groupAnagrams(String[] strs) {
        HashMap<String, List<String>> ans = new HashMap<>();

        for(String s : strs) {
            char[] characters = s.toCharArray();
            int[] key = new int[26];
            for(char c : characters){
                key[c - 'a']++;
            }
            String keyString = Arrays.toString(key);
            ans.putIfAbsent(keyString, new ArrayList());
            ans.get(keyString).add(s);
        }

        return new ArrayList<>(ans.values());
    
    }
}



