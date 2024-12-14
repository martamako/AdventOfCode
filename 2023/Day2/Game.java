package year2023.Day2;

import java.util.ArrayList;
import java.util.Objects;

public class Game {
    private final int ID;
    private final ArrayList<ArrayList<Tuple<Integer, String>>> records;

    public Game(int ID) {
        this.ID = ID;
        records = new ArrayList<>();
    }

    public int getID() {
        return ID;
    }

    public void addRecord(String info){
        String[] parts = info.split(", ");
        ArrayList<Tuple<Integer, String>> record = new ArrayList<>();
        for (String part: parts) {
            addCube(part, record);
        }
        records.add(record);
    }

    public void addCube(String info, ArrayList<Tuple<Integer, String>> record) {
        String[] parts = info.split(" ");
        record.add(new Tuple<>(Integer.valueOf(parts[0]), parts[1]));
    }

    public boolean isGamePossible() {
        for (ArrayList<Tuple<Integer, String>> record: records) {
            if (!isRecordValid(record)) {
                return false;
            }
        }
        return true;
    }

    public boolean isRecordValid(ArrayList<Tuple<Integer, String>> record){
        for (Tuple<Integer, String> tuple: record) {
            int maxRed = 12;
            if (Objects.equals(tuple.getColor(), "red") && tuple.getNumber() > maxRed) {
                return false;
            }
            int maxGreen = 13;
            if (Objects.equals(tuple.getColor(), "green") && tuple.getNumber() > maxGreen) {
                return false;
            }
            int maxBlue = 14;
            if (Objects.equals(tuple.getColor(), "blue") && tuple.getNumber() > maxBlue) {
                return false;
            }
        }
        return true;
    }

    public int powerOfCubes(){
        int maxRed = maximumColor("red"), maxGreen = maximumColor("green"), maxBlue = maximumColor("blue");
        return maxRed * maxGreen * maxBlue;
    }

    public int maximumColor(String color) {
        int maxColor = 0;
        for(ArrayList<Tuple<Integer, String>> record: records){
            for(Tuple<Integer, String> tuple : record){
                if(tuple.getColor().equals(color)){
                    if(tuple.getNumber() > maxColor){
                        maxColor = tuple.getNumber();
                    }
                }
            }
        }
        return maxColor;
    }

    @Override
    public String toString() {
        return "Game{" +
                "ID=" + ID +
                ", records=" + records +
                '}';
    }
}
