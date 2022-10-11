import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;

class Main {
    /**
     * punctul 1.
     * starea
     * (m,n,currentM,currentN,k)
     */
    int m,n,currentM,currentN,k;
    static List<List<Integer>> lists = new ArrayList<List<Integer>>();

    public static void main(String[] args) {

        System.out.println("first state" + initialize(5,6,0,0,3));

    }
    static List<Integer> initialize(int m, int n, int currentM, int currentN, int k){

        List<Integer> state1 = Arrays.asList(new Integer[] {m,n,currentM,currentN,k});
        lists.add(state1);
        return lists.get(0);
    }
    boolean isFinal(int currentM, int currentN){
        if(currentM==k||currentN==k){
            return true;
        }
        return false;
    }
}