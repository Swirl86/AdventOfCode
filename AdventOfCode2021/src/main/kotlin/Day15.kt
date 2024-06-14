import java.io.File

/* https://adventofcode.com/2021/day/15
* What is the lowest total risk of any path from the top left to the bottom right?
* Part One ->
* Part Two ->
 */
class Day15 {
    private var cavern = arrayListOf<IntArray>()
    private val visited = arrayListOf<Point>()

    fun run() {
        loadFile()
        //partOne()
       // partTwo()
    }

    private fun loadFile() {
        File("src/main/resources/Day15.txt").readText()
            .split("\r\n")
            .forEach { line ->
                cavern.add(line.map { it.digitToInt() }.toIntArray())
            }
    }

    private fun partOne() {
        TODO("Not yet implemented")
    }

    // Dijkstra's algorithm -  https://en.wikipedia.org/wiki/Dijkstra%27s_algorithm
    private fun cavernRecursion(point: Point): Int {
        val y = point.y
        val x = point.x

        return 0
    }

    private fun partTwo() {
        TODO("Not yet implemented")
    }

    private fun Point.neighbours(): List<Point> = listOf(
        Point(y, x + 1), // Right
        Point(y, x - 1), // Left
        Point(y + 1, x), // Top
        Point(y - 1, x), // Bottom
    ).filter {it.x >= 0 && it.y >= 0 && it.y < cavern.size && it.x < cavern[0].size }

    data class Point(val y: Int, val x: Int)
}