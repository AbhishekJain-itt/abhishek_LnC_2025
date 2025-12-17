import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.net.HttpURLConnection;
import java.net.URL;
import java.util.Scanner;
import java.util.regex.Matcher;
import java.util.regex.Pattern;

public class TumblrImageFetcher {

    public static void main(String[] args) {

        Scanner scanner = new Scanner(System.in);

        System.out.print("Enter the Tumblr blog name: ");
        String blogName = scanner.nextLine().trim();

        System.out.print("Enter the range (start-end): ");
        String range = scanner.nextLine().trim();

        int start = Integer.parseInt(range.split("-")[0]);
        int end = Integer.parseInt(range.split("-")[1]);

        try {
            fetchAndPrintData(blogName, start, end);
        } catch (Exception e) {
            System.out.println("Error while fetching Tumblr data.");
            e.printStackTrace();
        }

        scanner.close();
    }

    private static void fetchAndPrintData(String blogName, int start, int end) throws Exception {

        String apiUrl = "https://" + blogName + ".tumblr.com/api/read/json?type=photo";
        String response = readFromUrl(apiUrl);

        
        response = response.replace("var tumblr_api_read = ", "").trim();
        if (response.endsWith(";")) {
            response = response.substring(0, response.length() - 1);
        }

        printBasicBlogInfo(response);
        printImageUrls(response, start, end);
    }

    private static String readFromUrl(String urlString) throws Exception {

        URL url = new URL(urlString);
        HttpURLConnection connection = (HttpURLConnection) url.openConnection();
        connection.setRequestMethod("GET");

        BufferedReader reader =
                new BufferedReader(new InputStreamReader(connection.getInputStream()));

        StringBuilder result = new StringBuilder();
        String line;

        while ((line = reader.readLine()) != null) {
            result.append(line);
        }

        reader.close();
        return result.toString();
    }

    private static void printBasicBlogInfo(String json) {

        System.out.println("\nBlog Information:");
        printField(json, "title");
        printField(json, "name");
        printField(json, "description");
        printField(json, "posts-total");
        System.out.println();
    }

    private static void printField(String json, String fieldName) {

        Pattern pattern =
                Pattern.compile("\"" + fieldName + "\"\\s*:\\s*\"?(.*?)\"?,");
        Matcher matcher = pattern.matcher(json);

        if (matcher.find()) {
            System.out.println(fieldName + ": " + matcher.group(1));
        }
    }

   
    private static void printImageUrls(String json, int start, int end) {

        Pattern imagePattern =
                Pattern.compile("\"photo-url-1280\"\\s*:\\s*\"(.*?)\"");
        Matcher matcher = imagePattern.matcher(json);

        int imageIndex = 0;
        int outputIndex = 1;

        System.out.println("Images:");

        while (matcher.find()) {
            imageIndex++;

            if (imageIndex >= start && imageIndex <= end) {
                System.out.println(outputIndex + ". " + matcher.group(1));
                outputIndex++;
            }

            if (imageIndex > end) {
                break;
            }
        }
    }
}
