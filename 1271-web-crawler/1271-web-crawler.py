# """
# This is HtmlParser's API interface.
# You should not implement it, or speculate about its implementation
# """
#class HtmlParser(object):
#    def getUrls(self, url):
#        """
#        :type url: str
#        :rtype List[str]
#        """
from collections import deque

class Solution:
    def crawl(self, startUrl: str, htmlParser: 'HtmlParser') -> List[str]:
        def get_hostname(url: str):
            return url.split("/")[2]
        start_hostname = get_hostname(startUrl)
        q = deque([startUrl])
        visited = set([startUrl])
        while q:
            url = q.popleft()
            for next_url in htmlParser.getUrls(url):
                if get_hostname(next_url) == start_hostname and next_url not in visited:
                    q.append(next_url)
                    visited.add(next_url)
        
        return visited

# Complexity Analysis
# Let nnn be the total number of URLs (urls.length), mmm be the number of edges in the graph, and lll be the maximum length of a URL (urls[i].length).
# Let k be the number of traversed vertices. We add each of these vertices to the set and to the queue in up to O(l) per vertex. The total time for inserting into the set and into the queue is thus O(k⋅l)
# The total number of elements in htmlParser.getUrls(url) over all URLs is mmm – the total number of edges in the graph. Each element can have a length of O(l)O(l)O(l). The sum of lengths of the elements of htmlParser.getUrls(url) over all URLs is O(m⋅l)O(m \cdot l)O(m⋅l).
# The total complexity is O(k⋅l+m⋅l)O(k \cdot l + m \cdot l)O(k⋅l+m⋅l). Since k=O(m)k = O(m)k=O(m), we can simplify this expression to O(m⋅l)O(m \cdot l)O(m⋅l).
# Time complexity: O(m⋅l)
# Space complexity: O(n⋅l)