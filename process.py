#!/usr/bin/env python
 # -*- coding: utf-8 -*-

import os
import string
import json
import sys
import csv
from datetime import datetime
from collections import defaultdict

from mandrillEmailSender import sendEmails

from utils import dbgInfo, dbgWarn, dbgErr, dbgFatal, DBG
import utils
utils.DBG = False
DBG = False
uploadDir = 'app/uploads/'
csvfilenames = ["communityFile", "memberFile", "servicesFile" ]
inputcsv = [ uploadDir + filename for filename in csvfilenames ]
#inputcsv = [ filename + ".csv" for filename in inputcsv ]
#return inputcsv[0], inputcsv[1], inputcsv[2]

def get_file_names():
    ''' Gets the names of required csv files '''
    member_file = raw_input("Enter name of csv file with member details (with .csv): ")
    comm_file = raw_input("Enter name of csv file with member to community details (with .csv): ")
    offer_file = raw_input("Enter name of csv file with offer details (with .csv): ")
    return member_file, comm_file, offer_file

def is_expired(date):
    ''' Return 1 if the passed datetime object is beyond now '''
    pat = '%m/%d/%Y %H:%M'
    now = datetime.now()
    try:
        expiry = datetime.strptime(date, pat) # 1/6/2014 22:00
    except ValueError:
        expiry = datetime.strptime(date, '%m/%d/%y %H:%M') # 1/6/2014 22:00
    return expiry < now # return 1 if expiry date is before now

def get_member_dict(member_file):
    ''' Returns the dict containing all member information from members csv
    file'''
    data = defaultdict(lambda: defaultdict(lambda: 'filler')) # {userid: {firstname, email}}
    with open(member_file, 'rb') as f:
        read = csv.reader(f)
        next(read, None) # skip the header
        for row in read:
            # user id = row[1], f_name = row[4], email = row[3]
            if row[16] is not 'Opt out of messages':
                if row[4] is not '' and row[3] is not '':
                    user_id = int(row[1])
                    data[user_id]["first"] = row[4]
                    data[user_id]["email"] = row[3]
    return data

def get_comm_dict(comm_file):
    ''' Returns a dict containing community data for each user '''
    data = defaultdict(lambda: 'filler') # {userid: community}
    with open(comm_file, 'rb') as f:
        read = csv.reader(f)
        next(read, None) # skip the header
        for row in read:
            # user id = row[0], community = row[2]
            data[int(row[0])] = row[2]
    return data

def remove_bad_characters(yourstring):
    DELETE_CHARS = False
    if DELETE_CHARS:    # delete chars but has bug where it also deletes some spaces
        # this works well but removes some spaces next to bad chars for some reason
        return "".join(i for i in yourstring if ord(i)<128)
    else:
        chars_to_delete = ['â', '€', '™', 'Â']
        #chars_to_delete = "Ââ€™"
        #yourstring = unicode(yourstring, 'utf-8')
        #yourstring = unicode(yourstring, 'utf-8').encode('ascii', 'ignore')

        for c in chars_to_delete:
            yourstring = yourstring.replace(c, '')

        return yourstring.strip()

    # translate's deletechars argument cannot exist for unicode
    #return yourstring.translate(None, chars_to_delete).strip()
    
def get_ads(offer_file):
    ''' Builds up dicts for offers and requests in the ads csv file '''
    offers = defaultdict(lambda: defaultdict(lambda: 'filler')) # {ad_id: {details.}}
    requests = defaultdict(lambda: defaultdict(lambda: 'filler'))
    with open(offer_file, 'rb') as f:
        # id = row[1], type = row[2], f_name = row[6], cat = row[11],
        # expiry = row[13], url = row[14], title = row[15], body = row[16]
        read = csv.reader(f)
        next(read, None) # skip the header
        for row in read:
            dbgInfo( "row[1]:", row[1] )
            #row = unicode(row)
            try:
                ad_id = int(row[1])
                dbgInfo("ad_id", ad_id)
            except ValueError as e:
                dbgErr("Value error for row:", type(row))
                dbgErr("Exception:", e)
                continue
            expiry = row[13]
            dbgInfo("expiry", row[13])
            if not is_expired(expiry):
                ad_type = row[2]
                if ad_type == 'Offer':
                    offers[ad_id]["first"] = remove_bad_characters(row[6])
                    offers[ad_id]["category"] = remove_bad_characters(row[11])
                    offers[ad_id]["expiry"] = expiry
                    offers[ad_id]["url"] = row[14]
                    offers[ad_id]["title"] = remove_bad_characters(row[15])
                    offers[ad_id]["body"] = remove_bad_characters(row[16])
                    offers[ad_id]["lastUpdated"] = row[10]
                    offers[ad_id]["id"] = row[1]
                    offers[ad_id]["type"] = row[2]
                    dbgInfo( "offer body: " + offers[ad_id]['body'] )
                elif ad_type == 'Request':
                    requests[ad_id]["first"] = remove_bad_characters(row[6])
                    requests[ad_id]["category"] = remove_bad_characters(row[11])
                    requests[ad_id]["expiry"] = expiry
                    requests[ad_id]["url"] = row[14]
                    requests[ad_id]["title"] = remove_bad_characters(row[15])
                    requests[ad_id]["body"] = remove_bad_characters(row[16])
                    requests[ad_id]["lastUpdated"] = row[10]
                    requests[ad_id]["id"] = row[1]
                    requests[ad_id]["type"] = row[2]
                    dbgInfo( "request body: " + requests[ad_id]['body'] )
    return offers, requests
    
