/*
 * @lc app=leetcode.cn id=3 lang=c
 *
 * [3] Longest Substring Without Repeating Characters
 */

// @lc code=start


int lengthOfLongestSubstring(char* s){
    int counter = 0;
    int max = 0;
    int start = 0;
    int index[128] = {0};
    int i = 0;

    for (i=0; s[i]!='\0'; i++){
        if (index[s[i]] > start){
            counter = i - start;
            if (counter>max) max = counter;
            start = index[s[i]];
        }
        index[s[i]] = i+1;
    }
    counter = i-start;
    if (counter>max) max = counter;

    return max;
}
// @lc code=end

