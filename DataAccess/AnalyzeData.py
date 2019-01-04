import yaml
import datetime
import matplotlib.pyplot as plt

#storing the variables for plotting
dates_list = []
rtwt_count = []

# open for reading
with open("Dataset(oct18-oct17).txt", 'r') as dataset:

    # split every string ended with '\n' into a list of a string ['*']
    line_list = dataset.read().split('\n')

    end = ''

    for line in line_list:
        if line != end:
            # convert stringed dict into dict "*" -> {*:**}
            line_dict = yaml.load(line)
            # accessing the key
            # print(line_dict['created_at']," rtwt_count: ",
            #       line_dict['retweet_count']," fav_count: ",line_dict['favorite_count'],
            #       "reply_count: ",line_dict['reply_count'],
            #       " user_id: ",line_dict['user']["id"])

            dates_list.append(line_dict['created_at'])
            rtwt_count.append(line_dict['retweet_count'])
            # #check if key exist
            # if 'quoted_status' in line_dict:
            #     print("Quoted from:", "{ " ,line_dict['quoted_status']['created_at'],"",
            #           " rtwt_count: ",line_dict['quoted_status']['retweet_count'],
            #           " fav_count: ",line_dict['quoted_status']['favorite_count'],
            #           " reply_count: ",line_dict['quoted_status']['reply_count'],
            #           " user_id:",line_dict['quoted_status']['user']["id"], " }")
            #     print("")
            # else:
            #     print("")

        else:
            break

    # close the text file
    dataset.close()

############################################################################################

#this function takes a list of String of date in the format "Wed Aug 27 13:08:45 +0000 2008"
def getDate(date_list) :

    xlist = []

    for date in date_list:

        #split the whole string on whitespace (this is a list)
        date_split = date.split()
        #split time on ':' (this is a list)
        time_split = date_split[3].split(':')

        year   = int(date_split[5])
        month  = 10
        day    = int(date_split[2])

        hour   = int(time_split[0])
        minute = int(time_split[1])
        second = int(time_split[2])
        
        #convert dates into datetime for plotting
        x = datetime.datetime(year,month,day,hour,minute,second)

        xlist.append(x)

    return xlist

#get all the xvalue
dates = getDate(dates_list)

#plot
plt.plot(dates, rtwt_count)

plt.show()


