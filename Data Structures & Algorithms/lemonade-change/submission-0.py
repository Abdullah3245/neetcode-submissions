class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        # keep tracks of all the five
        five_bill = 0
        ten_bill = 0

        for bill in bills:
            if bill == 5:
                five_bill += 1
            elif bill == 10:
                if five_bill < 1:
                    return False
                five_bill -= 1
                ten_bill += 1

            elif bill == 20:
                if five_bill >= 3:
                    five_bill -= 3
                elif five_bill >= 1 and ten_bill >= 1:
                    five_bill -= 1
                    ten_bill -= 1
                else:
                    return False
        
        return True
