import java.util.Arrays;
class Solution {
    public boolean isAnagram(String s, String t) {
        char[] charsx=s.toCharArray();
        Arrays.sort(charsx);

        char[] charsy=t.toCharArray();
        Arrays.sort(charsy);

        return Arrays.equals(charsx,charsy);
    }
}