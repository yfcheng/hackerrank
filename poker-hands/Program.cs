using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;

namespace Poker
{
   class Program
    {   
       static void Main(string[] args)
       {
           Dealer l_cardSuites = new Dealer();
           Console.WriteLine("initial deal");
           Console.WriteLine(l_cardSuites.GetDealtCards(5));
           Console.ReadLine();
           Console.WriteLine("your cards ");
           Console.WriteLine(l_cardSuites.GetDealtCards(2));
           Console.ReadLine();
           Console.WriteLine("choose your best hand ");
           Console.WriteLine(l_cardSuites.GetBestHands());
           Console.ReadLine();
       }
    }
}