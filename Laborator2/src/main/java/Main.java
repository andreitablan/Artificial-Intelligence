import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;

class Main {

    /**
     * punctul 1.
     * starea
     * (m,n,currentM,currentN,k)
     */

    public static void main(String[] args) {

        State state=new State();
        state.initialize(3, 4, 0, 0, 2);
        if(state.backtracking(state.list)){
            System.out.println();
        }

    }

}