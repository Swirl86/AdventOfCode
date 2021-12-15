import java.io.File
import kotlin.math.*

/* https://adventofcode.com/2021/day/5
* Consider only horizontal and vertical lines. At how many points do at least two lines overlap?
* Part One -> 4655
* Part Two -> 20500
 */
class Day05 {
    private var linePoints = ArrayList<Coordinates>()
    private val pointList: ArrayList<Point> = arrayListOf()

    fun run() {
        loadFile()
        partOne()
        partTwo()
    }

    private fun loadFile() {
        File("src/main/resources/Day05.txt").useLines { lines ->
            lines.forEach {
                linePoints.add(getValues(it))
            }
        }
    }

    private fun getValues(line: String): Coordinates {
        val(start, end) = line.split("->")
        val(x1, y1) = start.trim().split(",")
        val(x2, y2) = end.trim().split(",")
        return Coordinates(x1.toInt(), y1.toInt(), x2.toInt(), y2.toInt())
    }

    private fun partOne() {
        val ventLines = ArrayList<Coordinates>()
        ventLines.addAll(linePoints)
        ventLines
            .filter { line -> line.x1 == line.x2 || line.y1 == line.y2  }
            .forEach { line ->
                for (x in min(line.x1, line.x2)..max(line.x1, line.x2)){
                    for (y in min(line.y1, line.y2)..max(line.y1, line.y2)) {
                        pointList.add(Point(x, y))
                    }
                }
        }

        val result = pointList.groupingBy { it }.eachCount().filterValues { it >= 2}.size
        println("Part One $result")
    }

    private fun partTwo() {
        val diagonalPoints = mutableListOf<Point>()
        linePoints
            .forEach { line ->
                val dx = line.x2 - line.x1
                val dy = line.y2 - line.y1

                // Distance between two points
                (0..abs(dx).coerceAtLeast(abs(dy))).forEach { i ->
                    val x = line.x1 + (if (dx > 0) 1 else (if (dx < 0) -1 else 0)) * i
                    val y = line.y1 + (if (dy > 0) 1 else (if (dy < 0) -1 else 0)) * i
                    diagonalPoints.add(Point(x, y))
                }
            }

        val result = diagonalPoints.groupingBy { it }.eachCount().filterValues { it >= 2 }.size

        println("Part Two $result")
    }

    data class Coordinates(val x1: Int, val y1: Int, val x2: Int, val y2: Int)
    data class Point(val x: Int, val y: Int)
}