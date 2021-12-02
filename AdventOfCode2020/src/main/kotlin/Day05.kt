import java.io.File

/*https://adventofcode.com/2020/day/5
* What is the highest seat ID on a boarding pass?
* part one -->
* part two -->
*/
class Day05 {

    private val rows = mutableListOf<String>()

    fun run() {
        loadFile()
        //partOne()
        //partTwo()
    }

    private fun loadFile() {
        File("Day05.txt").forEachLine {
            rows.add(it)
        }
    }

    private fun partOne() {
        TODO("Not yet implemented")
    }

    private fun partTwo() {
        TODO("Not yet implemented")
    }

}