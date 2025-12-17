import java.util.*;
import java.util.function.*;
import java.util.stream.*;

public class ShowAdjacentCountries {

    private static final Map<String, List<String>> COUNTRY_ADJACENCY =
            Map.ofEntries(
                    Map.entry("IN", List.of("China", "Pakistan", "Nepal", "Bhutan", "Bangladesh", "Myanmar", "Afghanistan")),
                    Map.entry("US", List.of("Canada", "Mexico")),
                    Map.entry("CA", List.of("United States")),
                    Map.entry("MX", List.of("United States", "Guatemala", "Belize")),
                    Map.entry("CN", List.of("India", "Mongolia", "Russia", "Nepal", "Bhutan", "Myanmar",
                            "Vietnam", "Laos", "North Korea", "Pakistan", "Afghanistan",
                            "Kazakhstan", "Kyrgyzstan", "Tajikistan")),
                    Map.entry("AU", List.of("Papua New Guinea", "Indonesia (sea border)", "New Zealand")),
                    Map.entry("NZ", List.of("Australia"))
            );

    public static void main(String[] args) {

        Scanner scanner = new Scanner(System.in);
        System.out.println("Show Adjacent Country\n");

        Stream.generate(() -> {
                    System.out.print("Enter a 2-letter country code or type EXIT to quit: ");
                    return scanner.nextLine();
                })
                .map(String::trim)
                .map(String::toUpperCase)
                .takeWhile(code -> !code.equals("EXIT"))
                .forEach(processCountryCode());

        System.out.println("Exiting...");
        scanner.close();
    }

    
    private static Consumer<String> processCountryCode() {
        return countryCode -> Optional.of(countryCode).filter(ShowAdjacentCountries::isValidCountryCode).map(COUNTRY_ADJACENCY::get).ifPresentOrElse(ShowAdjacentCountries::printAdjacentCountries,
         () -> System.out.println("Invalid or unsupported country code.\n")
        );
    }

    
    private static boolean isValidCountryCode(String code) {
        return code.length() == 2 && code.chars().allMatch(Character::isLetter);
    }

 
    private static void printAdjacentCountries(List<String> countries) {
        System.out.println("Adjacent Countries:");
        countries.forEach(country -> System.out.println(" - " + country));
        System.out.println();
    }
}
t
