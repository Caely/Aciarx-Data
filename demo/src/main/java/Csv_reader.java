import java.io.BufferedReader;
import java.io.FileReader;
import java.io.IOException;
import java.util.ArrayList;
import java.util.List;

public class Csv_reader {

    private String path;
    private List<List<String>> table = new ArrayList<List<String>>();

    public List<List<String>> get_csv() throws IOException {
        String row = "";
        String spliter = ",";

        BufferedReader csvReader = new BufferedReader(new FileReader(this.path));
        while((row = csvReader.readLine()) != null) {
            List<String> aux = new ArrayList<String>();
            String[] parts = row.split(spliter);
            for(int i = 0;i < parts.length;i++) {
                aux.add(parts[i]);
            }
            table.add(aux);
        }
        csvReader.close();
        return table;
    }

    public void set_path(String path) {
        this.path = path;
    }

    public String get_path() {
        return this.path;
    }
}

