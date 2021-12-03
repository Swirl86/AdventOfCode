import java.io.File
import java.math.BigInteger

/* https://adventofcode.com/2020/day/3
* how many trees would you encounter?
* part one --> 247 Rule 3 right and 1 down
* part two --> 2983070376
Rule :
Right 1, down 1.
Right 3, down 1. (Part One)
Right 5, down 1.
Right 7, down 1.
Right 1, down 2.
*/
class Day03 {

    private val rows = mutableListOf<String>()
    private val tree: Char = '#'
    private var rowWidth: Int = 0

    fun run() {
        loadFile()
        partOne()
        partTwo()
    }

    private fun loadFile() {
        File("data-files/Day03.txt").forEachLine {
            rows.add(it)
        }
        rowWidth = rows[0].length
    }

    private fun partOne() {
        //Rule 3 right and 1 down
        val encounteredTrees: Int = traverseTheMap(3, 1)
        println("Part One : $encounteredTrees")
    }

    private fun partTwo() {
        val slopes = arrayOf(arrayOf(1, 1), arrayOf(3, 1), arrayOf(5, 1), arrayOf(7, 1), arrayOf(1, 2))
        // Result will be too big for an Int, if an Int is used the value will be negative can't handle the big result
        var encounteredTrees: Long = 1; // Start at 1 to avoid multiply with 0

        slopes.forEach { (right, down) ->
            encounteredTrees *= traverseTheMap(right, down)
        }

        println("Part Two : $encounteredTrees")
    }


    private fun traverseTheMap(rightMove: Int, downMove: Int): Int {
        var treeEncounters: Int = 0;
        var columnIndex: Int = 0

        for (rowIndex in rows.indices step downMove) {
            // modular always stays within the length of the row - travers each row
            // using the remainder as index value, from 0 to rowWidth - 1.
            if (rows[rowIndex][columnIndex % rowWidth] == tree) treeEncounters++
            columnIndex += rightMove
        }
        return treeEncounters
    }

}
/* Part One before refactor
val rowWidth: Int = rows[0].length
    var encounteredTrees: Int = 0;
    var columnIndex: Int = 0

    for (rowIndex in rows.indices) { // Every row - down 1 rule
        if(rows[rowIndex][columnIndex % rowWidth] == tree) encounteredTrees++
        columnIndex += 3 // Every column - right 3 rule
    }

    println("Part One : $encounteredTrees")
*/