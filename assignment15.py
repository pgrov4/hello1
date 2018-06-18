print("""Q.1- Extract the user id, domain name and suffix from the following email addresses. emails = "zuck26@facebook.com" "page33@google.com" "jeff42@amazon.com"desired_output = [('zuck26', 'facebook', 'com'), ('page33', 'google', 'com'), ('jeff42', 'amazon', 'com')] Q.2- Retri""")
import re

line = "page33@google.com"
line1="zuck26@facebook.com"


matchObj = re.match(r'(.*)@(.*)(.)([a-z][a-z][a-z]).*', line, re.M|re.I)
matchObj1 = re.match(r'(.*)@(.*)(.)([a-z][a-z][a-z]).*', line1, re.M|re.I)

#print(matchObj.groups())
if matchObj:
   print("matchObj.group() : ", matchObj.group())
   print("matchObj.group(1) : ", matchObj.group(1))
   print("matchObj.group(2) : ", matchObj.group(2))
   print("matchObj.group(2) : ", matchObj.group(4))
else:
   print("No match!!")

if matchObj1:
   print("matchObj1.group() : ", matchObj1.group())
   print("matchObj1.group(1) : ", matchObj1.group(1))
   print("matchObj1.group(2) : ", matchObj1.group(2))
   print("matchObj1.group(2) : ", matchObj1.group(4))
else:
   print("No match!!")

print("""Q.2- Retrieve all the words starting with ‘b’ or ‘B’ from the following text.text = "Betty bought a bit of butter, But the butter was so bitter, So she bought some better butter, To make the bitter butter better.""")
line2="Betty bought a bit of butter, But the butter was so bitter, So she bought some better butter, To make the bitter butter better."

print(re.findall(r'\bB\w+', line2, flags=re.IGNORECASE))

print("""Q.3- Split the following irregular sentence into words sentence = "A, very very; irregular_sentence"desired_output = "A very very irregular sentence""")
text="A, very very; irregular_sentence"
regex = re.compile('((?!\n)\s+)')

text=re.sub(';', ' ', text)
text=(re.sub(',', ' ', text))
text=(re.sub('_', ' ', text))
print(text)

#print("Q.1- Clean up the following tweet so that it contains only the user’s message. That is, remove all URLs, hashtags, mentions, punctuations, RTs and CCs.tweet = '''Good advice! RT @TheNextWeb: What I would do differently if I was learning to code today http://t.co/lbwej0pxOd cc: @garybernhardt #rstats'''desired_output = 'Good advice What I would do differently if I was learning to code today'")