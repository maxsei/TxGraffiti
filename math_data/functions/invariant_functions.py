import grinpy as gp
from sympy import divisors, totient, mobius, primefactors, isprime

__all__ = ["calc", "property_check"]


def calc(G, invariant):
    """
    Returns the value of a given graph invariant for a given graph G.

    Parameters
    ----------
    G : NetworkX graph
        An undirected graph.
    invariant : string
        The name of the graph invariant to be calculated for the graph G.

    Returns
    -------
    int
        The value of the graph invariant for the graph G.
    """
    if invariant == "k_slater_index":
        return k_slater_index(G)
    elif invariant == "vertex_cover_number":
        return vertex_cover_number(G)
    elif invariant == "k_residual_index":
        return k_residual_index(G)
    elif invariant == "order":
        return gp.number_of_nodes(G)
    elif invariant == "size":
        return gp.number_of_edges(G)
    elif invariant == "(order - domination_number)":
        return gp.number_of_nodes(G) - gp.domination_number(G)
    elif invariant == "(order - total_domination_number)":
        return gp.number_of_nodes(G) - gp.total_domination_number(G)
    elif invariant == "(order - connected_domination_number)":
        return gp.number_of_nodes(G) - gp.connected_domination_number(G)
    elif invariant == "(order - independence_number)":
        return gp.number_of_nodes(G) - gp.independence_number(G)
    elif invariant == "(order - power_domination_number)":
        return gp.number_of_nodes(G) - gp.power_domination_number(G)
    elif invariant == "(order - zero_forcing_number)":
        return gp.number_of_nodes(G) - gp.zero_forcing_number(G)
    elif invariant == "(order - diameter)":
        return gp.number_of_nodes(G) - gp.diameter(G)
    elif invariant == "(order - radius)":
        return gp.number_of_nodes(G) - gp.radius(G)
    elif invariant == "(order - independent_domination_number)":
        return gp.number_of_nodes(G) - gp.independent_domination_number(G)
    elif invariant == "(order - chromatic_number)":
        return gp.number_of_nodes(G) - gp.chromatic_number(G)
    elif invariant == "(order - matching_number)":
        return gp.number_of_nodes(G) - gp.matching_number(G)
    elif invariant == "(order - min_maximal_matching_number)":
        return gp.number_of_nodes(G) - gp.min_maximal_matching_number(G)
    elif invariant == "(order - triameter)":
        return gp.number_of_nodes(G) - gp.triameter(G)
    elif invariant == "(order - min_degree)":
        return gp.number_of_nodes(G) - gp.min_degree(G)
    elif invariant == "(order - max_degree)":
        return gp.number_of_nodes(G) - gp.max_degree(G)
    elif invariant == "(order - clique_number)":
        return gp.number_of_nodes(G) - gp.clique_number(G)
    elif invariant == "(order - residue)":
        return gp.number_of_nodes(G) - gp.residue(G)
    elif invariant == "(order - annihilation_number)":
        return gp.number_of_nodes(G) - gp.annihilation_number(G)
    elif invariant == "(order - sub_total_domination_number)":
        return gp.number_of_nodes(G) - gp.sub_total_domination_number(G)
    elif invariant == "(order - slater)":
        return gp.number_of_nodes(G) - gp.slater(G)
    elif invariant == "(order - k_slater_index)":
        return gp.number_of_nodes(G) - k_slater_index(G)
    elif invariant == "(order - k_residual_index)":
        return gp.number_of_nodes(G) - k_residual_index(G)
    elif invariant == "order_number_of_divisors":
        return order_number_of_divisors(G)
    elif invariant == "order_sum_of_divisors":
        return order_sum_of_divisors(G)
    elif invariant == "order_euler_totient":
        return order_euler_totient(G)
    elif invariant == "order_mobius_function":
        return order_mobius_function(G)
    elif invariant == "order_sum_of_proper_divisors":
        return order_sum_of_proper_divisors(G)
    elif invariant == "order_sum_of_digits":
        return order_sum_of_digits(G)
    elif invariant == "order_product_of_digits":
        return order_product_of_digits(G)
    elif invariant == "order_number_of_prime_factors":
        return order_number_of_prime_factors(G)
    elif invariant == "order_number_of_distinct_prime_factors":
        return order_number_of_distinct_prime_factors(G)
    elif invariant == "independence_number_of_divisors":
        return independence_number_of_divisors(G)
    elif invariant == "independence_sum_of_divisors":
        return independence_sum_of_divisors(G)
    elif invariant == "independence_euler_totient":
        return independence_euler_totient(G)
    elif invariant == "independence_mobius_function":
        return independence_mobius_function(G)
    elif invariant == "independence_sum_of_proper_divisors":
        return independence_sum_of_proper_divisors(G)
    elif invariant == "independence_sum_of_digits":
        return independence_sum_of_digits(G)
    elif invariant == "independence_product_of_digits":
        return independence_product_of_digits(G)
    elif invariant == "independence_number_of_prime_factors":
        return independence_number_of_prime_factors(G)
    elif invariant == "independence_number_of_distinct_prime_factors":
        return independence_number_of_distinct_prime_factors(G)
    elif invariant == "matching_number_of_divisors":
        return matching_number_of_divisors(G)
    elif invariant == "matching_sum_of_divisors":
        return matching_sum_of_divisors(G)
    elif invariant == "matching_euler_totient":
        return matching_euler_totient(G)
    elif invariant == "matching_mobius_function":
        return matching_mobius_function(G)
    elif invariant == "matching_sum_of_proper_divisors":
        return matching_sum_of_proper_divisors(G)
    elif invariant == "matching_sum_of_digits":
        return matching_sum_of_digits(G)
    elif invariant == "matching_product_of_digits":
        return matching_product_of_digits(G)
    elif invariant == "matching_number_of_prime_factors":
        return matching_number_of_prime_factors(G)
    elif invariant == "matching_number_of_distinct_prime_factors":
        return matching_number_of_distinct_prime_factors(G)
    elif invariant == "zero_forcing_number_of_divisors":
        return zero_forcing_number_of_divisors(G)
    elif invariant == "zero_forcing_sum_of_divisors":
        return zero_forcing_sum_of_divisors(G)
    elif invariant == "zero_forcing_euler_totient":
        return zero_forcing_euler_totient(G)
    elif invariant == "zero_forcing_mobius_function":
        return zero_forcing_mobius_function(G)
    elif invariant == "zero_forcing_sum_of_proper_divisors":
        return zero_forcing_sum_of_proper_divisors(G)
    elif invariant == "zero_forcing_sum_of_digits":
        return zero_forcing_sum_of_digits(G)
    elif invariant == "zero_forcing_product_of_digits":
        return zero_forcing_product_of_digits(G)
    elif invariant == "zero_forcing_number_of_prime_factors":
        return zero_forcing_number_of_prime_factors(G)
    elif invariant == "zero_forcing_number_of_distinct_prime_factors":
        return zero_forcing_number_of_distinct_prime_factors(G)
    elif invariant == "domination_number_of_divisors":
        return domination_number_of_divisors(G)
    elif invariant == "domination_sum_of_divisors":
        return domination_sum_of_divisors(G)
    elif invariant == "domination_euler_totient":
        return domination_euler_totient(G)
    elif invariant == "domination_mobius_function":
        return domination_mobius_function(G)
    elif invariant == "domination_sum_of_proper_divisors":
        return domination_sum_of_proper_divisors(G)
    elif invariant == "domination_sum_of_digits":
        return domination_sum_of_digits(G)
    elif invariant == "domination_product_of_digits":
        return domination_product_of_digits(G)
    elif invariant == "domination_number_of_prime_factors":
        return domination_number_of_prime_factors(G)
    elif invariant == "domination_number_of_distinct_prime_factors":
        return domination_number_of_distinct_prime_factors(G)
    elif invariant == "min_edge_cover":
        return len(gp.min_edge_cover(G))
    elif invariant == "[(annihilation_number + residue)/ max_degree]":
        return (gp.annihilation_number(G) + gp.residue(G)) / gp.max_degree(G)
    elif invariant == "[order/ max_degree]":
        return gp.number_of_nodes(G) / gp.max_degree(G)
    elif invariant == "[order/ (max_degree + 1)]":
        return gp.number_of_nodes(G) / (gp.max_degree(G) + 1)
    elif invariant == "[order/ (max_degree - 1)]":
        return gp.number_of_nodes(G) / (gp.max_degree(G) - 1)
    else:
        return getattr(gp, invariant)(G)


