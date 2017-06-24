public class Main {
    public static void main(String[] args) {
        CheckingAccount a = new CheckingAccount(495);
        System.out.println("Name: " + a.getName() );
        System.out.println("Amount: " + a.getAmount() );
        a.withdraw(150);
        System.out.println("Amount: " + a.getAmount() );
    }
}