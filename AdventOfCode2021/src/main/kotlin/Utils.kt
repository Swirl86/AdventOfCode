import java.io.File

class Utils {
    companion object {
        fun print2Dlist(list: ArrayList<IntArray>) {
            for (row in list) {
                println(row.contentToString())
            }
        }

        fun readInput(name: String) = File("src/main/resources/", "$name.txt").readLines()

        fun readInputAsInts(name: String) = File("src/main/resources/", "$name.txt").readLines().map { it.toInt() }
    }
}
