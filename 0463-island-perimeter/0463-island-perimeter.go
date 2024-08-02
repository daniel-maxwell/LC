func islandPerimeter(grid [][]int) int {

    prepend := func (s [][]int, element []int) [][]int {
        newSlice := make([][]int, len(s)+1)
        copy(newSlice[1:], s)
        newSlice[0] = element
        return newSlice
    }

    getPerimBFS := func(ROWS int, COLS int, start []int) int {
        type coord [2]int

        queued := map[coord]bool{}
        visited := map[coord]bool{
            coord{start[0], start[1]} : true,
        }

        directions := [4][2]int{
            {-1, 0}, // Up
            {1, 0},  // Down
            {0, -1}, // Left
            {0, 1},  // Right
        }

        q, result := [][]int{start}, 0

        for len(q) > 0 {
            curLoc := q[len(q) - 1]
            q = q[:len(q) - 1]
            fmt.Println("Location: ", curLoc, " res:", result)

            for _, dir := range directions {
                move := []int{
                    curLoc[0] + dir[0],
                    curLoc[1] + dir[1],
                }

                _, haveVisited := visited[coord{move[0], move[1]}]
                if haveVisited { continue }

                if ( move[0] < 0 ||
                     move[0] == ROWS ||
                     move[1] < 0 ||
                     move[1] == COLS ||
                     grid[move[0]][move[1]] == 0) { 
                     result++ 
                } else {
                    if _, haveQueued := queued[coord{move[0], move[1]}]; !haveQueued {
                        q = prepend(q, move)
                        queued[coord{move[0], move[1]}] = true
                    }
                }
                visited[coord{curLoc[0], curLoc[1]}] = true
            }
        }
        return result
    }

    for r := range grid {
        for c := range grid[r] {
            if grid[r][c] == 1 {
                return getPerimBFS(len(grid), len(grid[0]), []int{r, c})
            }
        }
    }
    return 0
}