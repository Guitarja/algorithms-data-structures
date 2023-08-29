class Solution {
public:
    int jump(vector<int>& nums) {
        int destination = int(nums.size()) - 1;
        int cur_coverage = 0;
        int last_jump_index = 0;
        int times_of_jump = 0;
        if (destination == 0){
            return 0;
        }

        for(int i = 0; i < destination + 1; i++){
            cur_coverage = max(cur_coverage, nums[i] + i);
            if (i == last_jump_index){
                last_jump_index = cur_coverage;
                times_of_jump++;
                if(cur_coverage >= destination){
                    return times_of_jump;
                }
            }
        }
        return times_of_jump;
    }
};