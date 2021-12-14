import java.io.File

class Day13 {
    private val list = arrayListOf<String>()

    fun run() {
        loadFile()
        partOne()
        partTwo()
    }

    /*
    *  if (y - 1 >= 0 && currentValue >= list[y - 1][x]) continue // Bottom
                if (y + 1 < list.size && currentValue >= list[y + 1][x]) continue // Top
                if (x - 1 >= 0 && currentValue >= list[y][x - 1]) continue // Left
                if (x + 1 < list[y].size && currentValue >= list[y][x + 1]) continue // Right
    * */
    private fun loadFile() {
        File("src/main/resources/Day13.txt").useLines { lines -> lines.forEach { list.add(it) } }
    }

    private fun partOne() {
        TODO("Not yet implemented")
    }

    private fun partTwo() {
        TODO("Not yet implemented")
    }

    data class Point(val y: Int, val x: Int)
}