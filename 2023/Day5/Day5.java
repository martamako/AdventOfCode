package year2023.Day5;

import java.io.IOException;
import java.nio.file.Files;
import java.nio.file.Path;
import java.nio.file.Paths;
import java.util.*;

public class Day5 {
    public static void main(String[] args) throws IOException {
        Path path = Paths.get("src/year2023/Day5/input2.txt");
        List<String> lines = Files.readAllLines(path);

        List<Integer> seeds = new ArrayList<>();
        HashMap<Integer, Integer> seedToSoil = new HashMap<>();
        HashMap<Integer, Integer> soilToFertilizer = new HashMap<>();
        HashMap<Integer, Integer> fertilizerToWater = new HashMap<>();
        HashMap<Integer, Integer> waterToLight = new HashMap<>();
        HashMap<Integer, Integer> lightToTemperature = new HashMap<>();
        HashMap<Integer, Integer> temperatureToHumidity = new HashMap<>();
        HashMap<Integer, Integer> humidityToLocation = new HashMap<>();

        int index = 0;
        while (index < lines.size()){
            String line = lines.get(index);
            if (line.isEmpty()){
                index++;
                continue;
            }

            if (line.contains("seeds")){
                String[] parts = line.strip().split(": ");
                int[] numbers = Arrays.stream(parts[1].split(" ")).mapToInt(Integer::parseInt).toArray();
                System.out.println(Arrays.toString(numbers));
            }
            if (line.contains("seed-to-soil")){
                getMap(lines, index, seedToSoil);
                index += seedToSoil.size();
            } else if (line.contains("soil-to-fertilizer")){
                getMap(lines, index, soilToFertilizer);
                index += soilToFertilizer.size();
            } else if (line.contains("fertilizer-to-water")){
                getMap(lines, index, fertilizerToWater);
                index += fertilizerToWater.size();
            } else if (line.contains("water-to-light")){
                getMap(lines, index, waterToLight);
                index += waterToLight.size();
            } else if (line.contains("light-to-temperature")){
                getMap(lines, index, lightToTemperature);
                index += lightToTemperature.size();
            } else if (line.contains("temperature-to-humidity")){
                getMap(lines, index, temperatureToHumidity);
                index += temperatureToHumidity.size();
            } else if (line.contains("humidity-to-location")){
                getMap(lines, index, humidityToLocation);
                index += humidityToLocation.size();
            }

            index++;
//            System.out.println(line);
        }
    }

    static void getMap(List<String> lines, int index, HashMap<Integer, Integer> map){
        index++;

        while (true){
            String line = lines.get(index);
            if (line.isEmpty()) {
                break;
            }
            int[] numbers = Arrays.stream(line.split(" ")).mapToInt(Integer::parseInt).toArray();
            map.put(numbers[0], numbers[1]);
            index++;
            if (index >= lines.size()){
                break;
            }
        }
    }
}
