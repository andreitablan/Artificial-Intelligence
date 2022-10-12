import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;

public class State {
    List<Integer> list = new ArrayList<Integer>();
    List<List<Integer>> isVisited = new ArrayList<>();
    int m, n, currentM, currentN, k;

    public State() {

    }

    void initialize(int m, int n, int currentM, int currentN, int k) {
        List<Integer> state1 = Arrays.asList(new Integer[]{m, n, currentM, currentN, k});
        list = state1;
    }

    boolean isFinal(List<Integer> list) {
        if (list.get(currentM) == list.get(k) || list.get(currentN) == list.get(k)) {
            return true;
        }
        return false;
    }

    List<Integer> share(List<Integer> list, int fromCup, int toCup) {
        if (validateShare(list, fromCup, toCup)) {
            if (fromCup == 1) {
                int waterBuffer = 0;
                if (list.get(currentM) < (list.get(n) - list.get(currentN))) {
                    waterBuffer = list.get(currentM);
                } else waterBuffer = list.get(n) - list.get(currentN);
                list.set(currentM, list.get(currentM) - waterBuffer);
                list.add(currentN, waterBuffer);
            } else if (toCup == 1) {
                int waterBuffer = 0;
                if (list.get(currentN) < (list.get(m) - list.get(currentM))) {
                    waterBuffer = list.get(currentN);
                } else waterBuffer = list.get(m) - list.get(currentN);
                list.set(currentN, list.get(currentN) - waterBuffer);
                list.add(currentM, waterBuffer);

            }
        }
        return list;
    }

    boolean validateShare(List<Integer> list, int fromCup, int toCup) {
        if (fromCup != 1 || fromCup != 2) {
            return false;
        }
        if (toCup != 1 || toCup != 2) {
            return false;
        }
        if (toCup == fromCup) {
            return false;
        }
        if (fromCup == 0) {
            return false;
        }
        if (fromCup == 1) {
            if (toCup == list.get(m)) {
                return false;
            } else if (toCup == list.get(n)) {
                return false;
            }
        }
        return true;
    }

    List<Integer> fill(List<Integer> list, int whichCup) {
        if (validateFill(list, whichCup)) {
            if (whichCup == 1) {
                int waterBuffer = list.get(m) - list.get(currentM);
                list.add(currentN, waterBuffer);
            } else {
                int waterBuffer = list.get(n) - list.get(currentN);
                list.add(currentM, waterBuffer);
            }
        }
        return list;

    }

    boolean validateFill(List<Integer> list, int whichCup) {
        if (whichCup != 1 || whichCup != 2)
            return false;
        if (whichCup == 1)
            if (list.get(currentM) == list.get(m))
                return false;
            else if (list.get(currentN) == list.get(n))
                return false;
        return true;
    }

    List<Integer> empty(List<Integer> list, int whichCup) {
        if (validateEmpty(list, whichCup)) {
            if (whichCup == 1) {
                list.set(currentM, 0);
            } else {
                list.set(currentN, 0);
            }
        }
        return list;
    }

    boolean validateEmpty(List<Integer> list, int whichCup) {
        if (whichCup != 1 || whichCup != 2)
            return false;
        if (whichCup == 1)
            if (list.get(currentM) == 0)
                return false;
            else if (list.get(currentN) == 0)
                return false;
        return true;
    }

    boolean backtracking(List<Integer> list) {
        if (isFinal(list)) {
            System.out.println("final state:" + list);
            return true;
        }
        if (existsInVisited(list) == false) {
            System.out.println(list);
            isVisited.add(list);
            return (backtracking(fill(list, 1)) || backtracking(fill(list, 2)) || backtracking(empty(list, 1)) || backtracking(empty(list, 2))
                    || backtracking(share(list, 1, 2)) || backtracking(share(list, 2, 1)));
        }
        return false;
    }

    boolean existsInVisited(List<Integer> list) {
        for (List<Integer> list1 : isVisited)
            if (list1 == list) return true;
        return false;
    }

}
