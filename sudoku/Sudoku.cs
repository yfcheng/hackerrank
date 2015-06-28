using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Drawing;

namespace Sudoku
{
    class PointerMatrix
    {
        public Point Point { get; set; }
        public int Counter { get; set; }
    }
    class Sudoku
    {
        static void Main(string[] args)
        {
            int[,] sudokuin = new int[,]{ 
                                { 0,6,0,0,0,0,0,0,7 },
                                { 0,0,4,8,0,0,0,1,0 }, 
                                { 0,0,2,5,0,7,0,0,0 },
                                { 1,0,0,0,2,0,0,0,5 }, 
                                { 4,0,0,0,9,0,0,0,6 },
                                { 3,0,0,0,7,0,0,0,8 }, 
                                { 0,0,0,7,0,4,8,0,0 },
                                { 0,5,0,0,0,3,2,0,0 }, 
                                { 7,0,0,0,0,0,0,9,0 } };
            Console.WriteLine(PrintBoard(sudokuin));
        loop:            
            Console.WriteLine("\nHit enter to solve");
            ConsoleKeyInfo keyinfo = Console.ReadKey();
            if (keyinfo.Key == ConsoleKey.Enter)
                Solve(sudokuin);
            else
                goto loop;
            Console.ReadLine();
        }

        static void Solve(int[,] puzzle)
        {
            StringBuilder l_puzzleBoard = new StringBuilder();
            for (int i = 0; i <= puzzle.GetUpperBound(0); i++)
            {
                if (i != 0 && i % 3 == 0)
                    l_puzzleBoard.Append("\n");

                for (int j = 0; j <= puzzle.GetUpperBound(1); j++)
                {
                    if (j != 0 && j % 3 == 0)
                        l_puzzleBoard.Append("\t");

                    if (puzzle[i, j] == 0)
                        l_puzzleBoard.Append(string.Format(" {0},{1} ", i, j));
                    else
                        l_puzzleBoard.Append(" X ");
                }
                l_puzzleBoard.Append("\n");
            }

            List<PointerMatrix> l_validpoints = new List<PointerMatrix>();

            for (int i = 0; i <= puzzle.GetUpperBound(0); i++)
            {
                for (int j = 0; j <= puzzle.GetUpperBound(1); j++)
                {
                    if (puzzle[i, j] == 0)
                    {
                        PointerMatrix l_pntr = new PointerMatrix();
                        Point l_pnt = new Point();
                        l_pnt.X = i;
                        l_pnt.Y = j;
                        l_pntr.Point = l_pnt;
                        l_validpoints.Add(l_pntr);
                    }                        
                }
            }

            //foreach (PointerMatrix validPoint in l_validpoints)
            //{
            //    int x = validPoint.Point.X;
            //    int y = validPoint.Point.Y;
            //    int cnt = 0;
            //    for (int j = 0; j <= puzzle.GetUpperBound(1); j++)
            //    {
            //        if (puzzle[x, j] != 0)
            //            cnt++;
            //    }

            //    for (int k = 0; k <= puzzle.GetUpperBound(0); k++)
            //    {
            //        if (puzzle[k, y] != 0)
            //            cnt++;
            //    }

            //    int lbx = (x / 3) * 3;                
            //    int ubx = ((x / 3) + 1) * 3 - 1;
            //    int lby = (y / 3) * 3;
            //    int uby = ((y / 3) + 1) * 3 - 1; 
              
            //    for(int l=lbx;l<=ubx;l++)
            //    {
            //        for (int m = lby; m <= uby; m++)
            //            if (puzzle[l, m] != 0)
            //                cnt++;
            //    }
            //    validPoint.Counter = cnt;
            //}
            //l_validpoints.OrderByDescending(n => n.Counter);

            foreach (Point pnt in l_validpoints.Select(n => n.Point))
            {
                HashSet<int> tempnumbers = new HashSet<int>() { 1, 2, 3, 4, 5, 6, 7, 8, 9 };

                int x = pnt.X;
                int y = pnt.Y;
                int cnt = 0;
                for (int j = 0; j <= puzzle.GetUpperBound(1); j++)
                {
                    if (j == y)
                        continue;

                    if (puzzle[x, j] != 0)
                    { 
                        if(tempnumbers.Contains(puzzle[x, j]))
                            tempnumbers.Remove(puzzle[x, j]);
                    }
                }

                for (int k = 0; k <= puzzle.GetUpperBound(0); k++)
                {
                    if (k == x)
                        continue;

                    if (puzzle[k, y] != 0)
                    {
                        if (tempnumbers.Contains(puzzle[k, y]))
                            tempnumbers.Remove(puzzle[k, y]);
                    }
                }

                int lbx = (x / 3) * 3;
                int ubx = ((x / 3) + 1) * 3 - 1;
                int lby = (y / 3) * 3;
                int uby = ((y / 3) + 1) * 3 - 1;

                for (int l = lbx; l <= ubx; l++)
                {
                    for (int m = lby; m <= uby; m++)
                    { 
                        
                        if (puzzle[l, m] != 0)
                        {
                            if (tempnumbers.Contains(puzzle[l, m]))
                                tempnumbers.Remove(puzzle[l, m]);
                        }                       

                    }
                }
            }

            Console.WriteLine(l_puzzleBoard.ToString());
        }


        static string PrintBoard(int[,] puzzle)
        { 
            StringBuilder l_puzzleBoard = new StringBuilder();
            for (int i = 0; i <= puzzle.GetUpperBound(0); i++)
            {
                if (i!=0 && i % 3 == 0)
                    l_puzzleBoard.Append("\n");
                for (int j = 0; j <= puzzle.GetUpperBound(1); j++)
                {
                    if (j!=0 && j % 3 == 0)
                        l_puzzleBoard.Append("\t");
                    l_puzzleBoard.Append(" " + puzzle[i, j]);
                }                
                l_puzzleBoard.Append("\n");
            }
            return l_puzzleBoard.ToString();    
        }
    }
}