import java.io.File


/* https://adventofcode.com/2021/day/11
* Given the starting energy levels of the dumbo octopuses in your cavern, simulate 100 steps. How many total flashes are there after 100 steps?
* hat is the first step during which all octopuses flash?
* Part One -> 1755
* Part Two -> 212
 */
class Day11 {

    private val octopusList = arrayListOf<IntArray>()
    private var flashed = 0
    private var steps = 0

    fun run() {
        loadFile()
        partOne()
        partTwo()
    }

    private fun loadFile() {
        File("src/main/resources/Day11.txt").readText()
            .split("\r\n")
            .forEach { line ->
                octopusList.add(line.map { it.digitToInt() }.toIntArray())
            }
    }

    private fun partOne() {
        octopusSteps(100)
        println("Part one $flashed")
    }

    private fun partTwo() {
        octopusInfinitySteps()
        println("Part two $steps")
    }


    private fun octopusSteps(steps: Int) {
        repeat(steps) {
            incrementAllPoints()
            for (y in 0 until octopusList.size) {
                for (x in 0 until octopusList[y].size) {
                    if(octopusList[y][x] == 10)  {
                        increaseEnergyFlash(y, x)
                    }
                }
            }
        }
    }

    private fun octopusInfinitySteps() {
        while(notOnlyZero()) {
            incrementAllPoints()
            for (y in 0 until octopusList.size) {
                for (x in 0 until octopusList[y].size) {
                    if(octopusList[y][x] == 10)  {
                        increaseEnergyFlash(y, x)
                    }
                }
            }
        }

    }

    private fun notOnlyZero(): Boolean {
        return !octopusList.all { it.all { i -> i == 0 } }
    }

    private fun incrementAllPoints() {
        for (y in 0 until octopusList.size) {
            for (x in 0 until octopusList[y].size) {
                octopusList[y][x] += 1
            }
        }
        steps++
    }

    private fun increaseEnergyFlash(y: Int, x: Int) {
        flashed++
        Point(y, x).neighbours().forEach  {
            if(validPoint(it)) {
                octopusList[it.y][it.x] += 1
                if(octopusList[it.y][it.x] >= 10) increaseEnergyFlash(it.y, it.x)
            }
        }
        octopusList[y][x] = 0
    }

    private fun validPoint(point: Point) =
        octopusList[point.y][point.x] in 1..9

    private fun Point.neighbours(): List<Point> = listOf(
        Point(y, x + 1), // Right
        Point(y, x - 1), // Left
        Point(y + 1, x), // Top
        Point(y - 1, x), // Bottom
        Point(y + 1, x + 1), // Top Right
        Point(y + 1, x - 1), // Top Left
        Point(y - 1, x + 1), // Bottom Right
        Point(y - 1, x - 1), // Bottom Left
    ).filter {it.x >= 0 && it.y >= 0 && it.y < octopusList.size && it.x < octopusList[0].size }

    data class Point(val y: Int, val x: Int)
}