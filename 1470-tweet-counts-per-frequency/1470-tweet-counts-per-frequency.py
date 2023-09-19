class TweetCounts:

    def __init__(self):
        self.d = collections.defaultdict(list)

    def recordTweet(self, tweetName: str, time: int) -> None:
        bisect.insort(self.d[tweetName], time)

    def getTweetCountsPerFrequency(self, freq: str, tweetName: str, startTime: int, endTime: int) -> List[int]:
        if freq == 'minute':
            ftime = 60
        elif freq == 'hour':
            ftime = 3600
        else:
            ftime = 3600 * 24
        
        stime = startTime
        ans = []
        while stime <= endTime:
            cur_end = min(stime + ftime, endTime + 1)
            ans.append(bisect.bisect_left(self.d[tweetName],cur_end) - bisect.bisect_left(self.d[tweetName],stime))
            stime += ftime
        
        return ans
        


# Your TweetCounts object will be instantiated and called as such:
# obj = TweetCounts()
# obj.recordTweet(tweetName,time)
# param_2 = obj.getTweetCountsPerFrequency(freq,tweetName,startTime,endTime)