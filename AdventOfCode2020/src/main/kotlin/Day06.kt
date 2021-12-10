import java.io.File
/*https://adventofcode.com/2020/day/6
* For each group, count the number of questions to which anyone answered "yes". What is the sum of those counts?
* part one --> 6633
* part two --> 3202
*/
class Day06 {
    private val list = mutableListOf<String>()
    private val groups = mutableListOf<MutableList<String>>()

    fun run() {
        loadFile()
        partOne()
        partTwo()
    }

    private fun loadFile() {
        File("src/main/resources/Day06.txt").forEachLine { list.add(it) }

    }

    private fun partOne() {
        var rowBuilder = ""
        var sum:Long = 0
        list.forEach { row ->
            if (row.isEmpty()) {
                sum += rowBuilder.chars().distinct().count()
                rowBuilder = ""
            } else {
                rowBuilder += row
            }
        }
        sum += rowBuilder.chars().distinct().count()
        println("Part One : $sum")
    }

    private fun partTwo() {
        var sum:Long = 0

        val rowBuilder = mutableListOf<String>()
        list.forEach { row ->
            if (row.isEmpty()) {
                sum += countYesAnswers(rowBuilder)
                rowBuilder.clear()
            } else {
                rowBuilder.add(row)
            }
        }
        sum += countYesAnswers(rowBuilder)
        println("Part Two : $sum")
    }

    private fun countYesAnswers(group: MutableList<String>): Int {
        if(group.size == 1) return group[0].length
        // toSet - a Set of all characters
        // reduceRight - Accumulates value starting with the last element and applying operation from right to left to each element and current accumulator value.
        // intersect - Returns a set containing all elements that are contained by both this collection and the specified collection.
        return group.map(String::toSet).reduceRight(Set<Char>::intersect).size
      //  return group.sumOf { it -> it.lines().reduce{ s, t -> s.filter{ it in t } }.length}
    }
}