def property_check(G, property):
    """
    Returns True if a given graph G has a given graph property, and False otherwise.

    Parameters
    ----------
    G : NetworkX graph
        An undirected graph.
    property : string
        The name of the graph property to be checked for the graph G.

    Returns
    -------
    bool
        True if the graph G has the given property, and False otherwise.
    """
    if property == "a connected graph":
        return gp.is_connected(G)
    elif property == "a connected and planar graph":
        return gp.is_connected(G) and gp.check_planarity(G)[0]
    elif property == "a connected and regular graph":
        return gp.is_connected(G) and gp.min_degree(G) == gp.max_degree(G)
    elif property == "a connected and cubic graph":
        return gp.is_connected(G) and gp.min_degree(G) == 3 and gp.max_degree(G) == 3
    elif property == "a connected graph which is not K_n":
        return gp.is_connected(G) and gp.is_isomorphic(G, gp.complete_graph(gp.number_of_nodes(G))) == False
    elif property == "a connected and triangle-free graph":
        return gp.is_connected(G) and set(gp.triangles(G).values()) == {0}
    elif property == "a connected and claw-free graph":
        return gp.is_connected(G) and gp.is_claw_free(G)
    elif property == "a connected and chordal graph":
        return gp.is_connected(G) and gp.is_chordal(G)
    elif property == "a tree graph":
        return gp.is_connected(G) and gp.is_tree(G)
    elif property == "a connected and at-free graph":
        return gp.is_connected(G) and gp.is_at_free(G)
    elif property == "an eulerian graph":
        return gp.is_connected(G) and gp.is_eulerian(G)
    elif property == "a connected and bipartite graph":
        return gp.is_connected(G) and gp.is_bipartite(G)
    elif property == "a connected graph with maximum degree at most 3":
        return gp.is_connected(G) and gp.max_degree(G) <= 3
    elif property == "a connected graph which is not K_n and has maximum degree at most 3":
        return gp.is_connected(G) and gp.is_isomorphic(G, gp.complete_graph(gp.number_of_nodes(G))) == False and gp.max_degree(G) <= 3
    elif property == "a connected and cubic graph which is not K_4":
        return gp.is_connected(G) and gp.is_isomorphic(G, gp.complete_graph(gp.number_of_nodes(G))) == False and gp.min_degree(G) == 3 and gp.max_degree(G) == 3
    elif property == "a connected, claw-free, and cubic graph":
        return gp.is_connected(G) and gp.min_degree(G) == 3 and gp.max_degree(G) == 3 and gp.is_claw_free(G)
    elif property == "a connected, planar, and cubic graph":
        return gp.is_connected(G) and gp.min_degree(G) == 3 and gp.max_degree(G) == 3 and gp.is_planar(G)
    elif property == "a connected graph with a prime number of vertices":
        return gp.is_connected(G) and isprime(gp.number_of_nodes(G))
    elif property == "a connected graph with a prime number of edges":
        return gp.is_connected(G) and isprime(gp.number_of_edges(G))
    elif property == "a connected graph with a prime independence number":
        return gp.is_connected(G) and isprime(gp.independence_number(G))
    elif property == "a connected graph with a prime diameter":
        return gp.is_connected(G) and isprime(gp.diameter(G))
    elif property == "a connected graph with a prime zero forcing number":
        return gp.is_connected(G) and isprime(gp.zero_forcing_number(G))
    elif property == "a connected graph with a prime total domination number":
        return gp.is_connected(G) and isprime(gp.total_domination_number(G))
    elif property == "a connected graph with a prime domination number":
        return gp.is_connected(G) and isprime(gp.domination_number(G))
    elif property == "a connected graph with a total domination number equal to the domination number":
        return gp.is_connected(G) and gp.total_domination_number(G) == gp.domination_number(G)
    elif property == "a connected graph with a prime matching number":
        return gp.is_connected(G) and isprime(gp.matching_number(G))
    elif property == "a connected graph with a prime residue":
        return gp.is_connected(G) and isprime(gp.residue(G))
    elif property == "a connected and well-covered graph":
        return gp.is_connected(G) and gp.independence_number(G) == gp.independent_domination_number(G)
    elif property == "a connected and Class-1 graph":
        new_G = gp.line_graph(G)
        return gp.is_connected(G) and gp.chromatic_number(new_G) == gp.max_degree(G)
    elif property == "a connected and Class-2 graph":
        new_G = gp.line_graph(G)
        return gp.is_connected(G) and gp.chromatic_number(new_G) == gp.max_degree(G) + 1
    elif property == "a connected graph with diameter at most 3":
        return gp.is_connected(G) and gp.diameter(G) <= 3
    elif property == "a connected and planar graph with diameter at most 3":
        return gp.is_connected(G) and gp.is_planar(G) and gp.diameter(G) <= 3
    else:
        return getattr(gp, property)(G)


