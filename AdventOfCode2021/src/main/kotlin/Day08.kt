import java.io.File
import java.util.*


/* https://adventofcode.com/2021/day/8
* In the output values, how many times do digits 1, 4, 7, or 8 appear?
* Part One -> 440
* Part Two -> 1046281
 */
class Day08 {

    private var sevenSegmentDisplay: ArrayList<Segments> = arrayListOf()
    private val segmentsKeys = arrayOf("abcefg",  "cf", "acdeg", "acdfg", "bcdf", "abdfg", "abdefg", "acf", "abcdefg", "abcdfg")

    fun run() {
        loadFile()
        partOne()
        partTwo()
    }

    private fun loadFile() {
      File("data-files/Day08.txt").readText()
            .split("\n")
            .map {
                sevenSegmentDisplay.add(getValues(it))
            }
    }

    private fun getValues(line: String): Segments {
        val (signal, digit) = line.split("|")
        val pattern = """\w+""".toRegex()
        val signalPatterns = pattern.findAll(signal).map { it.value.alphabetized() }.toList()
        val digitOutput = pattern.findAll(digit).map { it.value.alphabetized() }.toList()
        return Segments(signalPatterns, digitOutput)
    }

    private fun partOne() {
        var count = 0
        sevenSegmentDisplay.forEach { segment ->
           segment.digitOutput.forEach {
                // Digits: 1, 4, 7 or 8
                    when (it.length) {
                    2, 3, 4, 7 -> count++
                }
           }
        }

        println("Part One $count")
    }

    private fun partTwo() {
        val result = mutableListOf<Int>()

        sevenSegmentDisplay.forEach { segment ->
            var digitValue = ""

            segment.digitOutput.forEach { digit ->
                // Check digitOutput length for value
                digitValue += when (digit.length) {
                    // Part one Digits: 1, 4, 7 or 8 unique digits
                    2 -> '1'
                    3 -> '7'
                    4 -> '4'
                    7 -> '8'
                    5-> when(getRemainderInPatternSize(segment, digit, 4)) {
                        // Can be 2, 3 or 5
                        // acdeg  -  acdfg  -  abdfg
                        2 -> '2'
                        3 -> if (getRemainderInPatternSize(segment, digit, 2) == 1) '5' else '3'
                        else -> throw IllegalArgumentException()
                    }
                    6-> when(getRemainderInPatternSize(segment, digit, 4)) {
                        // Can be 0, 6 or 9
                        // abcefg  -  abdefg  -  abcdfg
                        4 -> '9'
                        3 -> if (getRemainderInPatternSize(segment, digit, 2) == 1) '6' else '0'
                        else -> throw IllegalArgumentException()
                    }
                    else -> throw IllegalArgumentException()
                }
            }
           result.add(digitValue.toInt())
        }

        println("Part Two ${result.sum()}")
    }

    private fun getRemainderInPatternSize(segment: Segments, digit: String, i: Int): Int {
        val possiblePatterns = segment.signalPatterns.filter { it.length == i }[0]
        return possiblePatterns.toCharArray().intersect(digit.toCharArray().toSet()).size
    }

    // Sort chars in string
    private fun String.alphabetized() = String(toCharArray().apply { sort() })

    // signalPatterns - 10 values,  digitOutput - 4 values
    data class Segments(val signalPatterns: List<String>, val digitOutput: List<String>)
}