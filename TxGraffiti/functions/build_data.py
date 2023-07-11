from TxGraffiti.graph_data.functions.graph_calculator import calc, graph_property_check
from TxGraffiti.graph_data.functions.graph_property_names import invariant_names, property_names

import os
import grinpy as gp
import pandas as pd


def get_graph_data(G, name="G", invariants=invariant_names, properties=property_names):
    """
    Returns a dictionary of graph invariants and properties of a given graph G.

    Parameters
    ----------
    G : NetworkX graph
        An undirected graph.
    invariants : list of strings
        A list of graph invariants to be calculated for the graph G.
    properties : list of strings
        A list of graph properties to be checked for the graph G.

    Returns
    -------
    dict
        A dictionary of graph invariants and properties of the graph G.
    """
    data = {}
    data["name"] = name
    for invariant in invariants:
        data[invariant] = calc(G, invariant)
    for property in properties:
        data[property] = graph_property_check(G, property)
    return data

def get_graph_data_from_file(name, path="TxGraffiti/graph_data/small_connected", invariants=invariant_names, properties=property_names):
    """
    Returns a dictionary of graph invariants and properties of a given graph G.

    Parameters
    ----------
    filename : string
        The name of the file containing the graph G.
    invariants : list of strings
        A list of graph invariants to be calculated for the graph G.
    properties : list of strings
        A list of graph properties to be checked for the graph G.

    Returns
    -------
    dict
        A dictionary of graph invariants and properties of the graph G.
    """
    G = gp.read_edgelist(path + "/" + name + ".txt")
    return get_graph_data(G, name, invariants, properties)

def make_graph_dataframe(graphs, names, invariants=invariant_names, properties=property_names):
    """
    Returns a pandas dataframe of graph invariants and properties of a list of graphs.

    Parameters
    ----------
    graphs : list of NetworkX graphs
        A list of undirected graphs.
    invariants : list of strings
        A list of graph invariants to be calculated for the graphs.
    properties : list of strings
        A list of graph properties to be checked for the graphs.

    Returns
    -------
    pandas dataframe
        A pandas dataframe of graph invariants and properties of the graphs.
    """
    data = []
    for G, name in zip(graphs, names):
        data.append(get_graph_data(G, name, invariants, properties))
    return pd.DataFrame(data)

def get_graph_names(path):
    """
    Returns a list of graph names from a given path.

    Parameters
    ----------
    path : string
        The path to the directory containing the graphs.

    Returns
    -------
    list of strings
        A list of graph names.
    """
    return os.listdir(path)

def make_graph_data_csv(name="main", path="TxGraffiti/graph_data/small_connected", invariants=invariant_names, properties=property_names):
    """
    Returns a pandas dataframe of graph invariants and properties of a list of graphs.

    Parameters
    ----------
    path : string
        The path to the directory containing the graphs.
    invariants : list of strings
        A list of graph invariants to be calculated for the graphs.
    properties : list of strings
        A list of graph properties to be checked for the graphs.

    Returns
    -------
    pandas dataframe
        A pandas dataframe of graph invariants and properties of the graphs.
    """
    graph_names = get_graph_names(path)
    graphs = []
    for graph_name in graph_names:
        graphs.append(gp.read_edgelist(path + "/" + graph_name))
    df = make_graph_dataframe(graphs, graph_names, invariants, properties)
    df.set_index("name", inplace=True)
    df.to_csv(f"TxGraffiti/graph_data/{name}.csv")




