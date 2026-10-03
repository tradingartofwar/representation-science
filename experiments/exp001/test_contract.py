"""Synthetic pre-freeze kernel/contract checks; no q=10 matrix calls."""
import unittest
from fractions import Fraction as F
from core import (Meter, physical_profile, threshold_profile, profile_optimum,
                  union, append_speed, hull_planes, BudgetExceeded)
from check import grade,set_difference_witness
from run import invoke


class ContractTests(unittest.TestCase):
    def test_closed_equality_and_full_sets(self):
        p=physical_profile([1,2],Meter())
        best,ts=profile_optimum(p,Meter())
        self.assertEqual((best,ts),(F(1,3),[F(1,3),F(2,3)]))
        atpeak=threshold_profile(p,F(1,3),Meter())
        self.assertEqual(union([(a,b) for a,b,c,d in atpeak]),
                         [(F(1,3),F(1,3)),(F(2,3),F(2,3))])
        safe=threshold_profile(p,F(1,8),Meter())
        self.assertEqual(union([(a,b) for a,b,c,d in safe]),
                         [(F(1,8),F(7,16)),(F(9,16),F(7,8))])

    def test_addition_matches_full_construction(self):
        original=physical_profile([1],Meter())
        updated=append_speed(original,2,F(1,8),Meter())
        direct=threshold_profile(physical_profile([1,2],Meter()),F(1,8),Meter())
        self.assertEqual(updated,direct)

    def test_hull_recovers_interior(self):
        vertices=[tuple(map(F,p)) for p in [(0,0,0),(1,0,0),(0,1,0),(0,0,1)]]
        planes=hull_planes(vertices,Meter())
        self.assertEqual(len(planes),4)
        self.assertTrue(all(sum(n*F(1,4) for n in p[:3])<=p[3] for p in planes))
        self.assertFalse(all(sum(n for n in p[:3])<=p[3] for p in planes))

    def test_completeness_not_soundness(self):
        expected=[(F(1,3),F(1,3)),(F(2,3),F(2,3))]
        self.assertEqual(set_difference_witness(expected,expected[:1])['time'],'2/3')
        truth=dict(optimum=F(1,3),times=[F(1,3),F(2,3)],components=expected,exists=True)
        incomplete=grade('Q4',dict(output=['1/3'],supported=False,partial=True),truth,[1,2],F(1,3))
        self.assertEqual(incomplete['status'],'INADEQUATE')
        uncertified=grade('Q3',dict(output='1/3',supported=False,partial=True),truth,[1,2],F(1,3))
        self.assertEqual(uncertified['status'],'UNKNOWN')

    def test_isolated_worker_and_phase_contract(self):
        config=dict(added_speed=2,threshold='1/8')
        response=invoke(dict(kind='physical_generator',epoch='child',speeds=[1,2]),'Q2','internal',config)
        self.assertTrue(response['supported'])
        self.assertEqual(response['output'],dict(time='1/8',laps=[0,0],phases=['1/8','1/4']))
        cache=invoke(dict(kind='threshold_set',epoch='child',components=[['1/8','7/16']]),'Q2','native',config)
        self.assertFalse(cache['supported'])

    def test_budget_stop_is_distinct(self):
        with self.assertRaises(BudgetExceeded):
            Meter().tick('synthetic',2000001)
        result=grade('Q1',dict(resource_limit='cap'),dict(exists=True),[1],F(1,8))
        self.assertEqual(result['status'],'UNKNOWN')


if __name__=='__main__':
    unittest.main()
