//week-3
import java.util.*;

public class Lexer {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        System.out.println("Enter source code:");
        String s = sc.nextLine();

        String[] keywords = {
            "int", "float", "char", "double",
            "if", "else", "for", "while", "return"
        };

        String[] tokens = s.split("\\s+");

        for (String token : tokens) {
            boolean keyword = false;

            for (String k : keywords) {
                if (token.equals(k)) {
                    keyword = true;
                    break;
                }
            }

            if (keyword)
                System.out.println(token + " -> KEYWORD");
            else if (token.matches("[a-zA-Z_][a-zA-Z0-9_]*"))
                System.out.println(token + " -> IDENTIFIER");
            else if (token.matches("[0-9]+"))
                System.out.println(token + " -> NUMBER");
            else if (token.matches("[+\\-*/=]"))
                System.out.println(token + " -> OPERATOR");
            else
                System.out.println(token + " -> SYMBOL");
        }

        sc.close();
    }
}