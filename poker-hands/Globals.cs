using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;

namespace PokerHands
{
    public static class Globals
    {
        public enum PokerHands
        {
            None,
            StraightFlush,
            FourOfAKind,
            FullHouse,
            Flush,              ///done
            Straight,
            ThreeOfAKind,       ///done
            TwoPair,
            OnePair,
            HighCards
        }
    }
}