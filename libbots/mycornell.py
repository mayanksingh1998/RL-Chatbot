"""
Cornel Movies Dialogs Corpus
https://www.cs.cornell.edu/~cristian/Cornell_Movie-Dialogs_Corpus.html
"""
import os
import logging

from . import utils

log = logging.getLogger("cornell")
DATA_DIR = "data/my"
SEPARATOR = ":"


def load_dialogues(data_dir=DATA_DIR, genre_filter=''):
    """
    Load dialogues from cornell data
    :return: list of list of list of words
    """
    # movie_set = None
    # if genre_filter:
    #     movie_set = read_movie_set(data_dir, genre_filter)
    #     log.info("Loaded %d movies with genre %s", len(movie_set), genre_filter)
    log.info("Read and tokenise phrases...")
    lines = read_phrases(data_dir)
    # print(lines)
    # log.info("Loaded %d phrases", len(lines))
    # # print("done with load")
    dialogues = load_conversations(data_dir, lines)
    # print(dialogues)
    return dialogues


def iterate_entries(data_dir, file_name):
    with open(os.path.join(data_dir, file_name), "rb") as fd:
        for l in fd:
            l = str(l, encoding='utf-8', errors='ignore')
            yield list(map(str.strip, l.split(SEPARATOR)))


def read_movie_set(data_dir, genre_filter):
    res = set()
    for parts in iterate_entries(data_dir, "movie_titles_metadata.txt"):
        m_id, m_genres = parts[0], parts[5]
        if m_genres.find(genre_filter) != -1:
            res.add(m_id)
    return res


def read_phrases(data_dir, movies=None):
    res = {}
    for parts in iterate_entries(data_dir, "output.txt"):
        l_id, l_str = parts[0], parts[-1]
        # print(l_id)
        print("------------------------------lid")
        # print(m_id)
        # print("------------------------------lid")
        # print(l_str)
        print("------------------------------l]mid")
        # if movies and m_id not in movies:
        #     continue
        tokens = utils.tokenize(l_str)
        if tokens:
            res[l_id] = tokens
    # print(res)        
    return res

def load_conversations(data_dir, lines, movies=None):
    res = []
    dial_s_l=[]

    for parts in iterate_entries(data_dir, "output.txt"):
        m_id, dial_s = parts[0], parts[-1]
        # print("--------------------------------------++___")
        # print(dial_s)
        dial_s_l.append(dial_s)

        # print(dial_s)
        # for i in dial_s:
        #     print(dial_s)
        #     print("-----------------[")
        # if movies and m_id not in movies:
        #     continue
        # l_ids = dial_s.split(":")
        # l_ids = list(map(lambda s: s.strip("'"), l_ids))
        # dial = [lines[l_id] for l_id in l_ids if l_id in lines]
        # if dial:
        #     res.append(dial)
    # print(dial_s_l)
    # a = "i am mayank"
    # b = "you are sona"
    # al=[]
    # bl=[]
    # res2=[]
    # tokena = utils.tokenize(a)
    # tokenb = utils.tokenize(b)
    # res.append(tokena)
    # res.append(tokenb)
    resfinal=[]
    print("len of dial---------------sss")
    print(len(dial_s_l))
    for i in range(0,len(dial_s_l),2):
        res=[]
        a = utils.tokenize(dial_s_l[i])
        b = utils.tokenize(dial_s_l[i+1])
        res.append(a)
        res.append(b)
        resfinal.append(res)
    # res.append(al)
    # res.append(bl)
    # tok
    # for i in (dial_s_l):
    #     tokens = utils.tokenize(i)
    #     res.append(tokens)
    # res2.append(res)
    # print(resfinal)    
    return resfinal

# def load_conversations(data_dir, lines, movies=None):
#     res = []
#     count=0
#     for parts in iterate_entries(data_dir, "output.txt"):
#         m_id, dial_s = parts[0], parts[-1]
#         if movies and m_id not in movies:
#             continue

#         l_ids = dial_s.split(":")
#         # l_ids = list(map(lambda s: s.strip("'"), l_ids))
#         dial=[]

#         if count ==0 :


#             dial0 = [lines[l_id] for l_id in l_ids if l_id in lines]
#             count = 1
#             if dial0:
#                 dial.append(dial0)        

#         elif count == 1:
#             dial1 = [lines[l_id] for l_id in l_ids if l_id in lines]
#             count =0
#             if dial1: 
#                 dial.append(dial1)        
#             if dial:
#                 res.append(dial)
#         # if dial:
#             # print(dial)
#     # print(res)
#     return res


def read_genres(data_dir):
    res = {}
    for parts in iterate_entries(data_dir, "movie_titles_metadata.txt"):
        m_id, m_genres = parts[0], parts[5]
        l_genres = m_genres.strip("[]").split(", ")
        l_genres = list(map(lambda s: s.strip("'"), l_genres))
        res[m_id] = l_genres
    return res
