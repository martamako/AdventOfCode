package year2023.Day2;

import java.io.File;
import java.util.ArrayList;
import java.util.Scanner;

public class Day2 {
    static String filePath = "src/year2023/Day2/input.txt";
    public static void main(String[] args) {
        try (Scanner fileScanner = new Scanner(new File(filePath))){
            ArrayList<Game> games = new ArrayList<>();
            while(fileScanner.hasNextLine()) {
                String line = fileScanner.nextLine();
                processInfo(line, games);
            }
            System.out.println(countGames(games)); //Part 1
            System.out.println(powerGames(games)); //Part 2
        } catch(Exception e){
            System.out.println("No such file " + e.getMessage());
        }
    }

    public static void processInfo(String line, ArrayList<Game> games) {
        String[] parts = line.split(": ");
        String[] gameInfo = parts[0].split(" ");
        Game game = new Game(Integer.parseInt(gameInfo[1]));
        parts = parts[1].split("; ");
        for (String part: parts) {
            game.addRecord(part);
        }
        games.add(game);
    }

    public static int countGames(ArrayList<Game> games){
        int sum = 0;
        for (Game game: games) {
            if(game.isGamePossible()) {
                sum += game.getID();
            }
        }
        return sum;
    }

    public static int powerGames(ArrayList<Game> games){
        int power = 0;
        for(Game game: games){
            power += game.powerOfCubes();
        }
        return power;
    }
}
