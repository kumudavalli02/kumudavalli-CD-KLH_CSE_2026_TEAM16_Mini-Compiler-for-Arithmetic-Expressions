import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        String[] keywords = {
            "int", "float", "char", "if", "else",
            "while", "for", "return", "void"
        };

        System.out.println("Enter input:");
        String input = sc.nextLine();
        String[] words = input.split("\\s+");

        for (String word : words) {
            boolean found = false;

            for (String key : keywords) {
                if (word.equals(key)) {
                    System.out.println("Keyword: " + word);
                    found = true;
                    break;
                }
            }

            if (!found && word.matches("[a-zA-Z_][a-zA-Z0-9_]*"))
                System.out.println("Identifier: " + word);
            else if (word.matches("[0-9]+"))
                System.out.println("Number: " + word);
        }

        sc.close();
    }
}