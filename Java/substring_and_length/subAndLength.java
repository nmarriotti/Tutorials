public class subAndLength {
    public static void main(String[] args) {
        String filename = "01test_file.txt";
        String file1, file2, extension;

        file1 = filename.replace(filename.substring(2, filename.length()), "_example.doc");
        System.out.println(file1);

        file2 = filename.replace(filename.substring(2, filename.indexOf(".")), "_myfile");
        System.out.println(file2);

        extension = filename.substring(filename.indexOf("."), filename.length());
        System.out.println(extension);
    }    
}
