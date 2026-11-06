// week-6
//commands
//javac Follow.java 
//java Follow
import java.util.*;
public class Follow {
 static Map<String,String[]> g=new HashMap<>();
 static Map<String,Set<String>> f=new HashMap<>();
 static String start;
 public static void main(String[] a){
 Scanner sc=new Scanner(System.in);
 System.out.println("Enter no. of productions:");
 int n=sc.nextInt(); sc.nextLine();
 for(int i=0;i<n;i++){
 String[] in=sc.nextLine().split("->");
 if(i==0) start=in[0];
 g.put(in[0],in[1].split("\\|"));
 f.put(in[0],new LinkedHashSet<>());
 }
 f.get(start).add("$"); // start symbol
 for(String A:g.keySet())
 for(String p:g.get(A))
 for(int i=0;i<p.length()-1;i++){
 String B=p.charAt(i)+"", next=p.charAt(i+1)+"";
 if(g.containsKey(B))
 if(g.containsKey(next)) f.get(B).add(next);
 else f.get(B).add(next);
 }
 for(String nt:f.keySet())
 System.out.println("FOLLOW("+nt+")="+f.get(nt));
 sc.close(); } }