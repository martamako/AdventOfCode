package year2023.Day2;

public class Tuple<K, V> {
    private final K number;
    private final V color;

    public Tuple(K first, V second){
        this.number = first;
        this.color = second;
    }

    public K getNumber() {
        return number;
    }

    public V getColor(){
        return color;
    }

    @Override
    public String toString() {
        return "Tuple{" +
                "number of cubes=" + number +
                ", color=" + color +
                '}';
    }
}
