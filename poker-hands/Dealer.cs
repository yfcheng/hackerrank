using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Collections;
using PokerHands;

namespace Poker
{
    public class CardSelection
    {
        public string CardSelect { get; set; }
        public int Count { get; set; }
    }

    public class Dealer
    {
        ///private string[] m_Cards = new string[13] { "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine", "Ten", "Jack", "Queen", "King", "Ace" };
        ///private string[] m_Suites = new string[4]{"Spade","Clubs","Diamonds","Hearts"};
        private List<CardSuites> m_DealCards = new List<CardSuites>();
        private List<Cards> l_setupCards = new List<Cards>();
        private List<Suites> l_setupSuites = new List<Suites>();

        string flushSuite = string.Empty;
        string threeOfAKind = string.Empty;
        string onePair = string.Empty;
        string twoPair = string.Empty;


        private void SetupCards()
        {
            l_setupCards.Add(new Cards() { Text = "Two", Value = 2 });
            l_setupCards.Add(new Cards() { Text = "Three", Value = 3 });
            l_setupCards.Add(new Cards() { Text = "Four", Value = 4 });
            l_setupCards.Add(new Cards() { Text = "Five", Value = 5 });
            l_setupCards.Add(new Cards() { Text = "Six", Value = 6 });
            l_setupCards.Add(new Cards() { Text = "Seven", Value = 7 });
            l_setupCards.Add(new Cards() { Text = "Eight", Value = 8 });
            l_setupCards.Add(new Cards() { Text = "Nine", Value = 9 });
            l_setupCards.Add(new Cards() { Text = "Ten", Value = 10 });
            l_setupCards.Add(new Cards() { Text = "Jack", Value = 11 });
            l_setupCards.Add(new Cards() { Text = "Queen", Value = 12 });
            l_setupCards.Add(new Cards() { Text = "King", Value = 13 });
            l_setupCards.Add(new Cards() { Text = "Ace", Value = 14 });
        }

        private void SetupSuites()
        {
            l_setupSuites.Add(new Suites() { Text = "Spade" });
            l_setupSuites.Add(new Suites() { Text = "Clubs" });
            l_setupSuites.Add(new Suites() { Text = "Diamonds" });
            l_setupSuites.Add(new Suites() { Text = "Hearts" });
        }

        private CardSuites GetRandomCardSuites()
        {
            int l_card = RandomNumber(0, 12);
            int l_face = RandomNumber(0, 3);
            CardSuites l_dealTempCardSuite = new CardSuites() { Cards = l_setupCards[l_card], Suites = l_setupSuites[l_face] };
            if (m_DealCards.Contains(l_dealTempCardSuite))
                return GetRandomCardSuites();
            return l_dealTempCardSuite;
        }

        private int RandomNumber(int min, int max)
        {
            Random random = new Random();
            return random.Next(min, max);
        }

        private string OutStream(CardSuites[] cardSuites)
        {
            StringBuilder l_cardsDeal = new StringBuilder();
            foreach (CardSuites input in cardSuites)
            {
                l_cardsDeal.Append(input.Cards.Text);
                l_cardsDeal.Append(" ");
                l_cardsDeal.Append(input.Suites.Text);
                l_cardsDeal.Append("\n");
            }
            return l_cardsDeal.ToString();
        }

        public Dealer()
        {
            SetupCards();
            SetupSuites();
        }

        public string GetDealtCards(int dealCards)
        {
            for (int i = 0; i <= dealCards - 1; i++)
                m_DealCards.Add(GetRandomCardSuites());

            CardSuites[] l_temp = new CardSuites[dealCards];
            for (int j = 0; j < l_temp.Length; j++)
            {
                int lastIdx = m_DealCards.Count - 1 - j;
                l_temp[j] = m_DealCards[lastIdx];
            }
            return OutStream(l_temp);
        }

        public string GetBestHands()
        {
            var sortedGroups = from deal in m_DealCards
                               orderby deal.Cards.Value
                               select deal;
            Console.WriteLine(OutStream(sortedGroups.ToArray()));

            if(IsFlush())
                Console.WriteLine(string.Format("There is a flush : {0}", flushSuite));

            if (IsThreeOfAKind())
                Console.WriteLine(string.Format("There is a three of a kind card : {0}", threeOfAKind));

            if (IsTwoPair())
                Console.WriteLine(string.Format("There is two pair card : {0}", twoPair));

            if (IsOnePair())
                Console.WriteLine(string.Format("There is a one pair card : {0}", onePair));

            return string.Empty;
        }

        #region PokerHands
        private bool IsThreeOfAKind()
        {
            var threeOfKind = from deal in m_DealCards
                              group deal by deal.Cards.Value into g1
                              where g1.Count() >= 3
                              select new
                              {
                                  CardValue = g1.Key,
                                  CardCount = g1.Count()
                              };
            if (threeOfKind.Count() > 0)
            {
                threeOfAKind = threeOfKind.FirstOrDefault().CardValue.ToString();
                return true;
            }

            return false;
        }

        private bool IsTwoPair()
        {
            var twoPairedCard = from deal in m_DealCards
                              group deal by deal.Cards.Value into g2
                              where g2.Count() == 2
                              select new CardSelection
                              {
                                  CardSelect = l_setupCards.Find(n=>n.Value==g2.Key).Text,
                                  Count = g2.Count()
                              };

            if (twoPairedCard.Count() > 1)
            {
                for (int k = 0; k < twoPairedCard.Count(); k++)
                    twoPair = twoPair + twoPairedCard.ToArray()[k].CardSelect + " , ";
                return true;
            }
            return false;
        }

        private bool IsOnePair()
        {
            var onePairCard = from deal in m_DealCards
                              group deal by deal.Cards.Value into g1
                              where g1.Count() == 2
                              select new CardSelection
                              {
                                  CardSelect = l_setupCards.Find(n => n.Value == g1.Key).Text,
                                  Count = g1.Count()
                              };
            if (onePairCard.Count() == 1)
            {
                onePair = onePairCard.FirstOrDefault().CardSelect.ToString();
                return true;
            }
            return false;
        }

        private bool IsFlush()
        {
            var flushCards = from deal in m_DealCards
                             group deal by deal.Suites.Text into g
                             where g.Count() >= 5
                             select new CardSelection
                             {
                                 CardSelect = l_setupSuites.Find(n => n.Text.Equals(g.Key,StringComparison.InvariantCultureIgnoreCase)).Text,
                                 Count = g.Count()                                    
                             };
            if (flushCards.Count() > 0)
            {
                flushSuite = flushCards.FirstOrDefault().CardSelect;
                return true;
            }
            return false;
        }
        #endregion
    }
}