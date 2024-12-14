package year2023.Day3;

import java.io.File;
import java.util.ArrayList;
import java.util.List;
import java.util.Scanner;
import java.util.regex.Matcher;
import java.util.regex.Pattern;

public class Day3 {
    static String filePath = "src/year2023/Day3/input.txt";
    static int size;
    private static final List<int[]> dir = new ArrayList<>(List.of(
            new int[]{1, 1},
            new int[]{1, 0},
            new int[]{1, -1},
            new int[]{0, -1},
            new int[]{-1, -1},
            new int[]{-1, 0},
            new int[]{-1, 1},
            new int[]{0, 1}));

    public static void main(String[] args) {
        char[][] map;
        ArrayList<Number> numbers = new ArrayList<>();
        try (Scanner fileScanner = new Scanner(new File(filePath))){
            String firstLine = fileScanner.nextLine().strip();
            size = firstLine.length();
            map = new char[size][];
            map[0] = firstLine.toCharArray();
            int index = 1;
            while(fileScanner.hasNextLine()) {
                String line = fileScanner.nextLine();
                map[index] = line.toCharArray();
                index++;
            }
            getNumbers(map, numbers);
            System.out.println(addNumbers(numbers, map));
            System.out.println(getGearsRatio(numbers, map));
        } catch(Exception e){
            System.out.println("No such file " + e.getMessage());
        }
    }

    static int addNumbers(ArrayList<Number> numbers, char[][] map) {
        int sum = 0;
        for(Number number: numbers){
            if(isNumberValid(map, number)){
                System.out.println(number);
                sum += Integer.parseInt(number.getValue());
            }
        }
        return sum;
    }

    static void getNumbers(char[][] map, ArrayList<Number> numbers){
        Pattern pattern = Pattern.compile("([0-9]+)");
        for(int i=0; i<map.length; i++){
            String newString = new String(map[i]);
            int index = 0;
            int newIndex = 0;
            while(index < size){
                newString = newString.substring(newIndex);
                Matcher m = pattern.matcher(newString);
                if(!m.find()) {
                    break;
                }
                String found = m.group();
                newIndex = newString.indexOf(found);
                index += newIndex;
                numbers.add(new Number(found, index, i));
                newIndex += found.length();
                index += found.length();
            }
        }
    }

    static boolean isNumberValid(char[][] map, Number number){
        for(int i=number.getX(); i<number.getX() + number.getValue().length(); i++){
            for(int[] direction: dir){
                if(isInBound(direction, i, number.getY())){
                    char ch = map[number.getY() + direction[1]][i + direction[0]];
                    if(isSymbol(ch)){
                        return true;
                    }
                }
            }
        }
        return false;
    }

    static int getGearsRatio(ArrayList<Number> numbers, char[][] map){
        int ratio = 0;
        for(int i=0; i<size; i++){
            for(int j=0; j<size; j++){
                if(map[i][j] == '*'){
                    ArrayList<Integer> nums = getGearsNumbers(numbers, map, j, i);
                    if(nums.size() == 2){
                        ratio += nums.get(0) * nums.get(1);
                    }
                }
            }
        }
        return ratio;
    }

    static ArrayList<Integer> getGearsNumbers(ArrayList<Number> numbers, char[][] map, int x, int y){
        ArrayList<Integer> nums = new ArrayList<>();
        for(int[] direction: dir){
            if(isInBound(direction, x, y)){
                char ch = map[y + direction[1]][x + direction[0]];
                if(Character.isDigit(ch)){
                    for(Number number: numbers){
                        if(number.isNumbersCoordinate(x + direction[0], y + direction[1])){
                            if(!nums.contains(Integer.parseInt(number.getValue()))){
                                nums.add(Integer.parseInt(number.getValue()));
                            }
                            break;
                        }
                    }
                }
            }
        }
        return nums;
    }


    static boolean isInBound(int[] direction, int x, int y){
        return direction[0] + x >= 0 && direction[0] + x < size
                && direction[1] + y >= 0 && direction[1] + y < size;
    }

    static boolean isSymbol(char ch){
        return !Character.isDigit(ch) && ch != '.';
    }
}
