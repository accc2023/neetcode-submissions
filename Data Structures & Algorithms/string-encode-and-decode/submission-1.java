class Solution {

    public String encode(List<String> strs) {
        String result = "";
        for (String s: strs) {
            String length = String.valueOf(s.length());
            result += length + "#" + s;
        }
        return result;
    }

    public List<String> decode(String str) {
        List<String> result = new ArrayList<>();
        int i = 0;
        while (i < str.length()) {
            int j = i;
            while (str.charAt(j) != '#') {
                j++;
            }
                int length = Integer.parseInt(str.substring(i,j)); // j currently at '#'
                j++; // First character in the string itself
                i = j; // First character in the string itself
                while (length != 0) {
                    j++;
                    length--;
                }
                result.add(str.substring(i,j)); // j already at position at start of next string
                i = j; // Now i and j are at the start of the next string (will start with no. and #)
        }
        return result;
    }
}
