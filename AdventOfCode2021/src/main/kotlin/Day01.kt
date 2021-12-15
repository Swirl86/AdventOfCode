import java.io.File
import java.io.InputStream

/* https://adventofcode.com/2021/day/1
* How many measurements are larger than the previous measurement?
* part one --> 1139
* part two --> 1103
*/

class Day01 {

    private val list = Utils.readInputAsInts("Day01").toMutableList()

    fun run() {
        partOne()
        partTwo()
    }

    private fun partOne() {
        println("Part One : ${calculateMeasurement(0)}")
    }

    private fun partTwo() {
        println("Part Two : ${calculateMeasurement(2)}")
    }

    private fun calculateMeasurement(increase:Int): Int {
        var increaseCounter: Int = 0;

        for (i in 1 until (list.size - increase)) {
            if (list[i - 1] < list[i + increase]) increaseCounter++
        }
        return increaseCounter
    }
}
