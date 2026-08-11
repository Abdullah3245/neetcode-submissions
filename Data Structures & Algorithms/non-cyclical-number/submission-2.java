class Solution {
    public boolean isHappy(int n) {
        HashSet<Integer> l = new HashSet<>();
        while (n > 0) {
            n = sum(n);
            System.out.println(n);
            if (l.contains(n)) {
                return false;
            }
            l.add(n);
            if (n == 1) {
                return true;
            }
        }
        return false;
    }

    public int sum(int n) {
        int sum = 0;
        while (n > 0) {
            
            if (n < 10) {
                sum = sum + (n * n);
            } else {
                int digit = n % 10;
                sum = sum + (digit * digit);
            }
            n = n / 10;
        }
        return sum;
    }


}
