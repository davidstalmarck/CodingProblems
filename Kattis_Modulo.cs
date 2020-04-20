// you can find the problem here https://open.kattis.com/problems/modulo
//  written by David Stålmarck 2020-01-15


using System;
using System.Collections.Generic;
namespace c_sharp
{
    class MainClass
    {
        public static void Main(string[] args)
        {
            List<Int32> intList = new List<Int32>();
            int count = 0;
            for (int i = 0; i < 10; i++)
            {
                int x = Convert.ToInt32(Console.ReadLine());
                x = x % 42;
                if (intList.Contains(x))
                {

                }
                else
                {
                    intList.Add(x);
                    count = count + 1;

                }
            }

            Console.WriteLine(count);
            

        }
    }
}
