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
        state.initialize(2, 5, 0, 0, 4);
        if(state.backtracking(state.list)){}
        if(state.bfs(state.list)){}

    }

}