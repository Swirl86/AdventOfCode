import java.io.File

/* https://adventofcode.com/2020/day/2
* Validated the passwords
* part one --> 515
* part two --> 711
*/
class Day02 {

    fun run() {
        partOne()
        partTwo()
    }

    private fun partOne() {
        var validPasswords: Int = 0;

        File("src/main/resources/Day02.txt").useLines { lines ->
            lines.forEach { line ->
                val row: List<String> = line.split(" ")
                val range: List<String> = row[0].split("-")
                val ch: Char = row[1].split(":")[0].single()
                val occurrences: Int = row[2].count { it == ch }

                if (occurrences <= range[1].toInt() && occurrences >= range[0].toInt()) validPasswords++
            }
        }
        println("Part One : $validPasswords")
    }

    private fun partTwo() {
        var validPasswords: Int = 0;

        File("data-files/Day02.txt").useLines { lines ->
            lines.forEach { line ->
                val row: List<String> = line.split(" ")
                val range: List<String> = row[0].split("-")
                val ch: Char = row[1].split(":")[0].single()
                val password: CharArray = row[2].toCharArray()

                if (password[range[0].toInt() - 1] !=  password[range[1].toInt() - 1] &&
                    (password[range[0].toInt() - 1] == ch || password[range[1].toInt() - 1] == ch)) validPasswords++
            }
        }
        println("Part Two : $validPasswords")
    }
}
