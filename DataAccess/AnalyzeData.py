import yaml
import datetime
import networkx as nx
import matplotlib.pyplot as plt

# storing the variables for plotting
dates_list = []
rtwt_count = []
idA_list = []
idB_list = []

num_twt = 0
num_links = 0

############################################################################################
# open dataset for reading
with open("fullOct18.txt", 'r') as dataset:
    # split every string ended with '\n' into a list of a string ['*']
    line_list = dataset.read().split('\n')

    end = ''

    for line in line_list:
        if line != end:

            # count the number of tweets
            num_twt = num_twt + 1

            # convert stringed dict into dict "*" -> {*:**}
            line_dict = yaml.load(line)

            # accessing the key
            # print(line_dict['created_at'],)

            # extract the dates for plotting value (x)
            dates_list.append(line_dict['created_at'])
            # extract the rtwt count for plotting value (y)
            rtwt_count.append(line_dict['retweet_count'])

            # check if link exist
            if 'quoted_status' in line_dict:
                # count the number of links
                num_links = num_links + 1

                idA = line_dict['quoted_status']['user']["id"]
                idA_list.append(str(idA))

                idB = line_dict['user']["id"]
                idB_list.append(str(idB))

        else:
            break

    # close the text file
    dataset.close()


############################################################################################
# this function takes a list of String of vals and write it in text file
def writeText(list1, path):
    dataset = open(path, 'w')

    # pull out 100 Tweets from Wed Feb 28 23:58:46 +0000 2018 to Wed Feb 28 13:07:51 +0000 2018
    for val in list1:
        dataset.write('"' + val + '", ')

    # close the text file
    dataset.close()


############################################################################################
# this function takes a list of String of date in the format "Wed Aug 27 13:08:45 +0000 2008"
def getDate(date_list):
    xlist = []

    for date in date_list:
        # split the whole string on whitespace (this is a list)
        date_split = date.split()
        # split time on ':' (this is a list)
        time_split = date_split[3].split(':')

        year = int(date_split[5])
        # since only in October(13,14,15,16,17,18)
        month = 10
        day = int(date_split[2])

        hour = int(time_split[0])
        minute = int(time_split[1])
        second = int(time_split[2])

        x = datetime.datetime(year, month, day, hour, minute, second)
        xlist.append(x)

    return xlist


############################################################################################
# this function takes id, idList, the current element position of idList and return status string
def checkId(id, idList, linkNum):
    for x in range(linkNum):

        if x == 0:
            print('')

        if id == idList[x]:
            print(id)
            print(idList[x])
            return 'existed'

    return 'none'


############################################################################################
# plotting the Network function
def plotNetwork(listA, listB):

    nodeID = 0
    fullid_list = listA + listB
    itter = len(fullid_list)

    G = nx.DiGraph()

    for x in range(itter):

        print("iteration: ", x)

        # create nodes
        G.add_node(fullid_list[x], id = fullid_list[x])
        nodeID = nodeID + 1
        print(G.number_of_nodes())
        idDict = nx.get_node_attributes(G, 'id')
        print(idDict)
        print('')

    return G

############################################################################################
#set the plot Edges
def setEdges(graph,numLink,listA,listB):

     for x in range(numLink):
         graph.add_edge(listA[x],listB[x])


############################################################################################


G = plotNetwork(idA_list, idB_list)
setEdges(G,num_links,idA_list,idB_list)
print(G.edges())

#save the network as .gexf file and read it with Gephi tool
nx.write_gexf(G, "file.gexf", version="1.2draft")
