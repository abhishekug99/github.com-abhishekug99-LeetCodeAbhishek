import java.util.regex.*

fun solution(src: String): String {
    val pattern = Regex("(\\_*)([a-z]+(?:_[a-z]+)*)(\\_*)")

    return pattern.replace(src) { matchResult ->
        val prefix = matchResult.groups[1]?.value ?: ""
        val core = matchResult.groups[2]?.value ?: ""
        val suffix = matchResult.groups[3]?.value ?: ""

        val camelCase = core.split("_").mapIndexed { index, word ->
            if (index == 0) word else word.replaceFirstChar { it.uppercase() }
        }.joinToString("")

        "$prefix$camelCase$suffix"
    }
}

// Example usage
fun main() {
    val src = "this_is_a_test _another_example_ example_with__multiple_underscores_"
    println(solution(src))
}
