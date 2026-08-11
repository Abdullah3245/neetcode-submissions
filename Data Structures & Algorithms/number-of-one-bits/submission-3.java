class Solution {
public int hammingWeight(int n) {
    int count = 0;
    // Loop until all bits are processed
    while (n != 0) {
        count += n & 1; // Add the least significant bit to count
        n >>>= 1; // Unsigned right shift to process the next bit
    }
    return count;
}

}