def k_slater_index(G):
    """Return a the smallest integer k so that the sub-k-domination number
    of G is at least the domination number of G.
    Parameters
    ----------
    G : NetworkX graph
        An undirected graph.
    Returns
    -------
    number
        The smallest ineteger k such that gp.domination_number(G) <= gp.sub_k_domination_number(G, k).
    """
    k = 1
    while gp.sub_k_domination_number(G, k) < gp.domination_number(G):
        k += 1
    return k

def vertex_cover_number(G):
    """Return a the size of smallest vertex cover in the graph G.
    Parameters
    ----------
    G : NetworkX graph
        An undirected graph.
    Returns
    -------
    number
        The size of a smallest vertex cover of G.
    """
    return gp.number_of_nodes(G) - gp.independence_number(G)

def k_residual_index(G):
    """Return a the smallest integer k so that the k-residue of G is at least the
    independence number of G.
    Parameters
    ----------
    G : NetworkX graph
        An undirected graph.
    Returns
    -------
    number
        The smallest ineteger k such that gp.independence_number(G) <= gp.k_residue(G, k).

    """
    k = 1
    while gp.k_residue(G, k) < gp.independence_number(G):
        k += 1
    return k

from sympy import divisors, totient, mobius, primefactors

def prod(iterable):
    p = 1
    for n in iterable:
        p *= n
    return p


