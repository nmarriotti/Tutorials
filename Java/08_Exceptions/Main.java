public class Main {
    public static void main(String[] args) {
        try {
            int x = 1/0;
            System.out.println(x);
        } 
        catch (ArithmeticException e) {
            System.out.println("Error: " + e);
        }

        System.out.println("Hi there!");

    }
}