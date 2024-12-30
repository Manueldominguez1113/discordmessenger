import java.io.IOException;
import java.io.OutputStream;
import java.net.HttpURLConnection;
import java.net.URL;
import java.nio.charset.StandardCharsets;

public class Discordwebhook {
//    static String message = "";
//
//    public static void main(String[] args) {
//        String webhookURL = privatedata.return_webhook();
//        test();
//        try{
//            sendMessage(webhookURL, message);
//        }catch (IOException e){
//            e.printStackTrace();
//        }
//    }

//    private static void sendMessage(String webhookURL, String message) throws IOException {
      private static void sendMessage(String message) throws IOException {
        URL url = new URL(privatedata.return_webhook());
        HttpURLConnection connection = (HttpURLConnection) url.openConnection();
        connection.setRequestMethod("POST");
        connection.setRequestProperty("Content-Type", "application/json");
        connection.setDoOutput(true);

        String jsonPayload = "{\"content\":\"" + message + "\"}";
        byte[] payloadBytes = jsonPayload.getBytes(StandardCharsets.UTF_8);

        try (OutputStream outputStream = connection.getOutputStream()) {
            outputStream.write(payloadBytes);
        }

        int responseCode = connection.getResponseCode();
        if(responseCode == HttpURLConnection.HTTP_OK || responseCode == 204){
            System.out.println("Successfully sent message to Discord");
        } else {
            System.out.println("Failed to send message to Discord. code: " + responseCode);
        }
    }
//
//        private static void test(){
//        Scanner scanner = new Scanner(System.in);
//        System.out.println("enter message:\n");
//        message = scanner.nextLine();
//        }

}