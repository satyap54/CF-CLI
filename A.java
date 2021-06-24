import java.util.*;
import java.io.*;
import java.math.*;

public class A{
	 
	public static void process(int testNumber){
		int n = ni(), a = ni(), b = ni();
		char arr[] = (" " + nln()).toCharArray();
		pn((arr[a] == arr[b]) ? "0" : "1");	
	}
 
	static final long mod = (long)1e9+7l;
	static boolean DEBUG = true;
	static FastReader sc;
	static PrintWriter out = new PrintWriter(System.out);
	public static void main(String[]args){
		sc = new FastReader();
 
		long s = System.currentTimeMillis();
		int t = 1;
		// t = ni();
		for(int i = 1; i <= t; i++)
			process(i);
 
		out.flush();
		System.err.println(System.currentTimeMillis()-s+"ms");
	}

	static void trace(Object... o){ if(!DEBUG) return; System.err.println(Arrays.deepToString(o)); };    
	static void pn(Object o){ out.println(o); }
	static void p(Object o){ out.print(o); }
	static int ni(){ return Integer.parseInt(sc.next()); }
	static long nl(){ return Long.parseLong(sc.next()); }
	static double nd(){ return Double.parseDouble(sc.next()); }
	static String nln(){ return sc.nextLine(); }
	static long gcd(long a, long b){ return (b==0)?a:gcd(b,a%b);}
	static int gcd(int a, int b){ return (b==0)?a:gcd(b,a%b); }
	
	static class FastReader{ 
		BufferedReader br; 
		StringTokenizer st; 
  
		public FastReader(){ 
			br = new BufferedReader(new InputStreamReader(System.in)); 
		} 
  
		String next(){ 
			while (st == null || !st.hasMoreElements()){ 
				try{ st = new StringTokenizer(br.readLine()); } catch (IOException  e){ e.printStackTrace(); } 
			} 
			return st.nextToken(); 
		} 
  
		String nextLine(){ 
			String str = ""; 
			try{ str = br.readLine(); } catch (IOException e) { e.printStackTrace(); } 
			return str; 
		} 
	} 
}

class pair implements Comparable<pair> {
    int first, second;
    public pair(int first, int second){
        this.first = first;
        this.second = second;
    }

    @Override
    public int compareTo(pair ob){
        if(this.first != ob.first)
            return this.first - ob.first;
        return this.second - ob.second;
    }

    static public pair from(int f, int s){
        return new pair(f, s);
    }
}