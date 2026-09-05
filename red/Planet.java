import java.util.List;
import java.util.ArrayList;
import java.util.Map;
import java.util.HashMap;
public class Planet{
    public double x;
    public double y;
    public double mass;
    public Planet(double x,double y, double mass){
        this.x=x;
        this.y=y;
        this.mass=mass;
    }
    public double distance_to(Planet other){
        double answer= Math.sqrt(Math.pow((other.x-x),2)+(other.y-y));
        return answer;
    }
    public static double sum_mass(Planet p1, Planet p2){
        return p1.mass+p2.mass;
    }
    public static List<Integer> common(List<Integer> L1, List<Integer> L2) {
        List<Integer> x = new ArrayList<>();
        for(int i:L1){
            if (L2.contains(i)&& !x.contains(i)){
                x.add(i);
            }
        }
        return x;
    }
    public static void capitalize(List<String> L) {
        for(int i=0; i<L.size();i++){
            L.set(i, L.get(i).toUpperCase());
        }
    }
    public static Map<Integer, List<Integer>> buildLessThanMap(List<Integer> L) {
        Map<Integer, List<Integer>> result = new HashMap<>();
        for(int i:L){
            if(!result.containsKey(i)){
                result.put(i,new ArrayList<>());
            }
            for (int j :L){
                if(j<i){
                    if(!result.get(i).contains(j)){
                        result.get(i).add(j);
                    }
                }
            }

        }
        return result;
    }
public static int[] filterPositive(List<Integer> L) {
    List<Integer> answer= new ArrayList<>();
    for (int i:L){
    if (i>0){
        answer.add(i);
    }
}
    int[] a = new int [answer.size()];
    for(int i=0; i <answer.size();i++){
        a[i]=answer.get(i);
    }
        return a;
}
public static int[] filterPositive1(List<Integer> L) {
    return L.stream()
            .filter(x -> x > 0)
            .mapToInt(x -> x)
            .toArray();
}
    public static void main(String[] args){
        Planet p1 = new Planet(5, 10, 100);
        Planet p2= new Planet(1, 2, 200);
        p1.distance_to(p2);
        Planet.sum_mass(p1, p2);
    }

}