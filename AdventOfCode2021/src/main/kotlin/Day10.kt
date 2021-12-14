import java.io.File

/* https://adventofcode.com/2021/day/10
* Find the first illegal character in each corrupted line of the navigation subsystem.
* Find the completion string for each incomplete line, score the completion strings, and sort the scores.
* Part One -> 364389
* Part Two -> 2870201088
 */
class Day10 {

    private val list = arrayListOf<String>()
    private val openClosePair = mapOf("(" to ")", "[" to "]", "{" to "}", "<" to ">")
    private var syntaxErrorPointMap = mapOf(")" to 3, "]" to 57, "}" to 1197, ">" to 25137)
    private val closingPointMap = mapOf(")" to 1, "]" to 2, "}" to 3, ">" to 4)

    private val legalLines: ArrayList<MutableList<String>> = arrayListOf()
    private val illegalScoreList: ArrayList<Long> = arrayListOf()

    fun run() {
        loadFile()
        partOne()
        partTwo()
    }

    private fun loadFile() {
        File("src/main/resources/Day10.txt").readText()
            .split("\r\n")
            .map {
                list.add(it)
            }
    }

    //Some lines are incomplete, but others are corrupted. Find and discard the corrupted lines first.
    private fun partOne() {
        var result = 0L

        list.forEach charLoop@ { line ->
            val values: MutableList<String> = mutableListOf()
            for (c in line.toCharArray()) {
                val character = c.toString()
                if (openClosePair.containsKey(character)) {
                    values.add(character)
                } else {
                    val symbol = values.removeLast()
                    if (openClosePair[symbol] != character) {
                        result += syntaxErrorPointMap.getValue(character).toLong()
                        return@charLoop // simulate continue
                    }
                }
            }
            legalLines.add(values) // For part two, valid openings
        }
        println("Part one $result")
    }

    private fun partTwo() {
       legalLines.forEach { line ->
            val point = getPoints(line)
            illegalScoreList.add(point)
        }
        illegalScoreList.sort()
        val index = illegalScoreList.size / 2
        println("Part two ${illegalScoreList[index]}")
    }

    private fun getPoints(line: MutableList<String>): Long {
        var points = 0L
        while (line.isNotEmpty()) {
            val openingSymbol = line.removeLast()
            val closingSymbol = openClosePair[openingSymbol]
            points *= 5 // multiply the total score by 5
            points += closingPointMap.getValue(closingSymbol!!)
                .toLong() // then increase the total score by the point value given for the character
        }
        return points
    }
}