def combine_member_data(member_data, comm_data):
    ''' Combines the data in two dicts using user_id as primary key '''
    comm_keys = comm_data.keys() # add user id's in comm_data file
    for user_id in member_data.keys():
        if user_id in comm_keys:
            member_data[user_id]["community"] = comm_data[user_id]
    return member_data

if __name__ == '__main__':
    #member_file, comm_file, offer_file = get_file_names()
    member_file, comm_file, offer_file = sys.argv[2], sys.argv[1], sys.argv[3]
    member_data = get_member_dict(member_file)
    comm_data = get_comm_dict(comm_file)
    offers, requests = get_ads(offer_file)
    dbgInfo( "Offers: ", offers.keys() )
    print "\n\n"
    dbgInfo( "Requests: ", requests.keys() )
    full_member_data = combine_member_data(member_data, comm_data)

    TEST_FRONTEND = True
    if TEST_FRONTEND:
        f = open(inputcsv[1] + ".json", 'w')
        f.write( json.dumps( full_member_data ) );
        f.close()
        print "(process.py) wrote file", inputcsv[1] + ".json"

        f = open(inputcsv[2] + "-offers.json", 'w')
        f.write( json.dumps( offers ) );
        f.close()
        print "(process.py) wrote file", inputcsv[2] + "-offers.json"

        f = open(inputcsv[2] + "-requests.json", 'w')
        f.write( json.dumps( requests ) );
        f.close()
        print "(process.py) wrote file", inputcsv[2] + "-requests.json"

        f = open(inputcsv[2] + "-all.json", 'w')
        #f.write( json.dumps( offers.viewitems() & requests.viewitems() ) );
        all_ads = dict()    # combine requests and offers
        all_ads.update(offers)
        all_ads.update(requests)

        all_ads_array = []  # turn into array for easier sorting in angularjs
        for key in all_ads:
            all_ads_array.append(all_ads[key])

        f.write( json.dumps(all_ads_array) )
        #f.write( json.dumps(offers) + json.dumps(requests) );
        f.close()
        print "(process.py) wrote file", inputcsv[2] + "-all.json"
    
    fromAddress = 'dasher@tbanks.org' # May be taken as input 
    subject = 'Offers of the Day'   
    curdir = os.getcwd()
    #rootdir = os.path.join(curdir, '..')
    assetdir = os.path.join(curdir, 'assets')
    emailHtml = file(os.path.join(assetdir, 'emailtemplate.html')).read()
    emailText = file(os.path.join(assetdir, 'emailtemplate.txt')).read()
    offerText = offerHtml = ''
    reqText = reqHtml = ''
    offer_ids = offers.keys()
    offer_ids.sort(reverse=True)
    request_ids = requests.keys()
    request_ids.sort(reverse=True)
    numOffers = 10 if len(offer_ids) >= 10 else len(offer_ids)
    numRequests = 10 if len(request_ids) >= 10 else len(request_ids)
    
    for i in range(numOffers):
        offer = offer_ids[i]
        offerTitle = offers[offer]['title']
        offerUrl = offers[offer]['url']
        offerText += offerTitle + '\n'
        offerHtml += '<li> <a href="' + offerUrl + '">' + offerTitle + ' </a></li>'
    for i in range(numRequests):
        request = request_ids[i]
        reqTitle = requests[request]['title']
        reqUrl = requests[request]['url']
        reqText += reqTitle + '\n'
        reqHtml += '<li> <a href="' + reqUrl + '">' + reqTitle + ' </a></li>'
    
    emailHtml = emailHtml.replace('{{list_of_new_requests}}', reqHtml)
    emailText = emailText.replace('{{list_of_new_requests}}', reqText)
    emailHtml = emailHtml.replace('{{list_of_new_offers}}', offerHtml)
    emailText = emailText.replace('{{list_of_new_offers}}', offerText)
    print "\nRequests:", emailText
    #sendEmails(subject, fromAddress, emailHtml, emailText, full_member_data)
    
