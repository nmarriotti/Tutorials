public class CheckingAccount extends Account {

    public CheckingAccount(long amount) {
        super("Checking", amount);
    }
    void withdraw(long amount) {
        setAmount(getAmount() - amount);
    }
}