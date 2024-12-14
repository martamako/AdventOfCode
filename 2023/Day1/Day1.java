package year2023.Day1;

import java.io.File;
import java.util.*;
import java.util.stream.Collectors;
import java.util.stream.Stream;

public class Day1 {
    static String filePath = "src/year2023/Day1/input.txt";
    public static void main(String[] args) {
        part1();
        part2();
    }

    public static void part1(){
        try (Scanner fileScanner = new Scanner(new File(filePath))) {
            int sum = 0;
            while (fileScanner.hasNextLine()) {
                int first = 0, last = 0;
                String line = fileScanner.nextLine();
                for (char letter: line.toCharArray()) {
                    if (letter >= '0' && letter <= '9'){
                        first = (int) letter - 48;
                        break;
                    }
                }

                for (int i=line.length() - 1; i >= 0; i--) {
                    char letter = line.toCharArray()[i];
                    if (letter >= '0' && letter <= '9'){
                        last = (int) letter - 48;
                        break;
                    }
                }
                sum += first * 10 + last;
            }
            System.out.println(sum);
        } catch (Exception e) {
            System.out.println("Couldn't open " + e.getMessage());
        }
    }

    public static void part2() {
        Map<String, Integer> numbers = Stream.of(new Object[][] {
                { "one", 1 }, { "two", 2 }, { "three", 3 }, { "four", 4 }, { "five", 5 }, { "six", 6 },
                { "seven", 7 }, { "eight", 8 }, { "nine", 9 }, { "zero", 0 },
        }).collect(Collectors.toMap(data -> (String) data[0], data -> (Integer) data[1]));
        try (Scanner fileScanner = new Scanner(new File(filePath))) {
            int sum = 0;

            while (fileScanner.hasNextLine()) {
                String line = fileScanner.nextLine();
                TreeMap<Integer, Integer> wordNumbers = new TreeMap<>();
                for (String number: numbers.keySet()) {
                    int index = line.indexOf(number);
                    while (index >= 0) {
                        wordNumbers.put(index, numbers.get(number));
                        index = line.indexOf(number, index + 1);
                    }
                }
                for (int i=0; i<line.length(); i++) {
                    char letter = line.toCharArray()[i];
                    if (letter >= '0' && letter <= '9'){
                        int num = (int) letter - 48;
                        wordNumbers.put(i, num);
                    }
                }

                sum += wordNumbers.firstEntry().getValue() * 10 + wordNumbers.lastEntry().getValue();
            }
            System.out.println(sum);
        } catch (Exception e) {
            System.out.println("Couldn't open " + e.getMessage());
        }
    }
}
