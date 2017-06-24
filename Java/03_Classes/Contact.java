public class Contact {
    
    String name;

    public Contact(String name) {
        System.out.println("Object created!");
        setName(name);
    }

    public void setName(String name) {
        this.name = name;
    }

    public void getName() {
        System.out.println(this.name);
    }
}