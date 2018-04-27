import random
import os
import sys
sys.path.append('..')
sys.path.append('../..')
import argparse
import utils
from student_utils_sp18 import *
from dijkstra import *
from os import listdir
from os.path import isfile, join
import pickle




def graph_creator(adjacency_matrix, number_of_kingdoms):
    edge_list = []
    for i in range(number_of_kingdoms):
        for j in range(i):
            weight = adjacency_matrix[i][j]
            if weight == "x":
                continue
            edge_list.append((i,j, weight))
    G = nx.Graph()
    nodelist = range(number_of_kingdoms)
    G.add_weighted_edges_from(edge_list, nodelist=nodelist)
    return G




# G = graph_creator(adjacency_matrix, number_of_kingdoms)
# print(all_pairs_dijkstra_path_length(G))
# print(all_pairs_dijkstra_path(G))

input_file_path = "./inputs"

# all_input_files = [f for f in listdir(input_file_path) if isfile(join(input_file_path, f))]

path_dict_name = "path_dict.p"
dist_dict_name = "dist_dict.p"

all_input_files = []
for i in range(726,753):
    all_input_files.append(str(i) + ".in")

for file_name in all_input_files:
	file_num = file_name.split(".")[0]
	input_data = utils.read_file(input_file_path + "/" + file_name)
	number_of_kingdoms, list_of_kingdom_names, starting_kingdom, adjacency_matrix = data_parser(input_data)
	source_index = list_of_kingdom_names.index(starting_kingdom)
	G = graph_creator(adjacency_matrix, number_of_kingdoms)
	path_dict = all_pairs_dijkstra_path(G)
	dist_dict = all_pairs_dijkstra_path_length(G)

	path_file_name = "./dict_poly2/shortest_path_dict/" + file_num + "_" + path_dict_name
	dist_file_name = "./dict_poly2/shortest_dist_dict/" + file_num + "_" + dist_dict_name

<<<<<<< HEAD
	pickle.dump( path_dict, open( path_file_name, "wb" ), protocol = 2 )
	pickle.dump( dist_dict, open( dist_file_name, "wb" ), protocol = 2 )
=======
	pickle.dump( path_dict, open( path_file_name, "wb"), protocol=2 )
	pickle.dump( dist_dict, open( dist_file_name, "wb"), protocol=2 ) 
>>>>>>> 915088b235ccd30a00de566715414e3ac17de5a0
	print(file_num, " done")





