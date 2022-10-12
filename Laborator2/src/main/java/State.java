import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;
import java.util.Queue;

public class State {
    List<Integer> list = new ArrayList<Integer>();
    List<List<Integer>> isVisited= new ArrayList<>();
    List<List<Integer>> savedVisited= new ArrayList<>();
    List<List<Integer>> solution=new ArrayList<>();



    public State() {
        solution.add(new ArrayList<>());

    }

    void initialize(int m, int n, int currentM, int currentN, int k) {
        List<Integer> state1 = Arrays.asList(new Integer[]{m, n, currentM, currentN, k});
        list = state1;
    }

    boolean isFinal(List<Integer> list) {
        if (list.get(2) == list.get(4) || list.get(3) == list.get(4)) {
            return true;
        }
        return false;
    }

    List<Integer> share(List<Integer> list, int fromCup, int toCup) {
        List<Integer> auxList=new ArrayList<>();
        auxList.addAll(list);
        if (validateShare(auxList, fromCup, toCup)) {
            if (fromCup == 1) {
                int waterBuffer = 0;
                if (auxList.get(2) < (auxList.get(1) - auxList.get(3))) {
                    waterBuffer = auxList.get(2);
                } else waterBuffer = auxList.get(1) - auxList.get(3);
                auxList.set(2, auxList.get(2) - waterBuffer);
                auxList.set(3, waterBuffer + auxList.get(3));
            } else if (fromCup == 2) {
                int waterBuffer = 0;
                if (auxList.get(3) < (auxList.get(0) - auxList.get(2))) {
                    waterBuffer = auxList.get(3);
                } else waterBuffer = auxList.get(0) - auxList.get(2);
                auxList.set(3, auxList.get(3) - waterBuffer);
                auxList.set(2, waterBuffer+auxList.get(2));
            }
            return auxList;
        }
        return list;
    }

    boolean validateShare(List<Integer> list, int fromCup, int toCup) {
        if (toCup == fromCup) {
            return false;
        }
        if (fromCup == 0) {
            return false;
        }
        if (toCup == 1) {
            if (toCup == list.get(0)) {
                return false;
            } else if (toCup == list.get(1)) {
                return false;
            }
        }
        return true;
    }

    List<Integer> fill(List<Integer> list, int whichCup) {
        List<Integer> auxList=new ArrayList<>();
        auxList.addAll(list);

        if (validateFill(list, whichCup)) {
            if (whichCup == 1) {
                auxList.set(2,list.get(0));
            } else {
                auxList.set(3,list.get(1));
            }
            return auxList;
        }
        return list;
    }

    boolean validateFill(List<Integer> list, int whichCup) {
        if (whichCup == 1)
            if (list.get(2) == list.get(0))
                return false;
            else if (list.get(3) == list.get(1))
                return false;
        return true;
    }

    List<Integer> empty(List<Integer> list, int whichCup) {
        List<Integer> auxList=new ArrayList<>();
        auxList.addAll(list);
        if (validateEmpty(list, whichCup)) {
            if (whichCup == 1) {
                auxList.set(2, 0);
            } else {
                auxList.set(3, 0);
            }
            return auxList;
        }
        return list;

    }

    boolean validateEmpty(List<Integer> list, int whichCup) {
        if (whichCup == 1)
            if (list.get(2) == 0)
                return false;
            else if (list.get(3) == 0)
                return false;
        return true;
    }

    boolean backtracking(List<Integer> list) {

        if (isFinal(list)) {
            solution.add(list);
            solution.remove(solution.get(0));
            System.out.println("The solution is: " + solution);
            System.out.println("The final state is:" + list);
            return true;
        }

        if (!existsInVisited(list)) {
            isVisited.add(list);
            if(!solution.get(solution.size() - 1).equals(list)){
                solution.add(list);
            }

            return (backtracking(fill(list, 1)) ||
                    backtracking(fill(list, 2)) ||
                    backtracking(empty(list, 1)) ||
                    backtracking(empty(list, 2)) ||
                    backtracking(share(list, 1, 2)) ||
                    backtracking(share(list, 2, 1)));
        }
        else return false;
    }


    boolean existsInVisited(List<Integer> list) {

        for (List<Integer> list1 : isVisited){
           if(list.equals(list1)){
               return true;
           }
        }
        return false;
    }
    boolean existsInVisited1(List<Integer> list) {

        for (List<Integer> list1 : savedVisited){
            if(list.equals(list1)){
                return true;
            }
        }
        return false;

    }
    boolean bfs(List<Integer> list) {
        if ((list.get(2) == list.get(4) && list.get(3) == 0) || (list.get(3) == list.get(4) && list.get(2) == 0)) {
            System.out.println("The final state is:" + list);
            return true;
        }
        if (!existsInVisited1(list)) {
            System.out.println(list);
            savedVisited.add(list);
            return (bfs(empty(list, 1)) ||
                    bfs(empty(list, 2)) ||
                    bfs(fill(list, 1)) ||
                    bfs(fill(list, 2)) ||
                    bfs(share(list, 1, 2)) ||
                    bfs(share(list, 2, 1)));
        }
        return false;
    }
}
