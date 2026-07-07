package coding_exercise;

import com.opencsv.CSVReader;

import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.List;

public class JavaDataPipeline {

    public static void main(String[] args) throws Exception {

        // http://opencsv.sourceforge.net/
        final CSVReader reader = new CSVReader(new InputStreamReader(JavaDataPipeline.class.getClassLoader().getResourceAsStream("file1.csv")));
        final List<String[]> myEntries = reader.readAll();

        for (int i = 0; i < 10; i++) {
            System.out.println(Arrays.toString(myEntries.get(i)));
        }

        //TODO - Goal 1



        //TODO - Goal 2



        //TODO - Goal3



    }
}
