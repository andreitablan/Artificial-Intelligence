import java.util.Scanner;

class Main {

    /**
     * punctul 1.
     * starea
     * (m,n,currentM,currentN,k)
     */

    public static void main(String[] args) {

        //menu();
        State state = new State();
        state.initialize(3, 4, 2);
        state.AStar(state.list);

    }

    public static void menu() {
        System.out.println("Please give the initial state: ");
        Scanner scanner = new Scanner(System.in);
        System.out.println("capacity of the first cup = ");
        int m = Integer.parseInt(scanner.next());
        System.out.println("capacity of the second cup = ");
        int n = Integer.parseInt(scanner.next());
        System.out.println("final remaining quantity of water = ");
        int k = Integer.parseInt(scanner.next());
        System.out.println("Which strategy do you want to chose?[BKT/BFS/Hillclimbing]");
        String strategy = scanner.next();
        State state = new State();
        state.initialize(m, n, k);
        if (state.isSolvable(m, n, k)) {
            switch (strategy) {
                case "BKT" -> state.backtracking(state.list);
                case "BFS" -> state.bfs(state.list);
                case "Hillclimbing" -> state.Hillclimbing(state.list);
                case "A*" -> state.AStar(state.list);

            }
        } else {
            System.out.println("The input is not solvable!");
        }
    }
}