# Define our functions
def order_number_of_divisors(G):
    n = gp.number_of_nodes(G)
    return len(divisors(n))

def order_sum_of_divisors(G):
    n = gp.number_of_nodes(G)
    return sum(divisors(n))

def order_euler_totient(G):
    n = gp.number_of_nodes(G)
    return totient(n)

def order_mobius_function(G):
    n = gp.number_of_nodes(G)
    return mobius(n)

def order_sum_of_proper_divisors(G):
    n = gp.number_of_nodes(G)
    return sum(divisors(n)) - n

def order_sum_of_digits(G):
    n = gp.number_of_nodes(G)
    return sum(int(digit) for digit in str(n))

def order_product_of_digits(G):
    n = gp.number_of_nodes(G)
    return prod(int(digit) for digit in str(n))

def order_number_of_prime_factors(G):
    n = gp.number_of_nodes(G)
    return len(primefactors(n))

def order_number_of_distinct_prime_factors(G):
    n = gp.number_of_nodes(G)
    return len(set(primefactors(n)))


# Independence number functions
def independence_number_of_divisors(G):
    n = gp.independence_number(G)
    return len(divisors(n))

def independence_sum_of_divisors(G):
    n = gp.independence_number(G)
    return sum(divisors(n))

def independence_euler_totient(G):
    n = gp.independence_number(G)
    return totient(n)

