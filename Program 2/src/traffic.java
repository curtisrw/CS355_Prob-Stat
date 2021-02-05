import java.util.Random;

// Program to calculate traffic flow through a maze of cities

import java.io.* ;

public class traffic {

	/**
	 * @param args
	 */
	 
	static Random rand = new Random();

	static int cities[] = {'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P'} ;
	static int CityCount = 16 ;
	
// Map of probabilities of destinations leaving a city
// A huge flaw in this program is that it never checks for the rows adding up to 1.0
// Another flaw is that it really should take this map and the time map and construct an object
//   with travel information for the cities instead of using this Fortran approach
	 
	static double[][] prob = {
//  A   B   C   D   E   F   G   H   I   J   K   L   M   N   O   P
 {  0, .4, .6,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0}, //A
 {  0,  0,  0, .4, .6,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0}, //B
 {  0,  0,  0,  0, .5, .5,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0}, //C
 {  0,  0,  0,  0,  0,  0, .4, .6,  0,  0,  0,  0,  0,  0,  0,  0}, //D
 {  0,  0,  0,  0,  0,  0,  0, .6, .4,  0,  0,  0,  0,  0,  0,  0}, //E
 {  0,  0,  0,  0,  0,  0,  0,  0, .6, .4,  0,  0,  0,  0,  0,  0}, //F
 {  0,  0,  0,  0,  0,  0,  0,  0,  0,  0, .6, .4, 0,  0,  0,  0}, //G
 {  0,  0,  0,  0,  0,  0,  0,  0,  0,  0, .4, .3, .3,  0,  0,  0}, //H
 {  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0, .5, .5,  0,  0,  0}, //I
 {  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0, 1.,  0,  0,  0}, //J
 {  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0, 1.,  0,  0}, //K
 {  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0, .4, .6,  0}, //L
 {  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0, 1.,  0}, //M
 {  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0, 1.}, //N
 {  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0, 1.}, //O
 {  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0}  //P
} ;
 
// Transit times from city x to city y
 
	static int[][] times = {
// A  B  C  D  E  F  G  H  I  J  K  L  M  N  O  P
 { 0, 5, 6, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0}, //A
 { 0, 0, 0, 4, 7, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0}, //B
 { 0, 0, 0, 0, 4, 6, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0}, //C
 { 0, 0, 0, 0, 0, 0, 4, 6, 0, 0, 0, 0, 0, 0, 0, 0}, //D
 { 0, 0, 0, 0, 0, 0, 0, 6, 4, 0, 0, 0, 0, 0, 0, 0}, //E
 { 0, 0, 0, 0, 0, 0, 0, 0, 4, 7, 0, 0, 0, 0, 0, 0}, //F
 { 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 4, 6, 0, 0, 0, 0}, //G
 { 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 4, 8, 8, 0, 0, 0}, //H
 { 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 6, 4, 0, 0, 0}, //I
 { 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 5, 0, 0, 0}, //J
 { 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 4, 0, 0}, //K
 { 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 5, 6, 0}, //L
 { 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 5, 0}, //M
 { 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 5}, //N
 { 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 5}, //O
 { 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0}  //P
 
	} ;
	
static int count =1000, time=0, timesq=0, totaltime=0, totaltimesq=0 ;
static int start = 0, endNode = 15 ;
	
// Given a city (the integer value thisNode), return the next city randomly according to the 
// probabilities given
 
static int nextCity(int thisNode) {
	double r = rand.nextDouble() ;
	double p = 0.0 ;
	
	for (int j=0 ; j<CityCount; j++ ) {
		p += prob[thisNode][j] ;
		if (r  < p) {
			//System.out.printf("%c ", cities[j]) ;
			return(j) ;
		}
	}
	System.out.printf("B Node is %c\n", cities[endNode]) ;
	return endNode ;
}	
	
	public static void main(String[] args) {
		// TODO Auto-generated method stub


		for (int i=0 ; i< count ; i++) {
			time = 0 ; 
			timesq = 0 ;
					
			// Generate one traversal of the network
			int newNode ;
			for (int node = start ; ; ) {
				newNode = nextCity(node) ;
				time += times[node][newNode] ;
				timesq += times[node][newNode]*times[node][newNode] ;
				totaltime += times[node][newNode] ;
				totaltimesq += times[node][newNode]*times[node][newNode] ;
				node = newNode ;
				if (node == endNode) break ;
			}
			
			// traversed one time
		}
		// finished all traversals
			double ftime = totaltime, ftimesquared = totaltimesq, fcount=count, Etime, Etimesq ;
			
			Etime = ftime/fcount ;
			Etimesq = ftimesquared/fcount ;
		
			System.out.printf("Average time = %5.1f Std dev = %f\n", Etime , Math.sqrt(Etimesq - Etime)) ;
	}
}
