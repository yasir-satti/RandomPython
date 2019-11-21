import pytest
import Blackjack

def test_deal():
    assert Blackjack.deal([2,2,2,2,2,2,2,2,2,2,2,2,2,2]*4)==[2,2]

def test_deal_int_converter():
    assert Blackjack.deal([12,12,12,12,12,12,12,12,12,12,12,12,12]*4)==["Q","Q"]

def test_total_standard():
    assert Blackjack.total([4,6,"Q"])==20

def test_total_ace_maths1():
    assert Blackjack.total(["A",8,"A"])==20

def test_total_ace_maths2():
    assert Blackjack.total([10,"A","A","A"])==13

def test_total_stress_test():
    assert Blackjack.total([7,"A","A","A","A"])==21

def test_total_JQK_maths():
    assert Blackjack.total(["J","Q","K"])==30
