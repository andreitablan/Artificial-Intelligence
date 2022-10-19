import java.util.*;

import static java.lang.Math.abs;

public class State {
    List<Integer> list = new ArrayList<Integer>();
    List<List<Integer>> isVisited = new ArrayList<>();
    List<List<Integer>> solution = new ArrayList<>();
    HashMap<List<Integer>, Integer> heuristics = new HashMap<>();
    List<List<Integer>> hillclimbVisited = new ArrayList<>();
    List<List<Integer>> aStarVisited = new ArrayList<>();
    List<List<Integer>> aStarList= new ArrayList<>();
    HashMap<List<Integer>, Integer> aStarScores = new HashMap<>();


    public State() {
        solution.add(new ArrayList<>());

    }

    boolean isSolvable(int m, int n, int k) {
        if ((m % 2 == 0 && n % 2 == 0 && k % 2 == 1)
                || (k > m && k > n)
                || (m < 0 || n < 0 || k < 0))
            return false;
        return true;
    }

    void initialize(int m, int n, int k) {
        list = Arrays.asList(m, n, 0, 0, k);
    }

    boolean isFinal(List<Integer> list) {
        return Objects.equals(list.get(2), list.get(4)) || Objects.equals(list.get(3), list.get(4));
    }

    List<Integer> share(List<Integer> list, int fromCup, int toCup) {
        List<Integer> auxList = new ArrayList<>(list);
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
                auxList.set(2, waterBuffer + auxList.get(2));
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
            } else return toCup != list.get(1);
        }
        return true;
    }

    List<Integer> fill(List<Integer> list, int whichCup) {
        List<Integer> auxList = new ArrayList<>(list);

        if (validateFill(list, whichCup)) {
            if (whichCup == 1) {
                auxList.set(2, list.get(0));
            } else {
                auxList.set(3, list.get(1));
            }
            return auxList;
        }
        return list;
    }

    boolean validateFill(List<Integer> list, int whichCup) {
        if (whichCup == 1)
            if (Objects.equals(list.get(2), list.get(0)))
                return false;
            else if (Objects.equals(list.get(3), list.get(1)))
                return false;
        return true;
    }

    List<Integer> empty(List<Integer> list, int whichCup) {
        List<Integer> auxList = new ArrayList<>(list);
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
            System.out.println("The solution of Backtracking: " + solution);
            System.out.println("The final state of Backtracking:" + list);
            return true;
        }

        if (!existsInVisited(list)) {
            isVisited.add(list);
            if (!solution.get(solution.size() - 1).equals(list)) {
                solution.add(list);
            }

            return (backtracking(fill(list, 1)) ||
                    backtracking(fill(list, 2)) ||
                    backtracking(empty(list, 1)) ||
                    backtracking(empty(list, 2)) ||
                    backtracking(share(list, 1, 2)) ||
                    backtracking(share(list, 2, 1)));
        } else return false;
    }


    boolean existsInVisited(List<Integer> list) {

        for (List<Integer> list1 : isVisited) {
            if (list.equals(list1)) {
                return true;
            }
        }
        return false;
    }

    public void bfs(List<Integer> list) {
        Queue<List<Integer>> queue = new LinkedList<>();
        queue.offer(list);
        if ((Objects.equals(list.get(2), list.get(4)) && list.get(3) == 0) || (Objects.equals(list.get(3), list.get(4)) && list.get(2) == 0)) {
            System.out.println("The final state was already the input:" + list);
            return;
        }
        while (!queue.isEmpty()) {
            List<Integer> auxList = queue.poll();
            if (isFinal(auxList)) {
                System.out.println("The final state of BFS:" + auxList);
                break;
            }
            if(!isFinal(fill(auxList, 1))){
            queue.add(fill(auxList, 1));}
            if(!isFinal(fill(auxList, 2)))
            queue.add(fill(auxList, 2));
            if(!isFinal(empty(auxList, 1)))
            queue.add(empty(auxList, 1));
            if(!isFinal(empty(auxList, 2)))
            queue.add(empty(auxList, 2));
            if(!isFinal(share(auxList, 1, 2)))
            queue.add(share(auxList, 1, 2));
            if(!isFinal(share(auxList, 2, 1)))
            queue.add(share(auxList, 2, 1));
        }
    }


    public int CalculateHeuristic(List<Integer> list) {
        return Math.min(abs(list.get(4) - list.get(2)), abs(list.get(4) - list.get(3)));
    }

    public void Hillclimbing(List<Integer> list) {
        if (list.get(3).equals(list.get(4)) || list.get(2).equals(list.get(4))) {
            System.out.println("The solution is: " + hillclimbVisited);
            System.out.println("The final state is: " + list);
            return;
        }
        hillclimbVisited.add(list);

        heuristics.clear();
        heuristics.put(fill(list, 1), CalculateHeuristic(fill(list, 1)));
        heuristics.put(fill(list, 2), CalculateHeuristic(fill(list, 2)));
        heuristics.put(empty(list, 1), CalculateHeuristic(empty(list, 1)));
        heuristics.put(empty(list, 2), CalculateHeuristic(empty(list, 2)));
        heuristics.put(share(list, 1, 2), CalculateHeuristic(share(list, 1, 2)));
        heuristics.put(share(list, 2, 1), CalculateHeuristic(share(list, 2, 1)));


        int min = CalculateHeuristic(list);

        List<Integer> bestState = new ArrayList<>();
        for (List<Integer> key : heuristics.keySet()) {
            boolean stop = false;
            if (heuristics.get(key) <= min) {
                for (List<Integer> auxList : hillclimbVisited) {
                    if (auxList.equals(key)) {
                        stop = true;
                        break;
                    }
                }
                if (!stop) {
                    min = heuristics.get(key);
                    bestState = key;
                }
            }
        }

        if (bestState.isEmpty()) {
            System.out.println("There are no more options. Could only find a local maximum: " + list);
            System.out.println(hillclimbVisited);
            return;
        }
        Hillclimbing(bestState);
    }

    //a*      * (m,n,currentM,currentN,k)
    public int CalculateHeuristicAStar(List<Integer> list) {
        return Math.min(abs(list.get(0)-list.get(2))+ abs(list.get(4) - list.get(2)), abs(list.get(1)-list.get(3))+ abs(list.get(4) - list.get(3)));
    }

    List<List<Integer>> sortListByHeuristic(List<List<Integer>> toSortList){
        for(int index1=0; index1<toSortList.size()-1;index1++) {
            for (int index2=index1+1;index2<toSortList.size();index2++) {
                if(CalculateHeuristicAStar(toSortList.get(index1))<CalculateHeuristicAStar(aStarList.get(index2))) {
                    List<Integer> auxList = new ArrayList<>();
                    auxList=toSortList.get(index1);
                    toSortList.set(index1,toSortList.get(index2));
                    toSortList.set(index2,auxList);
                }
            }
        }
        return toSortList;
    }

    public void AStar(List<Integer> list){
        if (list.get(3).equals(list.get(4)) || list.get(2).equals(list.get(4))) {
            System.out.println("The solution is: " + aStarVisited);
            System.out.println("The final state is: " + list);
            return;
        }

        int bestScore=Math.max(list.get(0),list.get(1));

        aStarVisited.add(list);

        aStarList.clear();
        aStarList.add(fill(list, 1));
        aStarList.add(fill(list, 2));
        aStarList.add(empty(list, 1));
        aStarList.add(empty(list, 2));
        aStarList.add(share(list, 1, 2));
        aStarList.add(share(list, 2, 1));

        for(List<Integer> state:aStarList){
            if(!aStarScores.containsKey(state)){
                aStarScores.put(state,1);
            }
            else aStarScores.put(state,aStarScores.get(state)+1);
        }

        aStarList=sortListByHeuristic(aStarList);

        List<Integer> auxList=new ArrayList<>();
        auxList=aStarList.get(0);
        int score=2;
        while(!aStarList.isEmpty() && aStarScores.get(auxList)<bestScore){
            if (isFinal(auxList)) {
                System.out.println("The final state of BFS:" + auxList);
                bestScore=CalculateHeuristicAStar(auxList);
                break;
            }
            aStarVisited.add(auxList);
            System.out.println("---------------------------------");
            System.out.println(aStarVisited);

            aStarList.add(fill(auxList, 1));
            aStarList.add(fill(auxList, 2));
            aStarList.add(empty(auxList, 1));
            aStarList.add(empty(auxList, 2));
            aStarList.add(share(auxList, 1, 2));
            aStarList.add(share(auxList, 2, 1));

            for(List<Integer> state:aStarList){
                if(!aStarScores.containsKey(state)){
                    aStarScores.put(state,score);
                }
            }
            aStarList.remove(0);
            aStarList=sortListByHeuristic(aStarList);
            score++;
            auxList = aStarList.get(0);
        }
    }
}
