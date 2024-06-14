/* https://adventofcode.com/2021/day/14
* How many dots are visible after completing just the first fold instruction on your transparent paper?
* Part One -> 3411
* Part Two -> 7477815755570
 */
class Day14 {
    private var list = Utils.readInput("Day14")
    private var pairInsertionRules = mutableMapOf<Pair<Char, Char>, Char>()
    private var polymerTemplateList = mutableMapOf<Pair<Char, Char>, Long>()

    fun run() {
         splitInput()
         partOne()
         partTwo()
    }

    private fun splitInput() {
        polymerTemplateList =
            list.first().zipWithNext() // Returns a list of pairs of each two adjacent characters in this char sequence
                //The returned list is empty if this char sequence contains less than two characters.
                .groupingBy { it }
                .eachCount()
                .mapValues { (_, value) -> value.toLong() } as MutableMap<Pair<Char, Char>, Long>

        pairInsertionRules = list.takeLastWhile { it.isNotEmpty() }
            .associate {
                val (pair, insertion) = it.split(" -> ")
                (pair[0] to pair[1]) to insertion.first()
            } as MutableMap<Pair<Char, Char>, Char>
    }

    private fun partOne() {
        val resultMap = insertionLoop(10)
        val newResultMap = mergeResultMap(resultMap)
        println("Part one " + (newResultMap.values.let { it.maxOrNull()?.minus(it.minOrNull()!!) ?: 0 }))
    }

    private fun partTwo() {
        val resultMap = insertionLoop(40)
        val newResultMap = mergeResultMap(resultMap)
        println("Part two " + (newResultMap.values.let { it.maxOrNull()?.minus(it.minOrNull()!!) ?: 0 }))
    }

    private fun insertionLoop(xTimes: Int): MutableMap<Pair<Char, Char>, Long> {
        // pairInsertionRules  {(C, H)=B, (H, H)=N, (C, B)=H, (N, H)=C, (H, B)=C, (H, C)=B, (H, N)=C, (N, N)=C, . . .
        var copyPolymerList = polymerTemplateList// polymerTemplateList = NNCB <- {(N, N)=1, (N, C)=1, (C, B)=1}

        repeat(xTimes) {
            val newPolymerList = mutableMapOf<Pair<Char, Char>, Long>()
            // Before first forEach loop {(N, N)=1, (N, C)=1, (C, B)=1}
            copyPolymerList.forEach { (pair, value) ->
                // First loop (pair, value) = (N,N) 1  Rule says NN -> C
                newPolymerList.merge(pairInsertionRules[pair]!! to pair.second, value, Long::plus) // {(C, N)=1}
                newPolymerList.merge(pair.first to pairInsertionRules[pair]!!, value, Long::plus) //  {(N, C)=1}
                // newPolymerList = {(C, N)=1, (N, C)=1} added both combinations with own counter
                // If combination does not exist add new. If combination exists count up
            }
            // After first forEach loop {(C, N)=1, (N, C)=1, (B, C)=1, (N, B)=1, (H, B)=1, (C, H)=1}
            copyPolymerList = newPolymerList
        }
        return copyPolymerList
    }

    private fun mergeResultMap(resultMap: MutableMap<Pair<Char, Char>, Long>): MutableMap<Char, Long> {
        val newResultMap = mutableMapOf<Char, Long>()
        // From {(C, N)=2541358752, (C, C)=1451671811, (N, C)=1089686941, . . .
        resultMap.forEach { (pair, value) -> newResultMap.merge(pair.first, value, Long::plus) } // If combination exists count up
        // To {N=1096047802352, C=6597635301, B=2192039569602, H=3849876073}
        return newResultMap
    }
}