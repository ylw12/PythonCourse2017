import tweepy
import time
import imp
import math

twitt = imp.load_source('Python', '../../../keys.py')
api = twitt.api

#See rate limit
api.rate_limit_status()

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

# -------- Define a function to extract all the followers' information.
def FriendInfo(TargetName):
	target = api.get_user(TargetName)
	target_friends = api.friends(target.id, count=200)
	fnd_names = []
	fnd_tweets = []
	fnd_flws = []
	All_friends = []
	layman = []
	expert = []
	celebrity = []
	for i in range(0, len(target_friends)):
		fnd_names.append(target_friends[i].screen_name)
		fnd_tweets.append(target_friends[i].statuses_count)
		fnd_flws.append(target_friends[i].followers_count)
	# Put everthing together in the dictionaries and 
	# classify all these friends into layman, expert or celebrity.
	for i in range(0, len(target_friends)):
		All_friends.append({"Name": fnd_names[i], 
			"Total Tweets": fnd_tweets[i], "Total Followers": fnd_flws[i]})
		if All_friends[i]["Total Followers"] < 100:
			layman.append({"Name": fnd_names[i], "Total Tweets": fnd_tweets[i]})
		elif 100 <= All_friends[i]["Total Followers"] <= 1000:
			expert.append({"Name": fnd_names[i], "Total Tweets": fnd_tweets[i]})
		else:
			celebrity.append({"Name": fnd_names[i], "Total Tweets": fnd_tweets[i]})
	act_l = layman[max(xrange(len(layman)), 
		key=lambda index: layman[index]["Total Tweets"])]
	act_e = expert[max(xrange(len(expert)), 
		key=lambda index: expert[index]["Total Tweets"])]
	act_c = celebrity[max(xrange(len(celebrity)), 
		key=lambda index: celebrity[index]["Total Tweets"])]
	pop = All_friends[max(xrange(len(All_friends)), 
		key=lambda index: All_friends[index]["Total Followers"])]
	print "The most active layman is: %s \nHer or his total tweet number is: %s." %(act_l["Name"], act_l["Total Tweets"])
	print "The most active expert is: %s \nHer or his total tweet number is: %s." %(act_e["Name"], act_e["Total Tweets"])
	print "The most active celebrity is: %s \nHer or his total tweet number is: %s." %(act_c["Name"], act_c["Total Tweets"])
	print "The most popular friend is: %s \nHer or his total follower number is: %s" %(pop["Name"], pop["Total Followers"])

# -------- Use the function to answer the question.
# Q: Among the friends of your target, i.e. the users she is 
	#following, who are the most active layman, expert and celebrity?
# Q: Among the friends of your target who is the most popular?
FriendInfo("PatrickRickert")
# A:The most active layman is: haleybpritchard 
#	Her or his total tweet number is: 1649.
# 	The most active expert is: LucyRose193 
#	Her or his total tweet number is: 18221.
# 	The most active celebrity is: MaraWilson 
# 	Her or his total tweet number is: 95297.
# A:The most popular friend is: BarackObama 
#	Her or his total follower number is: 93849053


# -------- Two degrees of separation: -------- 
# (For the following two questions, limit your search of 
	# followers and friends to laymen and experts.)
# -------- Define a function to extract all the followers' and their followers' information.
def FollowerFollowerInfo(TargetName):
	target = api.get_user(TargetName)
	target_followers = api.followers(target.id, count = 200)
	flw_names = []
	flw_tweets = []
	All_followers = []
	try:
		# Extract all the followers' information
		for i in range(0, len(target_followers)):
			if target_followers[i].followers_count > 1000:
				pass
			else:
				flw_names.append(target_followers[i].screen_name)
				flw_tweets.append(target_followers[i].statuses_count)
		# Put the followers' and their followers' information into a dictionary
		for j in range(0, len(flw_names)):
			# Add the target's followers
			All_followers.append({"Name": flw_names[j], "Total Tweets": flw_tweets[j]})
			try:
				# Add the target's follower's followers
				new_target = api.get_user(flw_names[j])
				new_target_followers = api.followers(new_target.id, count = 200)
				new_flw_names = []
				new_flw_tweets = []
				# Extract the follower's followers' information
				for k in range(0, len(new_target_followers)):
					if new_target_followers[k].followers_count > 1000:
						pass
					else:
						new_flw_names.append(new_target_followers[k].screen_name)
						new_flw_tweets.append(new_target_followers[k].statuses_count)
				# Add these information to the "All_followers" dictionary
				for k in range(0, len(new_flw_names)):
					All_followers.append({"Name": new_flw_names[k], "Total Tweets": new_flw_tweets[k]})	
			except tweepy.TweepError as e:
				print e
				continue
	except tweepy.TweepError as f:
		print f
	# Find the most active person
	act = All_followers[max(xrange(len(All_followers)), 
		key=lambda index: All_followers[index]["Total Tweets"])]
	print "The most active person is: %s \nHer or his total tweet number is: %s." %(act["Name"], act["Total Tweets"])

# -------- Use the function to answer the question.
# Q: Among the followers of your target and their followers, who is the most active?
FollowerFollowerInfo("elrossit1")
# Rate limit reached. Sleeping for: 503
#The most active person is: lizzie_erftmier 
# Her or his total tweet number is: 33756.

# Q: Among the friends of your target and their friends, who is the most active?
