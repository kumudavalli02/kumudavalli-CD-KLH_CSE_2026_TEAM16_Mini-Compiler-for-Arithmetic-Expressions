//week1

import java.util.Scanner;
public class Removespace {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        System.out.println("Enter source code:");
        String s = sc.nextLine();

        s = s.replaceAll("//.*", "");
        s = s.replaceAll("/\\*.*?\\*/", "");
        s = s.replaceAll("\\s+", "");

        System.out.println("After removing spaces and comments:");
        System.out.println(s);
    }
}/