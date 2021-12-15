import java.io.File

/* https://adventofcode.com/2021/day/12
* How many paths through this cave system are there?
* Part One -> 3421
* Part Two -> 84870
 */
class Day12 {

    private var caveList = mapOf<String, List<String>>()
    private var partTwo = false

    fun run() {
        loadFile()
        partOne()
        partTwo()
    }

    private fun loadFile() {
        caveList = File("src/main/resources/Day12.txt").readText()
            .split("\r\n")
            .map { it.split("-") }
            .flatMap { // Returns a single list of all elements yielded from results of transform function being invoked on each element of original collection.
                listOf(
                    it.first() to it.last(),
                    it.last() to it.first()
                )
            }
            .groupBy(
                { it.first },
                { it.second }) // Returns a map where each group key is associated with a list of corresponding values
    }

    private fun partOne() {
        val paths =  recursivePathsDepthFirst(listOf("start"))
        println("Part one ${paths.size}")
    }

    private fun partTwo() {
        partTwo = true
        val paths =  recursivePathsDepthFirst(listOf("start"))
        println("Part two ${paths.size}")
    }

    // https://en.wikipedia.org/wiki/Depth-first_search
    private fun recursivePathsDepthFirst(node: List<String>, canRevisit: Boolean = false): List<List<String>> { //procedure DFS(G, v) is
        val current = node.last() // label v as discovered

        if(current == "end") { // stop here end of values
            return listOf(node)
        }
        // for all directed edges from v to w that are in G.adjacentEdges(v) do
        return caveList.getValue(current)
            .filterNot { validFilterOptions(it, node, canRevisit) } // if vertex w is not labeled as discovered then
            .flatMap {
                recursivePathsDepthFirst( // recursively call DFS(G, w)
                    node + it,
                    getRevisitBoolean(canRevisit, it, node),
                )
            }
    }

    private fun validFilterOptions(
        it: String,
        node: List<String>,
        canRevisit: Boolean
    ) = (it == "start") || (isLowerCase(it) && (it in node) && if (partTwo) canRevisit else true)

    private fun getRevisitBoolean(
        canRevisit: Boolean,
        it: String,
        node: List<String>
    ) = canRevisit || isLowerCase(it) && it in node // Returns true if one of the statements is true

    private fun isLowerCase(value: String): Boolean = value.all { it.isLowerCase() }

  //  private fun isUpperCase(value: String): Boolean = value.all { it.isUpperCase() }

}