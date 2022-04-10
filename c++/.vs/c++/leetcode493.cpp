class Solution {
public:
    int get(vector<int>& nums,int left,int right){
        if(left>=right) return 0;
        int m=(left+right)/2;
        int res=get(nums,left,m)+get(nums,m+1,right);
        int r=m+1;
        for(int i=left;i<=m;i++){
            while(r<=right && (long long)nums[i]>(long long)2*nums[r]) r++;
            res+=r-m-1;
        }
        vector<int> temp=vector<int>(right-left+1,0);
        int i=left,j=m+1,t=0;
        while(i<=m||j<=right){
            if(i>m){
                temp[t++]=nums[j++];
            }else if(j>right){
                temp[t++]=nums[i++];
            }else{
                if(nums[i]<=nums[j]){
                    temp[t++]=nums[i++];
                }else{
                    temp[t++]=nums[j++];
                }
            }
        }
        for(int i=0;i<temp.size();i++){
             nums[i+left]=temp[i];
        }
        return res;
    }
    int reversePairs(vector<int>& nums) {
       return get(nums,0,nums.size()-1);
    }
};