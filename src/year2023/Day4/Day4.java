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
        int power = 0;
        int index = 0;
        for(String line: read){
            Integer[] intersection = getIntersection(line);
            sum += (int) Math.pow(2.0, intersection.length - 1);
            power += getNumberOfCard(read, index) + 1;
            index++;
        }
        System.out.println(sum);
        System.out.println(power);
    }

    static int getNumberOfCard(List<String> lines, int number){
        if(number >= lines.size()){
            return 0;
        }
        int sum = 0;
        String line = lines.get(number);
        Integer[] intersection = getIntersection(line);
        for(int i=number+1; i <= number + intersection.length; i++){
             sum += getNumberOfCard(lines, i) + 1;
        }
        return sum;
    }

    static Integer[] getIntersection(String line){
        line = line.replaceAll("[ ]+", " ").strip();
        String[] parts = line.split(": ");
        parts = parts[1].split(" [|] ");
        String[] part1 = parts[0].split(" ");

        int[] winningNumbers = Arrays.stream(part1).mapToInt(Integer::parseInt).toArray();
        Integer[] what = Arrays.stream( winningNumbers ).boxed().toArray( Integer[]::new );
        String[] part2 = parts[1].split(" ");

        int[] myNumbers = Arrays.stream(part2).mapToInt(Integer::parseInt).toArray();
        Integer[] ever = IntStream.of( myNumbers ).boxed().toArray( Integer[]::new );

        return Arrays.stream(ever)
                .distinct()
                .filter(x -> Arrays.asList(what).contains(x))
                .toArray(Integer[]::new);
    }
}
