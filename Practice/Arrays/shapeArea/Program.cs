using System;
using System.Collections;

namespace shapeArea
{
    class Program
    {
        static void Main(string[] args)
        {
            Console.WriteLine(shape(5));
            //return shape(1);
            
        }

        public static int shape (int n){
            return n*n + (n-1)*(n-1);
        }
        // 1 : 1 
        // 2 : 5  +4  2*2+1
        // 3 : 13 +8  3*3
        // 4 : 25 +12 4*4+3^2 
    }
}

