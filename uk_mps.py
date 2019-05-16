import tweepy

consumer_key="" #import your tokens from your app here 
consumer_secret=""
api_token=""
api_secret=""
auth = tweepy.OAuthHandler(consumer_key.rstrip(), consumer_secret.rstrip())
auth.set_access_token(api_token.rstrip(), api_secret.rstrip())
api = tweepy.API(auth) 

labour = []
tories = []
snp = []
libdem = []

for member in tweepy.Cursor(api.list_members, 'tweetminster', 'uk-mps-labour').items():
    labour.append(member.screen_name)
for member in tweepy.Cursor(api.list_members, 'tweetminster', 'uk-mps-conservative').items():
    snp.append(member.screen_name)
for member in tweepy.Cursor(api.list_members, 'tweetminster', 'uk-mps-snp').items():
    snp.append(member.screen_name)
for member in tweepy.Cursor(api.list_members, 'markpack', 'libdem-mps').items():
    libdem.append(member.screen_name)
