import java.io.IOException;
import java.net.HttpURLConnection;
import java.net.URL;
import java.util.Scanner;

public class SonarQubeAPIClient {
    public static void main(String[] args) {
        String sonarqubeUrl = "http://your-sonarqube-server.com/api/projects/search";
        String authToken = "your-authentication-token";

        try {
            // Create URL object
            URL url = new URL(sonarqubeUrl);

            // Open connection
            HttpURLConnection connection = (HttpURLConnection) url.openConnection();

            // Set request method
            connection.setRequestMethod("GET");

            // Set request headers
            connection.setRequestProperty("Authorization", "Token " + authToken);
            connection.setRequestProperty("Content-Type", "application/json");

            // Read response
            Scanner scanner = new Scanner(connection.getInputStream());
            StringBuilder response = new StringBuilder();
            while (scanner.hasNextLine()) {
                response.append(scanner.nextLine());
            }
            scanner.close();

            // Print response
            System.out.println(response.toString());

            // Close connection
            connection.disconnect();
        } catch (IOException e) {
            e.printStackTrace();
        }
    }
}
