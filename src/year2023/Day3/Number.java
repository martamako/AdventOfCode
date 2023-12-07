package year2023.Day3;

public class Number {
    private final String value;
    private final int x;
    private final int y;



    public String getValue() {
        return value;
    }

    public int getX() {
        return x;
    }

    public int getY() {
        return y;
    }

    public Number(String value, int x, int y) {
        this.value = value;
        this.x = x;
        this.y = y;
    }

    public boolean isNumbersCoordinate(int x, int y){
        if(this.y == y){
            return this.x <= x && x < this.x + this.value.length();
        }
        return false;
    }

    @Override
    public String toString() {
        return "Number{" +
                "value=" + value +
                ", x=" + x +
                ", y=" + y +
                '}';
    }
}
