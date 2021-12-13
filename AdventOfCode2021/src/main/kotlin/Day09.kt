import java.io.File

/* https://adventofcode.com/2021/day/9
* Find all of the low points on your heightmap and the three largest basins.
* Part One -> 478
* Part Two -> 1327014
 */
class Day09 {

    private val list = arrayListOf<IntArray>()
    private val lowPointsList = arrayListOf<Point>()
    private val visited = arrayListOf<Point>()

    fun run() {
        loadFile()
        partOne()
        partTwo()
    }

    private fun loadFile() {
        File("src/main/resources/Day09.txt").useLines { lines ->
            lines.forEach { line ->
                list.add(line.map { it.digitToInt() }.toIntArray())
            }
        }
    }

    private fun partOne() {
        var lowPointsSum = 0
        for (y in 0 until list.size) {
            for (x in 0 until list[y].size) {
                val currentValue = list[y][x]

                if (y - 1 >= 0 && currentValue >= list[y - 1][x]) continue // Bottom
                if (y + 1 < list.size && currentValue >= list[y + 1][x]) continue // Top
                if (x - 1 >= 0 && currentValue >= list[y][x - 1]) continue // Left
                if (x + 1 < list[y].size && currentValue >= list[y][x + 1]) continue // Right

                lowPointsSum += (currentValue + 1)
                lowPointsList.add(Point(y, x)) // For part two
            }
        }
        println("Part one $lowPointsSum")
    }

    private fun partTwo() {
        // Find all basins
        val basinSizeResult = lowPointsList
            .map { basinRecursion(it) }
            .filter { it > 0 }
        // Find the three largest basins and multiply their sizes together, take the three highest values after sorted
        val largestBasin =
            basinSizeResult.sortedDescending().take(3).reduce(Int::times) // Multiplies this value by the other value
        println("Part two $largestBasin")
    }

    private fun basinRecursion(point: Point): Int {
        val y = point.y
        val x = point.x

         if (notValidPoint(point, y, x)) return 0

         val topPoint = Point(y + 1, x)
         val bottomPoint = Point(y - 1, x)
         val leftPoint = Point(y, x - 1)
         val rightPoint = Point(y, x + 1)

         visited.add(point) // Current point is marked to make sure same point is not visited again

        // count every recursion
        return 1 +
                (basinRecursion(rightPoint)
                + basinRecursion(leftPoint)
                + basinRecursion(topPoint)
                + basinRecursion(bottomPoint))
    }

    private fun notValidPoint(point: Point, y: Int, x: Int) =
        point in visited || y < 0 || x < 0 || x >= list[0].size || y >= list.size || list[y][x] == 9

    data class Point(val y: Int, val x: Int)
}