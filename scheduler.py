#!/bin/
#
# Reddit Post Scheduler
#
# Luke Rindels
# February 8, 2018

# imports
from prawcore import NotFound
import sys
import praw
import datetime
import time

# initialize instance 
reddit = praw.Reddit('bot1')

### functions ###
# get subreddit name
def get_sub():
    while 1:
        try:
            subname = input("Subreddit name (ex: askreddit): ")
            valid = False
            if subname:
                valid = check_sub(subname)
            if valid:
                break;
            else:
                print("Not a valid Subreddit\n")
        except KeyboardInterrupt:
            quit()

    return subname

# checks for a valid subreddit 
def check_sub(subname):
    valid = True
    try:
        reddit.subreddits.search_by_name(subname, exact=True)
    except NotFound:
        valid = False
    except KeyboardInterrupt:
        quit()

    return valid

# gets delay option
def optional_delay():
    while 1:
        try:
            return {"yes":True, "true":True, "false":False, "no":False}[input("Delayed Post? (yes/no): ").lower()]
        except KeyError:
            print("Please enter yes or no\n")
        except KeyboardInterrupt:
            quit()

# post confirmation
def confirm_post():
    while 1:
        try:
            return {"yes":True, "no":False}[input("Are you sure you would like to submit? (yes/no): ").lower()]
        except KeyError:
            print("Please enter yes or no\n")
        except KeyboardInterrupt:
            quit()
            
# delays the post by a specified amount
def delay_post():
    now = datetime.datetime.now()
    # date entry and error handling
    while 1:
        # year
        while 1:
            year = input("Year: ")
            try:
                year = int(year)
                if year >= now.year:
                    break
                else:
                    print("Year must be greater than or equal to the present year\n")
            except ValueError:
                print("Year must be entered in the form of an integer\n")
            except KeyboardInterrupt:
                quit()
        # month
        while 1:
            month = input("Month [1-12]: ")
            try:
                month = int(month)
                if month > 0 and month < 13:
                    break
                else:
                    print("Month must be entered in the form of an integer [1-12]\n")
            except ValueError:
                print("Month must be entered in the form of an integer [1-12]\n")
            except KeyboardInterrupt:
                quit()
        # day
        while 1:
            day = input("Day [1-31]: ")
            try:
                day = int(day)
                if day > 0 and day < 32:
                    break
                else:
                    print("Day must be entered in the form of an integer [1-31]\n")
            except ValueError:
                print("Day must be entered in the form of an integer [1-31]\n")
            except KeyboardInterrupt:
                quit()
        # hour
        while 1:
            hour = input("Hour [0-23]: ")
            try:
                hour = int(hour)
                if hour > -1 and hour < 24:
                    break
                else:
                    print("Hour must be entered in the form of an integer [0-23]\n")
            except ValueError:
                print("Hour must be entered in the form of an integer [0-23]\n")
            except KeyboardInterrupt:
                quit()
        # minute
        while 1:
            minute = input("Minute [0-59]: ")
            try:
                minute = int(minute)
                if minute > -1 and minute < 60:
                    break
                else:
                    print("Minute must be entered in the form of an integer [0-59]\n")
            except ValueError:
                print("Minute must be entered in the form of an integer [0-59]\n")
            except KeyboardInterrupt:
                quit()
        # second
        while 1:
            second = input("Second [0-59]: ")
            try:
                second = int(second)
                if second > -1 and second < 60:
                    break
                else:
                    print("Second must be entered in the form of an second [0-59]\n")
            except ValueError:
                print("Second must be entered in the form of an second [0-59]\n")
            except KeyboardInterrupt:
                quit()
        try:
            submit_date = datetime.datetime(year, month, day, hour, minute, second)
            if submit_date and submit_date > now:
                break
            else:
                print("Invalid date entered\n")
        except ValueError:
            print("Invalid date entered\n")
        except KeyboardInterrupt:
            quit()

    # post delay

    confirmation = confirm_post()

    if confirmation == False:
        quit()
        
    while datetime.datetime.now() < submit_date: 
        print("Submission time: ", submit_date.strftime('%Y/%m/%d %H:%M:%S'))
        print("Current time: ", datetime.datetime.now().strftime('%Y/%m/%d %H:%M:%S'))
        print()
        try:
            time.sleep(1)
        except KeyboardInterrupt:
            quit()


# submits the post to the subreddit specified
def post(subname, title, selftext, url):
    if selftext:
        return reddit.subreddit(subname).submit(title, selftext=selftext)
    elif url:
        return reddit.subreddit(subname).submit(title, url=url)
    else:
        print("Error submitting post, Sorry!")
        quit()

def quit():
    print("\nRun the script again to create a new post. Bye!\n")
    exit()

# prints submission info
def print_submission(submission):
    print("-------------- Your Post --------------\n")
    print("Title: ", submission.title, " by ", submission.author)
    print("Subreddit: ", submission.subreddit)
    if submission.url:
        print("Link: ", submission.url)
    else:
        print("Text: ", submission.selftext)
    print("ID: ", submission.id)
    print("URL: ", submission.url)
    
def main():
    # get subreddit
    subname = get_sub()
    subreddit = reddit.subreddit(subname)

    # post submission parameters
    while 1:
        try:
            title = input("Title: ")
            if title:
                break
            else:
                print("Title cannot be empty\n")
        except KeyboardInterrupt:
            quit()
    
    # ensure selftext or url (not both)
    while 1:
        try:
            selftext = input("Self Text (leave empty for URL post): ")
            url = input("URL (leave empty for text post): ")
            if bool(selftext) ^ bool(url):
                break;
            else:
                print("Must input something for url or selftext, but not both\n")
        except KeyboardInterrupt:
            quit()

    # delay post check
    delay = optional_delay()
    
    confirmation = False
    
    if delay:
        delay_post()
        confirmation = True
    else:
        confirmation = confirm_post()

    if confirmation:
        submission = post(subname, title, selftext, url)
    else:
        quit()

    print_submission(submission)
    quit()
        
main()
