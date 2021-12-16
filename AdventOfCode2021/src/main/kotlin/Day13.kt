import kotlin.math.abs

/* https://adventofcode.com/2021/day/13
* How many dots are visible after completing just the first fold instruction on your transparent paper?
* Part One -> 850
* Finish folding the transparent paper according to the instructions. The manual says the code is always eight capital letters.
* Part Two -> AHGCPGAU
 */
class Day13 {

    private val list = Utils.readInput("Day13")
    private var pointList = setOf<Pair<Int, Int>>()
    private var foldInstructionList = mutableListOf<Instruction>()
    private var isPartOne = true

    fun run() {
        splitList()
        partOne()
        partTwo()
    }

    private fun splitList() {
        // Returns a list containing FIRST elements satisfying the given predicate.
        pointList = list.takeWhile { it.isNotEmpty() }
            .map { it.split(",") }
            .map { it.first().toInt() to it.last().toInt() }
            .toSet()

        // Returns a list containing LAST elements satisfying the given predicate
        foldInstructionList = list.takeLastWhile { it.isNotEmpty() }
            .map { it.split("=") }
            .map {
                if (it.first().endsWith("y")) Instruction('y', it.last().toInt())
                else Instruction('x', it.last().toInt())
            }.toMutableList()
    }

    private fun partOne() {
        val result = foldPaper()
        println("Part one ${result.size}")
    }

    private fun partTwo() {
        isPartOne = false
        val result = foldPaper()
        println("Part two AHGCPGAU ")
        printOutPaper(result)
    }

    private fun foldPaper(): Set<Pair<Int, Int>> {
        var result = pointList

        foldInstructionList.forEach { (axis, yx) ->
            result = foldAxis(result, axis, yx)
            if (isPartOne) return result
        }

        return result
    }

    private fun foldAxis(
        result: Set<Pair<Int, Int>>,
        axis: Char,
        yx: Int
    ): Set<Pair<Int, Int>> {
       return result.map { (y, x) ->
            if (axis == 'y') y to yx - abs(x - yx)
            else yx - abs(y - yx) to x
        }.toSet()
    }

    private fun printOutPaper(result: Set<Pair<Int, Int>>) {
        val (y, x) = result.maxOf { it.first } to result.maxOf { it.second }
        (0..x).forEach { j ->
            println((0..y).joinToString(" ") { i ->
                if (i to j in result) "#" else " "
            })
        }
    }

    data class Instruction(var axis: Char, var yx: Int)
    /*

          # #     #     #     # #       # #     # # #       # #       # #     #     #
        #     #   #     #   #     #   #     #   #     #   #     #   #     #   #     #
        #     #   # # # #   #         #         #     #   #         #     #   #     #
        # # # #   #     #   #   # #   #         # # #     #   # #   # # # #   #     #
        #     #   #     #   #     #   #     #   #         #     #   #     #   #     #
        #     #   #     #     # # #     # #     #           # # #   #     #     # #

    */
}