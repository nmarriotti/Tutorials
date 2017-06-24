import java.util.ArrayList;
public class Main {
    public static void main(String[] args) {
        
        int size; /* Will store size of list */

        //Create an ArrayList of string values 
        ArrayList<String> MyList = new ArrayList<String>();  

        // Add values to the List
        MyList.add("Orange");
        MyList.add("Blue");
        MyList.add("Purple");

        // Remove item from list
        MyList.remove("Purple");

        // Set our list size
        size = MyList.size();

        // Get value from list
        System.out.println("Value at index 0 is: " + MyList.get(0));

        // Print out the list size
        System.out.println("List size: " + size);

        // Print everything in our list
        for(String item : MyList) {
            System.out.println(item);
        }
    }
}