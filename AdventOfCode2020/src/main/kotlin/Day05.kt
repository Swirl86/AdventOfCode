import java.io.File
import java.util.stream.Stream


/*https://adventofcode.com/2020/day/5
* What is the highest seat ID on a boarding pass?
* part one --> 919
* part two --> 642
*/
class Day05 {

    private val list = mutableListOf<String>()
    private val boardingPassList = mutableListOf<Int>()

    fun run() {
        loadFile()
        partOne()
        partTwo()
    }

    private fun loadFile() {
        File("src/main/resources/Day05.txt").forEachLine {
            list.add(it)
        }
    }

    /* 128 Rows 8 columns
     The first 7 characters will either be F or B
     front (0 through 63) or the back (64 through 127)
     last three characters will be either L or R 0 - 7
     F and L - Lower half
     B and R - upper half */
    private fun partOne() {
         var highestBoardingPass = 0

         for (i in 0 until list.size) {
             val rowNumber = seatIdLoop(list[i], 'F', 'B', 128)
             val columnNumber = seatIdLoop(list[i], 'L', 'R', 8)
             val boardingPass = (rowNumber * 8) + columnNumber
             if(boardingPass > highestBoardingPass) highestBoardingPass = boardingPass

             // For part two
             boardingPassList.add(boardingPass)
         }

        println("Part One : $highestBoardingPass")
    }

    private fun seatIdLoop(row: String, lowHalf: Char, upperHalf: Char, range: Int): Int {
        var upperRange = range
        var lowerRange = 0

        for (i in row.indices) {
            val middle = (upperRange + lowerRange) / 2
            when(row[i]) {
                lowHalf -> upperRange = middle // F or L
                upperHalf -> lowerRange = middle // B or R
            }
        }
        return lowerRange
    }

    private fun partTwo() {
        boardingPassList.sort()
        var missingSeatId = 0

        Stream.iterate(1) { i -> i + 1 }
            .takeWhile { i -> i < boardingPassList.size - 1 }
            .forEach { i ->
                if((boardingPassList[i] + 1) !=  boardingPassList[i+1])
                    missingSeatId = boardingPassList[i] + 1
            }

        println("Part Two : $missingSeatId")
    }

}