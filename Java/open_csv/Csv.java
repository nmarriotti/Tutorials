import java.io.BufferedReader;
import java.io.FileReader;
import java.io.IOException;

public class Csv {

    public static void main(String[] args) {

        String csvFile = "test.csv";
        String line = "";
        String cvsSplitBy = ",";
        boolean first_pass = true;

        try (BufferedReader br = new BufferedReader(new FileReader(csvFile))) {

            while ((line = br.readLine()) != null) {

                if(!first_pass) {
                    // use comma as separator
                    String[] country = line.split(cvsSplitBy);
                    System.out.println("Name: " + country[1] + " , Age: " + country[2]);
                }
                first_pass = false;

            }

        } catch (IOException e) {
            e.printStackTrace();
        }

    }

}