def independence_mobius_function(G):
    n = gp.independence_number(G)
    return mobius(n)

def independence_sum_of_proper_divisors(G):
    n = gp.independence_number(G)
    return sum(divisors(n)) - n

def independence_sum_of_digits(G):
    n = gp.independence_number(G)
    return sum(int(digit) for digit in str(n))

def independence_product_of_digits(G):
    n = gp.independence_number(G)
    return prod(int(digit) for digit in str(n))

def independence_number_of_prime_factors(G):
    n = gp.independence_number(G)
    return len(primefactors(n))

def independence_number_of_distinct_prime_factors(G):
    n = gp.independence_number(G)
    return len(set(primefactors(n)))

# Matching number functions
def matching_number_of_divisors(G):
    n = gp.matching_number(G)
    return len(divisors(n))

def matching_sum_of_divisors(G):
    n = gp.matching_number(G)
    return sum(divisors(n))

def matching_euler_totient(G):
    n = gp.matching_number(G)
    return totient(n)

def matching_mobius_function(G):
    n = gp.matching_number(G)
    return mobius(n)

def matching_sum_of_proper_divisors(G):
    n = gp.matching_number(G)
    return sum(divisors(n)) - n

def matching_sum_of_digits(G):
    n = gp.matching_number(G)
    return sum(int(digit) for digit in str(n))

def matching_product_of_digits(G):
    n = gp.matching_number(G)
    return prod(int(digit) for digit in str(n))

def matching_number_of_prime_factors(G):
    n = gp.matching_number(G)
    return len(primefactors(n))

def matching_number_of_distinct_prime_factors(G):
    n = gp.matching_number(G)
    return len(set(primefactors(n)))

# Zero forcing number functions
def zero_forcing_number_of_divisors(G):
    n = gp.zero_forcing_number(G)
    return len(divisors(n))

def zero_forcing_sum_of_divisors(G):
    n = gp.zero_forcing_number(G)
    return sum(divisors(n))

def zero_forcing_euler_totient(G):
    n = gp.zero_forcing_number(G)
    return totient(n)

def zero_forcing_mobius_function(G):
    n = gp.zero_forcing_number(G)
    return mobius(n)

def zero_forcing_sum_of_proper_divisors(G):
    n = gp.zero_forcing_number(G)
    return sum(divisors(n)) - n

def zero_forcing_sum_of_digits(G):
    n = gp.zero_forcing_number(G)
    return sum(int(digit) for digit in str(n))

def zero_forcing_product_of_digits(G):
    n = gp.zero_forcing_number(G)
    return prod(int(digit) for digit in str(n))

def zero_forcing_number_of_prime_factors(G):
    n = gp.zero_forcing_number(G)
    return len(primefactors(n))

def zero_forcing_number_of_distinct_prime_factors(G):
    n = gp.zero_forcing_number(G)
    return len(set(primefactors(n)))

# Domination number functions
def domination_number_of_divisors(G):
    n = gp.domination_number(G)
    return len(divisors(n))

def domination_sum_of_divisors(G):
    n = gp.domination_number(G)
    return sum(divisors(n))

def domination_euler_totient(G):
    n = gp.domination_number(G)
    return totient(n)

def domination_mobius_function(G):
    n = gp.domination_number(G)
    return mobius(n)

def domination_sum_of_proper_divisors(G):
    n = gp.domination_number(G)
    return sum(divisors(n)) - n

def domination_sum_of_digits(G):
    n = gp.domination_number(G)
    return sum(int(digit) for digit in str(n))

def domination_product_of_digits(G):
    n = gp.domination_number(G)
    return prod(int(digit) for digit in str(n))

def domination_number_of_prime_factors(G):
    n = gp.domination_number(G)
    return len(primefactors(n))

def domination_number_of_distinct_prime_factors(G):
    n = gp.domination_number(G)
    return len(set(primefactors(n)))






