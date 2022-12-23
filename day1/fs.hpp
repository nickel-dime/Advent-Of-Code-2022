// crea an graph representation in c++ using adjacecny lists
// and a function to print the graph

#ifndef FS_HPP
#define FS_HPP

#include <iostream>
#include <vector>
#include <list>
#include <string>
#include <fstream>
#include <sstream>
#include <algorithm>


using namespace std;

// graph representation using adjacency lists
class Graph {
    int V; // number of vertices
    vector<list<int>> adj; // adjacency lists
public:
    Graph(int V); // constructor
    void addEdge(int v, int w); // add an edge to the graph
    void printGraph(); // print the graph
};

// constructor
Graph::Graph(int V) {
    this->V = V;
    adj.resize(V);
}

// add an edge to the graph
void Graph::addEdge(int v, int w) {
    adj[v].push_back(w);
}

// print the graph
void Graph::printGraph() {
    for (int v = 0; v < V; v++) {
        cout << v << ": ";
        for (auto w : adj[v]) {
            cout << w << " ";
        }
        cout << endl;
    }
}

// read the graph from a file
Graph readGraph(string filename) {
    ifstream file(filename);
    string line;
    getline(file, line);
    int V = stoi(line);
    Graph g(V);
    while (getline(file, line)) {
        stringstream ss(line);
        int v, w;
        ss >> v;
        while (ss >> w) {
            g.addEdge(v, w);
        }
    }
    return g;
}

#endif
