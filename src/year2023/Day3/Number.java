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

    @Override
    public String toString() {
        return "Number{" +
                "value=" + value +
                ", x=" + x +
                ", y=" + y +
                '}';
    }
}
