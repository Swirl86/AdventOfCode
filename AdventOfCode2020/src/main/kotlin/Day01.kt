import java.io.File
import java.io.InputStream

/* https://adventofcode.com/2020/day/1
* Find the two entries that sum to 2020 and then multiply those two numbers together
* part one --> 539851
* part two --> 212481360
*/
class Day01 {

    fun run() {
        partOne()
        partTwo()
    }

    private fun partOne() {
        var found: Boolean = false;

        val list = mutableListOf<Int>()
        File("src/main/resources/Day01.txt").useLines { lines -> lines.forEach { list.add(it.toInt()) } }

        list.forEach { i ->
            list.forEach { j ->
                if((i + j) == 2020) {
                    println("Part One : $i  *  $j =  " + (i*j) )
                    found = true;
                    return@forEach
                }
            }
            if(found) return@forEach
        }
    }

    private fun partTwo() {
        var found: Boolean = false;

        val list = mutableListOf<Int>()
        File("data-files/Day01.txt").useLines { lines -> lines.forEach { list.add(it.toInt()) } }

        list.forEach { i ->
            list.forEach { j ->
                list.forEach { k ->
                    if((i + j + k) == 2020) {
                        println("Part Two : $i  *  $j * $k =  " + (i*j*k) )
                        found = true;
                        return@forEach
                    }
                }
                if(found) return@forEach
            }
            if(found) return@forEach
        }
    }
}
