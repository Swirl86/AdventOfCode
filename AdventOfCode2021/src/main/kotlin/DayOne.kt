import java.io.File
import java.io.InputStream

/* https://adventofcode.com/2021/day/1
* How many measurements are larger than the previous measurement?
* part one --> 1139
* part two --> 1103
*/
fun dayOne() {
    /* Part Two */
    var increaseCounter: Int = 0;
    var currentMeasurementA: Int = 0
    var currentMeasurementB: Int = 0

    val list = mutableListOf<Int>()
    File("DayOne.txt").useLines { lines -> lines.forEach { list.add(it.toInt()) } }

    for (i in 1 until (list.size - 2)) {
        if (list[i - 1] < list[i + 2]) increaseCounter++
    }

    println(increaseCounter)
}

/* Part One */
/*  var firstLine: Boolean = true
    var prevDepth: Int = 0;
    var increaseCounter: Int = 0;

    val inputStream: InputStream = File("DayOne.txt").inputStream()

    inputStream.bufferedReader().forEachLine {
        val measurement = it.toInt()
        if(firstLine) {
            prevDepth = measurement
            firstLine = false
        }
        if(measurement > prevDepth) increaseCounter++
        prevDepth = measurement
    }

    println(increaseCounter)
 * */