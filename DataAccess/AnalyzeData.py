import yaml

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
            print(line_dict['created_at']," rtwt_count: ",
                  line_dict['retweet_count']," fav_count: ",line_dict['favorite_count'],
                  " quote_count: ",line_dict['quote_count']," reply_count: ",line_dict['reply_count'],
                  " user_id: ",line_dict['user']["id"])

            #check if key exist
            if 'quoted_status' in line_dict:
                print("Quoted from:", "{ " ,line_dict['quoted_status']['created_at'],"",
                      " rtwt_count: ",line_dict['quoted_status']['retweet_count'],
                      " fav_count: ",line_dict['quoted_status']['favorite_count'],
                      " quote_count: ",line_dict['quoted_status']['quote_count'],
                      " reply_count: ",line_dict['quoted_status']['reply_count'],
                      " user_id:",line_dict['quoted_status']['user']["id"], " }")
                print("")
            else:
                print("")

        else:
            break

    # close the text file
    dataset.close()
