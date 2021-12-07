import java.io.File

/* https://adventofcode.com/2021/day/4
* To guarantee victory against the giant squid, figure out which board will win first.
* What will your final score be if you choose that board?
* Part One -> 71708
* Part Two -> 34726
 */

class Day04 {

    private var list = ArrayList<String>()
    private lateinit var boards: List<Day04.Board>
    private lateinit var drawNumbers: List<Int>
    private var winningList = ArrayList<Day04.Board>()

    fun run() {
        loadFile()
        partOne()
        partTwo()
    }

    private fun loadFile() {
        File("data-files/Day04.txt").useLines { lines -> lines.forEach { list.add(it) } }
        setDrawNumbersAndBoards()
    }

    private fun setDrawNumbersAndBoards() {
        drawNumbers = list[0].split(",").map { it.toInt() }

        boards = list.asSequence().drop(2)
            .filterNot { it.isEmpty() }
            .chunked(5)
            .map { rows ->
                rows.map { it ->
                    Regex("[0-9]+").findAll(it)
                        .map(MatchResult::value)
                        .map { BoardEntry(it.toInt(), false) }
                        .toList()
                }
            }
            .map { Board(it) }.toList()
    }

    private fun partOne() {
        val sum = findFirstBingoWinning()
        println("Part one $sum")
    }

    private fun findFirstBingoWinning(): Int {
        var sum = 0

        drawNumbers.forEach {drawnNumber ->
            boards.forEach { board ->
                board.markNumberHits(drawnNumber)

                val bingo = board.checkIfBingo()

                if (bingo) {
                    board.entries.forEach { boardEntry ->
                        sum += boardEntry.filter { !it.marked }.sumOf { it.number }
                    }
                    return sum * drawnNumber
                }
            }
        }
        return sum  // Should not come here
    }

    private fun partTwo() {
        boards.forEach { it.resetMarkedHits() }
        val sum = findLastBingoWinning()
        println("Part Two $sum")
    }

    private fun findLastBingoWinning(): Int {
        var sum = 0
        drawNumbers.forEach {drawnNumber ->
            boards.forEach { board ->
                board.markNumberHits(drawnNumber)
                val bingo = board.checkIfBingo()

                if (bingo && !winningList.contains(board)) {
                    winningList.add(board)
                }

                if(winningList.size == boards.size) {
                    board.entries.forEach { boardEntry ->
                        sum += boardEntry.filter { !it.marked }.sumOf { it.number }
                    }
                    return sum * drawnNumber
                }
            }
        }
        return sum  // Should not come here
    }

    data class BoardEntry(val number: Int, var marked: Boolean)

    data class Board(val entries: List<List<Day04.BoardEntry>>) {

        fun markNumberHits(bingoNumber: Int) {
            entries.forEach { rows ->
                rows.forEach { row ->
                    if (row.number == bingoNumber) row.marked = true
                }
            }
        }

        fun checkIfBingo(): Boolean {
            val verticalBingo = entries.any { rows ->
                rows.all { number -> number.marked } // Returns true if all elements match the given predicate
            }

            val horizontalBingo =  (0 until 5).any { columns ->
                entries.map { row -> row[columns] }.all { number -> number.marked }
            }

            return verticalBingo || horizontalBingo
        }

        fun resetMarkedHits() {
            entries.forEach { rows ->
                rows.forEach { row ->
                    row.marked = false
                }
            }
        }
    }
}