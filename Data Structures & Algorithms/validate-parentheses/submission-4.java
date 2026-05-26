class Solution {
    public boolean isValid(String s) {
        Stack<Character> stack = new Stack<Character>();
        HashMap<Character, Character> hash = new HashMap<Character, Character>();

        hash.put(')', '(');
        hash.put(']', '[');
        hash.put('}', '{');

        for(int i = 0; i < s.length(); i++){
            
            if (hash.containsValue(s.charAt(i))) stack.push(s.charAt(i));
            else {
                if(stack.isEmpty() || (stack.peek() != hash.get(s.charAt(i)))){
                return false;
                }
                stack.pop();
            }
            
        }
        if (stack.isEmpty()) return true;
        return false;
    }
}
