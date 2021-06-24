import java.util.*;
import java.io.*;
import java.math.*;

public class Slic{
	
	static ArrayList<pair> primeFactors(int n){
		ArrayList<pair> li = new ArrayList<>();
		int cnt = 0;
		while(n % 2 == 0){
			++cnt;
			n /= 2;
		}

		if(cnt != 0){
			li.add(pair.from(2 , cnt));
			cnt = 0;
		}

		int lt = (int)Math.sqrt(n);
		for(int i = 3; i <= lt; i++){
			if(n % i != 0)
				continue;
			while(n % i == 0){
				++cnt;
				n /= i;
			}
			li.add(pair.from(i, cnt));
			cnt = 0;
		}

		if(n > 2)
			li.add(pair.from(n , 1));
		return li;
	} 

	static int nxtPow2(int n){
		if(n == 1)
			return 1;

		int cnt = 0, val = 1;
		while(val < n){
			val *= 2;
			++cnt;
		}
		return cnt;
	}

	static boolean isPowerOf2(int n){
		if(n == 1)
			return false;
		int val = 1;
		while(val < n)
			val *= 2;
		return val == n;
	}

	public static void process(int testNumber){
		int n = ni();
		ArrayList<pair> li = primeFactors(n);
		int val = 1, steps = 0, prev = -1;
		boolean flag = true, allEqual = true;

		for(pair x : li){
			val *= x.first;
			flag = flag && isPowerOf2(x.second);
			steps = Math.max(steps, nxtPow2(x.second));
			if(prev != -1)
				allEqual = allEqual && (prev == x.second);
			prev = x.second;
		}
		
		if(val == n)
			steps = 0;
		else if(!flag || !allEqual)
			++steps;

		pn(val + " " + steps);
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

    @Override
    public String toString(){
    	return this.first + " " + this.second;
    }

    static public pair from(int f, int s){
        return new pair(f, s);
    }
}
