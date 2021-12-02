import java.io.File
import java.io.InputStream

/* https://adventofcode.com/2021/day/1
* How many measurements are larger than the previous measurement?
* part one --> 1139
* part two --> 1103
*/

class Day01 {

    private val list = mutableListOf<Int>()

    fun run() {
        loadFile()
        partOne()
        partTwo()
    }
    private fun loadFile() {
        File("Day01.txt").useLines { lines -> lines.forEach { list.add(it.toInt()) } }
    }

    private fun partOne() {
        var increaseCounter: Int = 0;

        for (i in 1 until (list.size)) {
            if (list[i - 1] < list[i]) increaseCounter++
        }

        println("Part One : $increaseCounter")
    }

    private fun partTwo() {
        var increaseCounter: Int = 0;

        for (i in 1 until (list.size - 2)) {
            if (list[i - 1] < list[i + 2]) increaseCounter++
        }

        println("Part Two : $increaseCounter")
    }
}
