#Register an app: https://dev.twitter.com/

#sudo pip install tweepy
import tweepy
import time

#Check the documentation page
#http://docs.tweepy.org/en/v3.2.0/
#Get access to API


#See rate limit
api.rate_limit_status()

#Create user objects
target = api.get_user('PatrickRickert')
target.followers_count # Our target has 115 followers.
target.followers_ids() #creates a list of follower ids

# From now on, we define the most active user as a user
	#with the greatest number of total tweets.

# -------- One degree of separation: --------
# -------- Define a function to extract all the followers' information.
def FollowerInfo(TargetName):
	target = api.get_user(TargetName)
	target_followers = api.followers(target.id, count=200)
	flw_names = []
	flw_tweets = []
	flw_flws = []
	All_followers = []
	# Extract all the followers' information
	for i in range(0, len(target_followers)):
		flw_names.append(target_followers[i].screen_name)
		flw_tweets.append(target_followers[i].statuses_count)
		flw_flws.append(target_followers[i].followers_count)
	# Put everthing together in the dictionaries
	for i in range(0, len(target_followers)):
		All_followers.append({"Name": flw_names[i], 
			"Total Tweets": flw_tweets[i], "Total Followers": flw_flws[i]})
	act = All_followers[max(xrange(len(All_followers)), 
		key=lambda index: All_followers[index]["Total Tweets"])]
	pop = All_followers[max(xrange(len(All_followers)), 
		key=lambda index: All_followers[index]["Total Followers"])]
	print "The most active follower is: %s \nHer or his total tweet number is: %s." %(act["Name"], act["Total Tweets"])
	print "The most popular follower is: %s \nHer or his total follower number is: %s" %(pop["Name"], pop["Total Followers"])

# -------- Use the function to answer the question.
# Q: Among the followers of your target who is the most active?
# Q: Among the followers of your target who is the most popular, 
	#i.e. has the greatest number of followers?
FollowerInfo("PatrickRickert")
# A:The most active follower is: simonwillo 
# 	Her or his total tweet number is: 54273.
# A:The most popular follower is: benlandis 
#	Her or his total follower number is: 3237135

flw_names = []
for follower in tweepy.Cursor(target_followers, count = 200, include_entities = True).items():
	flw_names.append(follower.screen_name)


for friend in tweepy.Cursor(api.friends).items():
    # Process the friend here
    process_friend(friend)

print target.screen_name
print target.followers_count
for friend in target.followers():
   print friend.screen_name

    # process status here
    mytweets.append(status.text)



# Q: Among the friends of your target, i.e. the users she is 
	#following, who are the most active layman, expert and celebrity?
# Q: Among the friends of your target who is the most popular?

# -------- Two degrees of separation: -------- 
# (For the following two questions, limit your search of 
	# followers and friends to laymen and experts.)

# Q: Among the followers of your target and their followers, who is the most active?
# Q: Among the friends of your target and their friends, who is the most active?




#What can I do using this object?
dir(target)

#Get some of her information
batman.id
batman.name
batman.screen_name
batman.location

#Check her tweets
batman.status
batman.status.text
batman.statuses_count

#Check her followers
target.followers_count
target.followers() #creates a list of user objects - only the first 20!
api.followers(target.id,count=1) #creates a list of user objects - can get up to 200


api.followers_ids('BigDataBatman')


for follower_id in mich.followers_ids():
	user = api.get_user(follower_id)
	print user.screen_name


bstatuses = api.user_timeline('BigDataBatman',page=1)
[x.text for x in bstatuses]


#How to deal with limits

# Extract tweets
mytweets = []
for status in tweepy.Cursor(api.user_timeline, id='michtorresp').items():
    # process status here
    mytweets.append(status.text)



#Get the first 2 "pages" of follower ids
krugmans_followers=[]

# extend:
# try x=[1,2]
# x.append([3,4])
# x.extend([3,4])

for page in tweepy.Cursor(api.followers_ids, 'NYTimeskrugman').pages(2):
    krugmans_followers.extend(page)
    time.sleep(60)
    
#Get the ids of 6000 followers
krugmans_followers=[]

for item in tweepy.Cursor(api.followers_ids, 'NYTimeskrugman').items(10):
	print item
	krugmans_followers.append(item)
	time.sleep(1)
	


