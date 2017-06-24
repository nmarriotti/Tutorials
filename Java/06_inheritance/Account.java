public class Account {

    private String name;
    private long amount;

    public Account(String name, long amount) {
        this.name = name;
        this.amount = amount;
        this.setAmount(amount);
    }

    void deposit(long amount) {
        this.amount += amount;
    }

    void setAmount(long amount) {
        this.amount = amount;
    }
    
    String getName() {
        return name;
    }

    long getAmount() {
        return amount;
    }

}