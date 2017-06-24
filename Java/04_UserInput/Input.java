import java.util.Scanner;

public class Input {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        
        String name;
        
        System.out.print("Enter your name: ");
        name = scanner.next();

        System.out.println("You entered: " + name);  
    }
}