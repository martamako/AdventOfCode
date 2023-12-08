package year2023.Day4;

import java.io.IOException;
import java.nio.file.Files;
import java.nio.file.Path;
import java.nio.file.Paths;
import java.util.Arrays;
import java.util.List;
import java.util.stream.IntStream;

public class Day4 {
    static Path path = Paths.get("src/year2023/Day4/input.txt");
    public static void main(String[] args) throws IOException {
        List<String> read = Files.readAllLines(path);
        int sum = 0;
        for(String line: read){
            line = line.replaceAll("[ ]+", " ").strip();

            String[] parts = line.split(": ");
            parts = parts[1].split(" [|] ");
            String[] part1 = parts[0].split(" ");

            int[] winningNumbers = Arrays.stream(part1).mapToInt(Integer::parseInt).toArray();
            Integer[] what = Arrays.stream( winningNumbers ).boxed().toArray( Integer[]::new );
            String[] part2 = parts[1].split(" ");

            int[] myNumbers = Arrays.stream(part2).mapToInt(Integer::parseInt).toArray();
            Integer[] ever = IntStream.of( myNumbers ).boxed().toArray( Integer[]::new );
            Integer[] intersection = Arrays.stream(ever)
                    .distinct()
                    .filter(x -> Arrays.asList(what).contains(x))
                    .toArray(Integer[]::new);

            sum += (int) Math.pow(2.0, intersection.length - 1);
        }
        System.out.println(sum);
    }
}
