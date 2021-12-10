import java.io.File

/* https://adventofcode.com/2021/day/3
* Use the binary numbers in your diagnostic report to calculate the gamma rate and epsilon rate, then multiply them together.
* Part One -> 2261546
* Part Two -> 6775520
 */
class Day03 {
    private val list = mutableListOf<String>()

    fun run() {
        loadFile()
        partOne()
        partTwo()
    }

    private fun loadFile() {
        File("src/main/resources/Day03.txt").useLines { lines -> lines.forEach { list.add(it) } }
    }

    private fun partOne() {
        val gammaRate = StringBuilder() // most common bit in the corresponding position (columns)
        val epsilonRate = StringBuilder() // the least common bit in the corresponding position
        val rowWidth = list[0].length

        for (i in 0 until rowWidth) {
            val zeroCount = list.stream().filter{ it[i] == '0'}.count()
            val oneCount = list.size - zeroCount

            if(zeroCount > oneCount) {
                gammaRate.append(0)
                epsilonRate.append(1)
            } else {
                gammaRate.append(1)
                epsilonRate.append(0)
            }
        }

        val gamma = Integer.parseInt(gammaRate.toString(), 2)
        val epsilon = Integer.parseInt(epsilonRate.toString(), 2)
        println("Part One : ${gamma * epsilon}")
    }

    private fun partTwo() {
        val oxygenGeneratorRating: String = getOxygenGeneratorRating()
        val cO2ScrubberRating: String = getCO2ScrubberRating()
        val gamma = Integer.parseInt(oxygenGeneratorRating, 2)
        val epsilon = Integer.parseInt(cO2ScrubberRating, 2)
        println("Part Two : ${gamma * epsilon}")
    }

    private fun getOxygenGeneratorRating(): String {
        // determine the most common value (0 or 1) in the current bit position
        // If 0 and 1 are equally common, keep values with a 1 in the position being considered
        var oxygenList  = list.toMutableList()
        var i = 0
        do {
            val zeroCount = oxygenList.stream().filter{x -> x[i] == '0'}.count()
            val oneCount = oxygenList.stream().filter{x -> x[i] == '1'}.count()

            oxygenList = if(oneCount >= zeroCount ) {
                oxygenList.stream().filter{it -> it[i] == '1'}.toList()
            } else {
                oxygenList.stream().filter{it -> it[i] == '0'}.toList()
            }
            i++
        } while (oxygenList.size > 1);

        return oxygenList[0]
    }

    private fun getCO2ScrubberRating(): String {
        // determine the least common value (0 or 1) in the current bit position
        // if 0 and 1 are equally common, keep values with a 0 in the position being considered
        var cO2List  = list.toMutableList()
        var i = 0
        do {
            val zeroCount = cO2List.stream().filter{it -> it[i] == '0'}.count()
            val oneCount = cO2List.stream().filter{it -> it[i] == '1'}.count()

            cO2List = if(zeroCount <= oneCount) {
                cO2List.stream().filter{it -> it[i] == '0'}.toList()
            } else {
                cO2List.stream().filter{it -> it[i] == '1'}.toList()
            }
            i++
        } while (cO2List.size > 1);

        return cO2List[0]
    }
}