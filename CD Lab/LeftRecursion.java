//week-4
//commands
//javac LeftRecursion.java
//java LeftRecursion
import java.util.*;
public class LeftRecursion {
 public static void main(String[] args) {
 Scanner sc = new Scanner(System.in);
 System.out.println("Enter production (e.g. A->Aa|b):");
 String s = sc.nextLine();
 sc.close();
 String nt = s.split("->")[0];
 String[] prods = s.split("->")[1].split("\\|");
 List<String> alpha = new ArrayList<>(), beta = new ArrayList<>();
 for (String p : prods)
 if 
 (p.startsWith(nt)) alpha.add(p.substring(nt.length()));
 else 
 beta.add(p);
 if 
 (alpha.isEmpty()) System.out.println("No left recursion");
 else {
 String nt1 = nt + "'";
 System.out.print(nt + "->");
 for (int i = 0; i < beta.size(); i++)
 System.out.print(beta.get(i) + nt1 + (i < beta.size()-1 ? "|" : ""));
 System.out.print("\n" + nt1 + "->");
 for (int i = 0; i < alpha.size(); i++)
 System.out.print(alpha.get(i) + nt1 + "|");
 System.out.println("ε");
 }
 }
}
