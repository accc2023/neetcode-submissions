class Solution {
    public boolean validTree(int n, int[][] edges) {
        if (edges.length != n - 1) return false;
        HashMap<Integer, List<Integer>> children = new HashMap<>();
        for (int i = 0; i < n; i++) {
            children.put(i,new ArrayList<>());
        }
        for (int i = 0; i < edges.length; i++) {
            int node = edges[i][0];
            int child = edges[i][1];
            children.get(node).add(child);
        }
        for (int i = 0; i < edges.length; i++) {
            int node = edges[i][1];
            int child = edges[i][0];
            children.get(node).add(child);
        }
        int[] status = new int[n];
        if(!dfs(0,-1,children, status)) return false;
        return true;
    }
    private boolean dfs(int node,int parent,HashMap<Integer,List<Integer>> list,int[] status) {
        if (status[node] == 1) return false;
        if (status[node] == 2) return true;
        status[node] = 1;
        List<Integer> children = list.get(node);
        for (int i = 0; i < children.size(); i++) {
            int neigh = children.get(i);
            if (neigh == parent) continue;
            if(!dfs(neigh,node,list,status)) return false;
        }
        status[node] = 2;
        return true;
    }
}
