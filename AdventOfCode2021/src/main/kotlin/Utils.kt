class Utils {
    companion object {
        fun print2Dlist(list: ArrayList<IntArray>) {
            for (row in list) {
                println(row.contentToString())
            }
        }
    }
}
