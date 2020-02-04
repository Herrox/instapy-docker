""" Quickstart script for InstaPy usage """

# imports
from instapy import InstaPy
from instapy import smart_run
from instapy import set_workspace


# set workspace folder at desired location (default is at your home folder)
set_workspace(path='/home/gianluca/InstaPy')

# get an InstaPy session!
session = InstaPy(username='mythos.s3',password='Xx')



with smart_run(session):

    hashtags = ['audi', 'audisport', 'audituning', 'audiquattro', 'quattro' ,'rs3', 'quattroworld' , 'cargasm', 'audilover', 'germancar' ,'food4audis', 'audirs3' , 'rs3sedan', 'audi_official', 'audi_regram', 'audiswiss', 'audiclubswitzerland', 'audiclub', 'audifan', 'audifamily' ,'audigirl' ,'carphotography' ,'carphoto','ozwheels','fastandfurious','audia3']
    random.shuffle(hashtags)
    my_hashtags = hashtags[:10]

    # general settings
    session.set_user_interact(amount=3, randomize=True, percentage=100,media='Photo')
    session.set_relationship_bounds(
                         enabled=True,
                         potency_ratio=None,
                         delimit_by_numbers=True,
                         max_followers=10000,
                         min_followers=50,
                         min_following=50
        )

    # activity
    session.interact_user_followers([], amount=340)
