// Homework Assignment
// Dynamic programming 

#include <iostream> 
#include <cstdlib>
using namespace std; 

#include <bits/stdc++.h> 

using namespace std; 
#define INF INT_MAX  
  
// A utility function to print the solution  
int printSolution (int p[], int n);  

// GLobal variables to store number of lines and margin cost
int nl;
int cost;

// justify text in pretty printing  
void justify (int l[], int n, int M)  
{  
    // margin spaces
    int extras[n+1][n+1];  
  
    // cost of the marging
    int lc[n+1][n+1];  
    int c[n+1];  
  
    // indexes of words on lines
    int p[n+1];  
  
    int i, j;  
  
    for (i = 1; i <= n; i++)  
    {  
        extras[i][i] = M - l[i-1];  
        for (j = i+1; j <= n; j++)  
            extras[i][j] = extras[i][j-1] - l[j-1] - 1;  
    }  

    for (i = 1; i <= n; i++)  
    {  
        for (j = i; j <= n; j++)  
        {  
            if (extras[i][j] < 0)  
                lc[i][j] = INF;  
            else
                lc[i][j] = extras[i][j]*extras[i][j];  
        }  
    }  
  
    // COmpute cost of optimum margin
    c[0] = 0;  
    for (j = 1; j <= n; j++)  
    {  
        c[j] = INF;  
        for (i = 1; i <= j; i++)  
        {  
            if (c[i-1] != INF && lc[i][j] != INF &&  
                           (c[i-1] + lc[i][j] < c[j]))  
            {  
                c[j] = c[i-1] + lc[i][j];  
                p[j] = i;  
            }  
        }  
    }  
  
    nl = printSolution(p, n);
    //for( int k = 0; k <= n; k++){
    //    cout<<"k"<< k << endl;
    //    cout << " " << c[k];
    //}
    cost = c[n];
    
}  
  
int printSolution (int p[], int n)  
{  
    int k;  
    if (p[n] == 1)  
        k = 1;  
    else
        k = printSolution (p, p[n]-1) + 1;  
    //cout<<"Line number "<<k<<": From word no. "<<p[n]<<" to "<<n<<endl;  
    return k;  
}  

int main() 
{ 
    int n; 
    int l;
    string w;
  
    cin >> n >> l;
    int lword[n];
    
    for (int i=0; i<n; i++) 
    { 
        cin >> w; 
        lword[i] = w.length();
    } 
    
    justify (lword, n, l);  
    cout<< cost << " "<<nl;
    return 0; 
} 
