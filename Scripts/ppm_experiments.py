from clustering_algorithms.spectral_clustering import *
from clustering_algorithms.louvain import *
from clustering_algorithms.paris import *
from dendrogram_manager.homogeneous_cut_slicer import *
from dendrogram_manager.heterogeneous_cut_slicer import *
from dendrogram_manager.distance_slicer import *
from experiments.flat_clustering_experiments_manager import *

SAVE_PLOTS = True
LOAD_RESULTS = True
SAVE_RESULTS = True
directory_results = "/home/sharp/Documents/Graphs/Graph_Clustering/Results/"
results_file_name = "ppm"
n_samples = 10

# List of tested algorihtms:
# - Spectral clustering
# - Louvain
# - Paris + homogenegeous cut
# - Paris + heterogeneous cut
# - Paris + distance cut + Louvain
# - Paris + distance cut + Louvain + spectral


def paris_homogeneous(G):
    D = paris(G)
    best_cut, best_score = best_homogeneous_cut(D)
    clusters = clustering_from_homogeneous_cut(D, best_cut)
    return clusters


def paris_heterogeneous(G):
    D = paris(G)
    best_cut, best_score = best_heterogeneous_cut(D)
    clusters = clustering_from_heterogeneous_cut(D, best_cut)
    return clusters


def paris_louvain(G):
    D = paris(G)
    best_dist, best_score = best_distance(D)
    clusters = louvain(G, 1/float(best_dist))
    return clusters


def paris_louvain_spectral_clustering(G):
    n_clusters = len(paris_louvain(G))
    clusters = spectral_clustering(G, n_clusters=n_clusters)
    return clusters

algorithms = [('Spectral Clustering - (25)', lambda G: spectral_clustering(G, n_clusters=25)),
              ('Spectral Clustering - (50)', lambda G: spectral_clustering(G, n_clusters=50)),
              ('Spectral Clustering - (75)', lambda G: spectral_clustering(G, n_clusters=75)),
              ('Louvain', louvain),
              ('Paris+homogeneous cut', paris_homogeneous),
              ('Paris+heterogeneous cut', paris_heterogeneous),
              ('Paris+Louvain', paris_louvain),
              ('Paris+Louvain+Spectral', paris_louvain_spectral_clustering)]

# print('Experiment: number of blocks')
# make_n_blocks_experiment(algorithms, range_n_blocks=range(10, 101, 10), block_size=10, d_in=5., d_out=1., n_samples=10, score=lambda true, pred: AMI(true, pred),
#                          SAVE_PLOTS=SAVE_PLOTS, LOAD_RESULTS=LOAD_RESULTS, SAVE_RESULTS=SAVE_RESULTS, directory_results=directory_results, results_file_name=results_file_name)
#
#
# print('Experiment: internal/external degree')
# make_degree_in_out_experiment(algorithms, d_in=5., range_d_out=np.linspace(1, 20, num=10), n_blocks=50, block_size=10, n_samples=10, score=lambda true, pred: AMI(true, pred),
#                               SAVE_PLOTS=SAVE_PLOTS, LOAD_RESULTS=LOAD_RESULTS, SAVE_RESULTS=SAVE_RESULTS, directory_results=directory_results, results_file_name=results_file_name)
#
# print('Experiment: block size heterogeneity')
# make_block_size_het_experiment(algorithms, range_param=np.linspace(1., 3., num=10), range_block_size=range(10, 100), n_blocks=50, p_in=.5, p_out=.01, n_samples=10, score=lambda true, pred: AMI(true, pred),
#                                SAVE_PLOTS=SAVE_PLOTS, LOAD_RESULTS=LOAD_RESULTS, SAVE_RESULTS=SAVE_RESULTS, directory_results=directory_results, results_file_name=results_file_name)
#
# print('Experiment: block size ratio')
# make_block_size_ratio_experiment(algorithms, range_ratio=range(1, 11), big_block_size=100, graph_size=600, p_in=.5, p_out=.01, n_samples=10, score=lambda true, pred: AMI(true, pred),
#                                    SAVE_PLOTS=SAVE_PLOTS, LOAD_RESULTS=LOAD_RESULTS, SAVE_RESULTS=SAVE_RESULTS, directory_results=directory_results, results_file_name=results_file_name)

print('Experiment: size of blocks')
make_block_size_experiment(algorithms, range_block_size=range(10, 101, 10), n_blocks=50, d_in=5., d_out=1., n_samples=10, score=lambda true, pred: AMI(true, pred),
                           SAVE_PLOTS=SAVE_PLOTS, LOAD_RESULTS=LOAD_RESULTS, SAVE_RESULTS=SAVE_RESULTS, directory_results=directory_results, results_file_name=results_file_name)
