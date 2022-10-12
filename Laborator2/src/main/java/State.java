import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;

public class State {
    List<Integer> list = new ArrayList<Integer>();
    List<Integer> isVisited[]=new List[20];
    int index=0;

    public State() {}

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
        if (validateShare(list, fromCup, toCup)) {
            if (fromCup == 1) {
                int waterBuffer = 0;
                if (list.get(2) < (list.get(1) - list.get(3))) {
                    waterBuffer = list.get(2);
                } else waterBuffer = list.get(1) - list.get(3);
                list.set(2, list.get(2) - waterBuffer);
                list.set(3, waterBuffer + list.get(3));
            } else if (fromCup == 2) {
                int waterBuffer = 0;
                if (list.get(3) < (list.get(0) - list.get(2))) {
                    waterBuffer = list.get(3);
                } else waterBuffer = list.get(0) - list.get(2);
                list.set(3, list.get(3) - waterBuffer);
                list.set(2, waterBuffer+list.get(2));
            }
            return list;
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
        if (validateFill(list, whichCup)) {
            if (whichCup == 1) {
                list.set(2,list.get(0));
            } else {
                list.set(3,list.get(1));
            }
            return list;
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
        if (validateEmpty(list, whichCup)) {
            if (whichCup == 1) {
                list.set(2, 0);
            } else {
                list.set(3, 0);
            }
            return list;
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
            System.out.println("final state:" + list);
            return true;
        }
        if (!existsInVisited(list)) {
            System.out.println('a');
            System.out.println(list);
            isVisited[index++]=list;
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
        for(int index1=0; index1<index;index1++)
        {
            System.out.println(isVisited[index1]);
        }
        for (int index1=0; index1<index;index1++) {

            if (isVisited[index1].equals(list)) return true;
        }
        return false;

    }

}
