import java.util.HashSet;
import java.util.Set;
class Solution {
    public boolean hasDuplicate(int[] nums) {
        Set<Integer> x = new HashSet<>();
        for (int i:nums){
            if(x.contains(i)){
                return true;

            }
            else{
                x.add(i);
            }

        }
        return false;
    }
}