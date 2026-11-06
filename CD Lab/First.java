//week-5
//commands 
//javac First.java
//java First
import java.util.*;
public class First {
 static Map<String, String[]> g = new HashMap<>();
 static Set<String> first(String x) {
 Set<String> f = new LinkedHashSet<>();
 if (!g.containsKey(x)) f.add(x);
 else for (String p : g.get(x)) {
 String s = p.substring(0,1);
 f.addAll(first(s));
 }
 return f;
 }
 public static void main(String[] a) {
 Scanner sc = new Scanner(System.in);
 System.out.println("Enter no. of productions:");
 int n = sc.nextInt(); sc.nextLine();
 for (int i=0;i<n;i++){
 String[] in = sc.nextLine().split("->");
 g.put(in[0], in[1].split("\\|"));
 }
 for (String nt : g.keySet())
 System.out.println("FIRST(" + nt + ") = " + first(nt));
 sc.close();
 }
}
