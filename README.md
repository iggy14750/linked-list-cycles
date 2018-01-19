Linked List Cycle Detector
==========================

While the typical approach is O(n) in time and space, (`cycle1()` in `cycle.py`), there is another approach which is O(n) in time, but O(1) in space.
This solution involves keeping two pointers which both walk the list, but one moves twice as fast as the other.
In the case there is no cycle, the fast pointer quickly reaches the end of the list.
When there is a cycle, however, we will see the fast pointer catch up to the slow one, and in doing so, be able to conclude that the list does contain a cycle.

It is not immediately apparent that this chase will remain linear time.
Consider that the list is now in two distinct pieces: the front, which will be visited only once by each pointer, and the cycle, which may appear many times.
I belive it is fair to consider both as a constant fraction of the overall length of the list.
Then, the time for both pointers to enter the cycle (leave behind the front) is linear.
Moreover, since the slow pointer will not make an entire walk around the cycle (see below), the time in the cycle is bounded by linear time as well.

Why will the slow pointer not make a whole trip around the cycle?
*Sounds like the setup to a terrible joke.*
Imagine, to the contrary, that it does.
Then the fast pointer will have made two trips around it in the same time, and will therefore have already seen the slow pointer.

And I swear I didn't look this up, Mike.
Wish there was someway I could prove it to you.
Enjoy anyhow!
