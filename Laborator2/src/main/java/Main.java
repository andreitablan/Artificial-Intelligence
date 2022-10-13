import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;
import java.util.Scanner;

class Main {

    /**
     * punctul 1.
     * starea
     * (m,n,currentM,currentN,k)
     */

    public static void main(String[] args) {

        menu();

    }
    public static void menu(){
        System.out.println("Please give the initial state: ");
        Scanner scanner = new Scanner(System.in);
        System.out.println("capacity of the first cup = ");
        Integer m = Integer.valueOf(scanner.next());
        System.out.println("capacity of the second cup = ");
        Integer n = Integer.valueOf(scanner.next());
        System.out.println("final remaining quantity of water = ");
        Integer k = Integer.valueOf(scanner.next());
        System.out.println("Which strategy do you want to chose?[BKT/BFS]");
        String strategy = scanner.next();
        State state=new State();
        state.initialize(m, n, 0, 0, k);
        if(strategy.equals("BKT")){
            if(state.backtracking(state.list)){}
        }
        else if(strategy.equals("BFS")){
            state.bfs(state.list);
        }
    }
}