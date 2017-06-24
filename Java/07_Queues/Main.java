import java.util.Queue;
import java.util.LinkedList;
public class Main {
    public static void main(String[] args) {
        Queue<String> q = new LinkedList<String>();

        q.add("job1");
        q.add("job2");
        q.add("job3");

        String s = q.peek();
        System.out.println("The first value using peek() is: " + s);

        System.out.println("The size is: " + q.size());

        s = q.element();
        System.out.println("The first value using element() is: " + s);

        s = q.remove();
        System.out.println("The first value using remove() is: " + s);
        System.out.println("The size is: " + q.size());

        s = q.poll();
        System.out.println("The first value using poll() is: " + s);
        System.out.println("The size is: " + q.size());


    }
}