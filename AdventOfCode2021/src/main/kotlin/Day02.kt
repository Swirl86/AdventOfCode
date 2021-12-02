import java.io.File

/* https://adventofcode.com/2021/day/2
* Calculate the horizontal position and depth you would have after following the planned course.
* Part One -> 1561344
* Part Two -> 1848454425
 */
class Day02 {
    private val list = mutableListOf<String>()

    fun run() {
        loadFile()
        partOne()
        partTwo()
    }

    private fun loadFile() {
        File("Day02.txt").useLines { lines -> lines.forEach { list.add(it) } }
    }

    private fun partOne() {
        /*
         * forward X increases the horizontal position by X units.
         * down X increases the depth by X units.
         * up X decreases the depth by X units.
         */

        var horizontal = 0
        var depth: Long = 0

        list.forEach{line ->
            val row: List<String> = line.split(" ")
            val direction: String = row[0]
            val steps: Int = row[1].toInt()

            when (direction) {
                "up" -> depth -= steps
                "down" -> depth += steps
                else -> horizontal += steps
            }
        }
        println("Part One : ${horizontal * depth}")
    }

    private fun partTwo() {
        /*
         * down X increases your aim by X units.
         * up X decreases your aim by X units.
         * forward X does two things:
                It increases your horizontal position by X units.
                It increases your depth by your aim multiplied by X.
         */

        var horizontal = 0
        var depth: Long = 0
        var aim = 0

        list.forEach{line ->
            val row: List<String> = line.split(" ")
            val direction: String = row[0]
            val steps: Int = row[1].toInt()

            when (direction) {
                "up" -> {
                    aim -= steps
                }
                "down" -> {
                    aim += steps
                }
                else -> {
                    horizontal += steps
                    if(aim != 0) depth += (steps * aim)
                }
            }
        }
        println("Part Two : ${horizontal * depth}")
    }
}