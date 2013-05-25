"""
Multiples of 3 and 5
--------------------

If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.
Find the sum of all the multiples of 3 or 5 below 1000.

Approach:

All multiples of 3 below 1000: 3 6 9 12 15 18 21 24 ... 996 999
All multiples of 5 below 1000: 5 10 15 20 25 30 35 ... 990 995

Those are both arithmetic sequences. We can find the sum of it by the formula: 0.5*(t1 + tn)*n ==> t1 is the first element (3 or 5), tn the last (999 or 995),
n the place it occurs in the sequence, this can be found using the formula: (tn-t1)/v + 1 ==> v is the step (3 or 5).

If we add the two sums, you will have counted the numbers divisible by 15 twice, so you need to calculate that sum and subtract it from the answer.
"""
n999 = (999-3)/3 + 1
sum_of_multiples_3 = .5 * (3+999) * n999
n995 = (995-5)/5 + 1
sum_of_multiples_5 = .5 * (5+995) * n995
n990 = (990-15)/15 + 1
sum_of_multiples_15 = .5 * (15+990) * n990

print(
    """
    The sum of the multiples of 3 is {m3}
    The sum of the multiples of 5 is {m5}
    The sum of the multiples of 15 is {m15}
    The answer to Project Euler 1 is {answer}
    """.format(m3=sum_of_multiples_3,
        m5=sum_of_multiples_5,
        m15=sum_of_multiples_15,
        answer=(sum_of_multiples_3+sum_of_multiples_5-sum_of_multiples_15))
    )