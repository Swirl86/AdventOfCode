import java.io.File
import kotlin.math.abs

/* https://adventofcode.com/2021/day/7
* Determine the horizontal position that the crabs can align to using the least fuel possible.
* How much fuel must they spend to align to that position?
* Part One -> 343605
* Part Two -> 96744904
 */
class Day07 {

    private var crabPositions: ArrayList<Int> = arrayListOf()

    fun run() {
        loadFile()
        partOne()
        partTwo()
    }

    private fun loadFile() {
        val values = File("src/main/resources/Day07.txt").readText()
            .split(",")
            .map {
                crabPositions.add(it.toInt())
            }
    }

    private fun partOne() {
        val min = crabPositions.minOrNull()
        val max = crabPositions.maxOrNull()

        var minimumFuel = Int.MAX_VALUE

        for (i in min!!..max!!) {
            var currentFuel = 0
            crabPositions.forEach { position ->
                val distance = abs(i - position)
                currentFuel += distance
            }
            if (currentFuel < minimumFuel) minimumFuel = currentFuel
        }

        println("Part One $minimumFuel")
    }

    private fun partTwo() {
        val min = crabPositions.minOrNull()
        val max = crabPositions.maxOrNull()

        var minimumFuel = Int.MAX_VALUE

        for (i in min!!..max!!) {
            var currentFuel = 0
            crabPositions.forEach { position ->
                val distance = getDistance(abs(i - position))
                currentFuel += distance
            }

            if (currentFuel < minimumFuel) minimumFuel = currentFuel
        }

        println("Part Two $minimumFuel")
    }

    private fun getDistance(n: Int) = (n * (n + 1)) / 2 // Gauss formula
}