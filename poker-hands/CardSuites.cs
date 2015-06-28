using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Collections;

namespace PokerHands
{

    class CardSuites : IEquatable<CardSuites>
    {
        public Cards Cards { get; set; }
        public Suites Suites { get; set; }

        public bool Equals(CardSuites other)
        {
            return ((Cards.Value == other.Cards.Value) &&
                (string.Equals(Suites.Text, other.Suites.Text, StringComparison.InvariantCultureIgnoreCase)));
        }
    }

    class Cards
    {
        public string Text { get; set; }
        public int Value { get; set; }
    }

    class Suites
    {
        public string Text { get; set; }
    }
}