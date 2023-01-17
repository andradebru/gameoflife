<template>
    <div>
        <table>
            <tr v-for="(line, i) in grid" :key="i">
                <td v-for="(cell, j) in line" :key="j" :class="{alive: cell==1}"></td>
            </tr>
        </table>
    </div>
</template>

<script>
    function countAliveNeighbours(i, j, grid) {
      let alives = 0;
      for (let line_x of [-1, 0, 1]) {
        for (let columns_y of [-1, 0, 1]) {
          if (line_x == 0 && columns_y == 0) continue
          const neighbor_x = i + line_x;
          const neighbor_y = j + columns_y;
          if (grid[neighbor_x]?.[neighbor_y]) {
            alives += 1
          }
        }
      }
      return alives;
    }
    function nextState(grid) {
        const [M, N] = [grid.length, grid[0].length]
        let newGrid = new Array(M)
        for (let i=0; i<M; i++) {
            newGrid[i] = new Array(N).fill(0)
        }
        for (let i=0; i<M; i++){
            for(let j=0; j<N; j++) {
                    let aliveNeighbours = countAliveNeighbours(i, j, grid)
                if (grid[i][j] == 1) {
                    if (aliveNeighbours == 2 || aliveNeighbours == 3) {
                        newGrid[i][j] = 1
                    } else {
                        newGrid[i][j] = 0
                    }
                } else {
                    if (aliveNeighbours == 3) {
                        newGrid[i][j] = 1
                    } else {
                        newGrid[i][j] = 0
                    }
                }
            }
        }
        return newGrid
    }

    export default {
        name: 'LifeGame',
        data() {
            return {
                grid: [
                    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0],
                    [0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0],
                    [0, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                ]
            }
        },
        methods: {
            nextStep() {
                this.grid = nextState(this.grid)
            }
        },
        mounted() {
            setInterval(() => {
                this.nextStep()
            }, 1000)
        }
}
</script>

<style scoped>

div {
    height: 80vh;
    display: flex;
    align-items: center;
    justify-content: center;
}

table, td {
    border: 1px solid #000000;
    border-collapse: collapse;
}

td {
    width: 20px;
    height: 20px;
    background-color: #e9e7df;
}

.alive {
    background-color: #b98dc3;
}
</style>