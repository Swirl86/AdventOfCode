import java.io.File

/*https://adventofcode.com/2020/day/7
* How many bag colors can eventually contain at least one shiny gold bag?
* part one --> 124
* part two --> 34862
*/
class Day07 {

    private val luggageList = ArrayList<String>()
    private lateinit var bagRelations: Set<BagRule>

    fun run() {
        loadFile()
        partOne()
        partTwo()
    }

    private fun loadFile() {
        File("data-files/Day07.txt").forEachLine { luggageList.add(it) }
    }

    private fun partOne() {
        // A generic unordered collection of elements that does not support duplicate elements.
        bagRelations = parseLuggageList()
        println("Part One : ${findParentsRecursion().size - 1} ")
    }

    private fun partTwo() {
        println("Part Two : ${bagCostRecursion() - 1} ")
    }

    private fun parseLuggageList(): Set<BagRule> {
        // Returns a single list of all elements yielded from results of transform function being invoked on each element of original collection.
        return luggageList.filterNot { it.contains("no other") }.flatMap { row ->
            val (bagType, containsBags) = row
                .replace(wastedTxt, "") //wastedTxt <- bags bag , .
                .split("contain")
                .map { it.trim() }

            val bags = containsBags.split(" ").map { it.trim() } // [4, shiny, lavender, , 5, dull, orange]

            bags.filter { x -> x.isNotEmpty() }
                // Returns a list of snapshots of the window of the given size sliding along this collection with the given step, where each snapshot is a list.
                .windowed(3, 3).map { child ->// Pattern is 3 values : number str str <-- 4, shiny, lavender
                    BagRule(
                        bagType,
                        child.first().toInt(),
                        child.drop(1).joinToString(" ")
                    )
                }
        }.toSet() // The returned set preserves the element iteration order of the original collection.
    }

    private fun findParentsRecursion(bag: String = "shiny gold"): Set<String> {
        return bagRelations
            .filter { it.child == bag }
            .flatMap { findParentsRecursion(it.parent) }.toSet() + bag
    }

    private fun bagCostRecursion(bag: String = "shiny gold"): Int {
        return bagRelations
            .filter { it.parent == bag }
            .sumOf { it.cost * bagCostRecursion(it.child) } + 1
    }

    companion object {
        private const val goldBag = "shiny gold"
        private val wastedTxt = """bags|bag|,|\.""".toRegex() // bags before bag to avoid alone s
        private val whitespace = """\s+""".toRegex()
    }

    //A tree data structure - Node: Any single item in the tree, usually a key-value item.
    // parent <- root - The initial node of the tree, where all the operations start / The converse notion of a child
    // cost <- how many bags for part two
    // child <- inner bag - A node directly connected to another node when moving away from the root.
    private data class BagRule(val parent: String, val cost: Int, val child: String)
}