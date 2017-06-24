public class Main {
    public static void main(String[] args) {

        int[] x = {1,2,3,4};

        String myString = "This is a string";
        int myInt = 10;
        float myFloat = 49.3f;
        char myChar = 'C';

        System.out.format("%s%n", myString);
        System.out.format("%d%n", myInt);
        System.out.format("%f%n", myFloat);
        System.out.format("%c%n", myChar);


        System.out.format("%.2f%n", myFloat);  /* 2 Decimal Places */
        
    }
}