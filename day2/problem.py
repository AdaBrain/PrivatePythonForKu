'''
========================================================
Given a dictionary, find mean of all the values present.
========================================================
Ex.1
Input : 
test_dict = {"Gfg" : 4, "is" : 4, "Best" : 4, "for" : 4, "Geeks" : 4} 
Output : 4.0 
Explanation : (4 + 4 + 4 + 4 + 4) / 4 = 4.0, hence mean. 
========================================================
Ex.2
Input : test_dict = {"Gfg" : 5, "is" : 10, "Best" : 15} 
Output : 10.0 
Explanation : Mean of these is 10.0
'''

test_dict = {"Gfg" : 4, "is" : 4, "Best" : 4, "for" : 4, "Geeks" : 4}
message = '''To dive deeper and have a hands-on experience with Python 3.11, head over to our dedicated tutorial or video course about the new features, where you can make your way through the most important language improvements with code examples.

Even though Python 3.11 has just been released, it’s going to be a while before companies and cloud service providers start using it in production on a larger scale. Upgrading the runtime environment is always risky and can lead to downtime, data loss, or other unforeseen problems. That’s precisely why the US army refuses to upgrade their old-school software on mission-critical equipment.

At the same time, it’s worth mentioning that some major Python libraries, especially those in the data science field, began supporting Python 3.11 and tested it thoroughly before the official release. This ensures that users can make a safe switch to Python 3.11 and start taking advantage of the new language features without having to wait for their package dependencies to catch up.

What’s your favorite new feature in Python 3.11?'''

freq = {}
for word in message.split(" "):
    if freq.get(word):
        freq[word] += 1
    else:
        freq[word] = 1

print(freq)
maxKey = max(freq, key=freq.get) # the
print(maxKey, ":", freq[maxKey])