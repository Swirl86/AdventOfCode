import java.io.File

/* https://adventofcode.com/2020/day/4
* detecting which passports have all required fields
* part one --> 192
* part two --> 101
*/
class Day04 {
    private val rows = mutableListOf<Map<String, String>>()

    fun run() {
        loadFile()
        partOne()
        partTwo()
    }

    private fun loadFile() {
        val rowBuilder = mutableListOf<String>()
        File("Day04.txt").useLines { lines ->
            lines.forEach { line ->
                if (line.isEmpty()) {
                    rows.add(splitRows(rowBuilder))
                    rowBuilder.clear()
                } else {
                    rowBuilder.add(line)
                }
            }
        }
        rows.add(splitRows(rowBuilder))// Add last row in file
    }

    private fun splitRows(line: List<String>): Map<String, String> {
        return line
            .flatMap { it.split(" ") }
            .associate {
                val (key, value) = it.split(":")
                Pair(key, value)
            }
    }

    /*
    * byr (Birth Year)
    * iyr (Issue Year)
    * eyr (Expiration Year)
    * hgt (Height)
    * hcl (Hair Color)
    * ecl (Eye Color)
    * pid (Passport ID)
    * cid (Country ID) <-- Treat cid as optional
    */
    private fun partOne() {
        val validPassport = rows.stream().filter() { row ->
            row.containsKey("byr") && row.containsKey("iyr") && row.containsKey("eyr")
                    && row.containsKey("hgt") && row.containsKey("hcl") && row.containsKey("ecl")
                    && row.containsKey("pid")
        }.count()

        println("Part One : $validPassport")
    }

    private fun partTwo() {
        // 91 WRONG
        val validPassport = rows.stream().filter() { row ->
            row.containsKey("byr") && validByr(row.getValue("byr")) &&
            row.containsKey("iyr") && validIyr(row.getValue("iyr")) &&
            row.containsKey("eyr") && validEyr(row.getValue("eyr")) &&
            row.containsKey("hgt") && validHgt(row.getValue("hgt")) &&
            row.containsKey("hcl") && validHcl(row.getValue("hcl")) &&
            row.containsKey("ecl") && validEcl(row.getValue("ecl")) &&
            row.containsKey("pid") && validPid(row.getValue("pid"))
            /* cid (Country ID) - ignored, missing or not.*/
        }.count()

        println("Part Two : $validPassport")
    }

    private fun validByr(value: String): Boolean {
        // byr (Birth Year) - four digits; at least 1920 and at most 2002.
        return value.all { it in '0'..'9' } && inRange(value.toInt(), 1920,2002)
    }

    private fun validIyr(value: String): Boolean {
        // iyr (Issue Year) - four digits; at least 2010 and at most 2020.
        return value.all { it in '0'..'9' } && inRange(value.toInt(), 2010, 2020)
    }

    private fun validEyr(value: String): Boolean {
        // eyr (Expiration Year) - four digits; at least 2020 and at most 2030.
        return value.all { it in '0'..'9' } && inRange(value.toInt(), 2020, 2030)
    }

    private fun validHgt(value: String): Boolean {
        /* hgt (Height) - a number followed by either cm or in:
        If cm, the number must be at least 150 and at most 193.
        If in, the number must be at least 59 and at most 76. */
        return if(value.endsWith("cm")) inRange(value.substring(0, value.length-2).toInt(), 150, 193)
        else if(value.endsWith("in")) inRange(value.substring(0, value.length-2).toInt(), 59, 76)
        else false
    }

    private fun validHcl(value: String): Boolean {
        // hcl (Hair Color) - a # followed by exactly six characters 0-9 or a-f.
        val pattern = Regex("[a-f0-9]{6}")
        return value.startsWith("#") && pattern.matches(value.substring(1,7))
    }

    private fun validEcl(value: String): Boolean {
        // ecl (Eye Color) - exactly one of: amb blu brn gry grn hzl oth.
        return value == "amb" || value == "blu" || value == "brn" || value == "gry"
                || value == "grn" || value == "hzl" || value == "oth"
    }

    private fun validPid(value: String): Boolean {
        // pid (Passport ID) - a nine-digit number, including leading zeroes.
        return value.all { it in '0'..'9' } && value.length == 9
    }

    private fun inRange(value:Int, low: Int, high: Int): Boolean{
        return (value.toInt() in low..high)
    }
}