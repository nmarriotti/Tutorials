public class Substring {
    public static void main(String[] args) {
        String filename = "AA.HOWNOWBROWNCOW_26JAN2018-0651PM.txt";

        System.out.println("Original Filename: " + filename);

        System.out.println(filename.substring(3, 6));

        String test = "THAT TREE IS HUGE.";
        System.out.println(test.substring(5, 9));
    }
}