import java.util.*;
import java.util.function.*;
import java.util.stream.*;

public class ShowAdjacentCountries {

    private static final String TITLE_MESSAGE = "Show Adjacent Country\n";
    private static final String INPUT_PROMPT = "Enter a 2-letter country code or type EXIT to quit: ";
    private static final String INVALID_CODE_MESSAGE = "Invalid or unsupported country code.\n";
    private static final String ADJACENT_COUNTRIES_HEADER = "Adjacent Countries:";
    private static final String EXIT_MESSAGE = "Exiting...";

    
    private static final Map<String, Set<String>> COUNTRY_ADJACENCY =
            Map.ofEntries(
                    Map.entry("IN", Set.of("China", "Pakistan", "Nepal", "Bhutan", "Bangladesh", "Myanmar", "Afghanistan")),
                    Map.entry("US", Set.of("Canada", "Mexico")),
                    Map.entry("CA", Set.of("United States")),
                    Map.entry("MX", Set.of("United States", "Guatemala", "Belize")),
                    Map.entry("CN", Set.of("India", "Mongolia", "Russia", "Nepal","Bhutan", "Myanmar", "Vietnam", "Laos", "North Korea","Pakistan", "Afghanistan", "Kazakhstan", "Kyrgyzstan","Tajikistan")),
                    Map.entry("AU", Set.of("Papua New Guinea", "Indonesia (sea border)", "New Zealand")),
                    Map.entry("NZ", Set.of("Australia"))
            );

    public static void main(String[] args) {

        Scanner scanner = new Scanner(System.in);
        System.out.println(TITLE_MESSAGE);

        Stream.generate(() -> {
                    System.out.print(INPUT_PROMPT);
                    return scanner.nextLine();
                })
                .map(String::trim)
                .map(String::toUpperCase)
                .takeWhile(code -> !code.equals("EXIT"))
                .forEach(processCountryCode());

        System.out.println(EXIT_MESSAGE);
        scanner.close();
    }

    private static Consumer<String> processCountryCode() {
        return countryCode ->
                Optional.of(countryCode)
                        .filter(ShowAdjacentCountries::isValidCountryCode)
                        .map(COUNTRY_ADJACENCY::get)
                        .ifPresentOrElse(
                                ShowAdjacentCountries::printAdjacentCountries,
                                () -> System.out.println(INVALID_CODE_MESSAGE)
                        );
    }

    private static boolean isValidCountryCode(String code) {
        return code.length() == 2 && code.chars().allMatch(Character::isLetter);
    }

    private static void printAdjacentCountries(Set<String> countries) {
        System.out.println(ADJACENT_COUNTRIES_HEADER);
        countries.forEach(country -> System.out.println(" - " + country));
        System.out.println();
    }
}
