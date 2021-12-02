import java.io.File

class Day02 {
    private val list = mutableListOf<Int>()

    fun run() {
        partOne()
        partTwo()
    }

    private fun loadFile() {
        File("Day02.txt").useLines { lines -> lines.forEach { list.add(it.toInt()) } }
    }

    private fun partTwo() {
        TODO("Not yet implemented")
    }

    private fun partOne() {
        TODO("Not yet implemented")
    }
}