class Solution {
    public void islandsAndTreasure(int[][] grid) {
        //run bfs from all treasures and keep visited set to avoid repeats

        ArrayDeque<int[]> queue = new ArrayDeque<>();
        for (int i = 0; i < grid.length; i++) {
            for (int j = 0; j < grid[i].length; j++) {
                if (grid[i][j] == 0) queue.add(new int[] {i,j});
            }
        }
        while (!queue.isEmpty()) {
            int size = queue.size();
            for (int count = 0; count < size; count++) {
                int[] current = queue.remove();
                int i = current[0];
                int j = current[1];
                if (i > 0 && grid[i-1][j] == Integer.MAX_VALUE) {
                    grid[i-1][j] = grid[i][j] + 1;
                    queue.add(new int[]{i-1,j});
                }
                if (i < grid.length-1 && grid[i+1][j] == Integer.MAX_VALUE) {
                    grid[i+1][j] = grid[i][j] + 1;
                    queue.add(new int[]{i+1,j});
                }
                if (j > 0 && grid[i][j-1] == Integer.MAX_VALUE) {
                    grid[i][j-1] = grid[i][j] + 1;
                    queue.add(new int[]{i,j-1});
                }
                if (j < grid[i].length-1 && grid[i][j+1] == Integer.MAX_VALUE) {
                    grid[i][j+1] = grid[i][j] + 1;
                    queue.add(new int[]{i,j+1});
                }
            }
        }
    }
}
