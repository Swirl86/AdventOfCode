import java.io.File

/* https://adventofcode.com/2021/day/6
* Find a way to simulate lanternfish. How many lanternfish would there be after X days?
* Part One -> 376194
* Part Two -> 1693022481538
 */
class Day06 {

    private var lanternFishList: ArrayList<Int> = arrayListOf()

    fun run() {
        loadFile()
        partOne()
        partTwo()
    }

    private fun loadFile() {
        val values = File("data-files/Day06.txt").readText()
        values.split(",").map{
            lanternFishList.add(it.toInt())
        }
    }

    private fun partOne() {
        println("Part One ${modelFishGrowthForGivenDays(80)}")
    }

    private fun partTwo() {
        println("Part Two ${modelFishGrowthForGivenDays(256)}")
    }

    private fun modelFishGrowthForGivenDays(cycles: Int): Long {
        val fishGrowth = MutableList<Long>(9) { 0 }
        for (i in 0..8) {
            // Returns the number of elements matching the given predicate.
            // Can only be values between 0-8 (0 = time for new fish, 8 = new fish timer)
            fishGrowth[i] = lanternFishList.count { it == i }.toLong()
        }


        for (i in 0 until cycles) {
            val fishStartNewCycle = fishGrowth.removeFirst()
            fishGrowth[6] += fishStartNewCycle // Reset 6 day cycle and add prev value
            fishGrowth.add(fishStartNewCycle) // create new fish on 8 day cycle
        }

        return fishGrowth.sum()
    }
}