import base64
import datetime
import os
from tweepy import OAuthHandler
from tweepy import Stream
from tweepy.streaming import StreamListener

import collections
import datetime
import time

from apiclient import discovery
# import dateutil.parser
import httplib2
from oauth2client.client import GoogleCredentials

SCOPES = ['https://www.googleapis.com/auth/bigquery',
          'https://www.googleapis.com/auth/pubsub']
NUM_RETRIES = 3



def get_credentials():
    """Get the Google credentials needed to access our services."""
    credentials = GoogleCredentials.get_application_default()
    if credentials.create_scoped_required():
            credentials = credentials.create_scoped(SCOPES)
    return credentials


def create_bigquery_client(credentials):
    """Build the bigquery client."""
    http = httplib2.Http()
    credentials.authorize(http)
    return discovery.build('bigquery', 'v2', http=http)


def create_pubsub_client(credentials):
    """Build the pubsub client."""
    http = httplib2.Http()
    credentials.authorize(http)
    return discovery.build('pubsub', 'v1beta2', http=http)


def flatten(lst):
    """Helper function used to massage the raw tweet data."""
    for el in lst:
        if (isinstance(el, collections.Iterable) and
                not isinstance(el, basestring)):
            for sub in flatten(el):
                yield sub
        else:
            yield el


def cleanup(data):
    """Do some data massaging."""
    if isinstance(data, dict):
        newdict = {}
        for k, v in data.items():
            if (k == 'coordinates') and isinstance(v, list):
                # flatten list
                newdict[k] = list(flatten(v))
            elif k == 'created_at' and v:
                newdict[k] = str(dateutil.parser.parse(v))
            # temporarily, ignore some fields not supported by the
            # current BQ schema.
            # TODO: update BigQuery schema
            elif (k == 'video_info' or k == 'scopes' or k == 'withheld_in_countries'
                  or k == 'is_quote_status' or 'source_user_id' in k
                  or k == ''
                  or 'quoted_status' in k or 'display_text_range' in k or 'extended_tweet' in k
                  or 'media' in k):
                pass
            elif v is False:
                newdict[k] = v
            else:
                if k and v:
                    newdict[k] = cleanup(v)
        return newdict
    elif isinstance(data, list):
        newlist = []
        for item in data:
            newdata = cleanup(item)
            if newdata:
                newlist.append(newdata)
        return newlist
    else:
        return data


def bq_data_insert(bigquery, project_id, dataset, table, tweets):
    """Insert a list of tweets into the given BigQuery table."""
    try:
        rowlist = []
        # Generate the data that will be sent to BigQuery
        for item in tweets:
            item_row = {"json": item}
            rowlist.append(item_row)
        body = {"rows": rowlist}
        # Try the insertion.
        response = bigquery.tabledata().insertAll(
                projectId=project_id, datasetId=dataset,
                tableId=table, body=body).execute(num_retries=NUM_RETRIES)
        # print "streaming response: %s %s" % (datetime.datetime.now(), response)
        return response
        # TODO: 'invalid field' errors can be detected here.
    except Exception, e1:
        print "Giving up: %s" % e1

# Get your twitter credentials from the environment variables.
# These are set in the 'twitter-stream.json' manifest file.
consumer_key = 'EtMLrd8H11BuIYpCIp56AWKnf'
consumer_secret = 'vmD2ECzg5XRgzmdMyhc2m7nYdo7R0fdN1fhMX1ZI4ZnSfyzsIV'
access_token = '142500263-rhpKzqQAiHpJaXJbmCXWa3xTypWzaMSydNE0Mc83'
access_token_secret = 'vpLmeHdfrCmOSoP5fBkE8krjPYP6XZf5Wvy3rJeSKe2bI'

PUBSUB_TOPIC = 'projects/servinf-geomark-social-prod/topics/tweets'
NUM_RETRIES = 3


def publish(client, pubsub_topic, data_lines):
    """Publish to the given pubsub topic."""
    messages = []
    for line in data_lines:
        pub = base64.urlsafe_b64encode(line)
        messages.append({'data': pub})
    body = {'messages': messages}
    resp = client.projects().topics().publish(
            topic=pubsub_topic, body=body).execute(num_retries=NUM_RETRIES)
    return resp


class StdOutListener(StreamListener):
    """A listener handles tweets that are received from the stream.
    This listener dumps the tweets into a PubSub topic
    """

    count = 0
    twstring = ''
    tweets = []
    batch_size = 50
    total_tweets = 10000000
    client = create_pubsub_client(get_credentials())

    def write_to_pubsub(self, tw):
        publish(self.client, PUBSUB_TOPIC, tw)

    def on_data(self, data):
        """What to do when tweet data is received."""
        self.tweets.append(data)
        if len(self.tweets) >= self.batch_size:
            self.write_to_pubsub(self.tweets)
            self.tweets = []
        self.count += 1
        # if we've grabbed more than total_tweets tweets, exit the script.
        # If this script is being run in the context of a kubernetes
        # replicationController, the pod will be restarted fresh when
        # that happens.
        if self.count > self.total_tweets:
            return False
        if (self.count % 1000) == 0:
            print 'count is: %s at %s' % (self.count, datetime.datetime.now())
        return True

    def on_error(self, status):
        print status


if __name__ == '__main__':
    print '....'
    listener = StdOutListener()
    auth = OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)

    stream = Stream(auth, listener)
    # set up the streaming depending upon whether our mode is 'sample', which
    # will sample the twitter public stream. If not 'sample', instead track
    # the given set of keywords.
    # This environment var is set in the 'twitter-stream.yaml' file.
    stream.filter(
                track=['Presidente Duque', 'Ivan Duque', 'Duque', 'Presidente Colombia']
                )