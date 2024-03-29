#include <iostream>
#include <queue>
#include <list>
#include <map>
using namespace std;

class Graph 
{
public:
    map<int, list<int>> aList;
    map<int, bool> visited;

    void addEdge(int src, int dest) 
    {
        aList[src].push_back(dest);
    }

    void DFS(int node) 
    {
        visited[node] = true;
        cout << node << " ";
        for (int i : aList[node]) 
        {
            if (!visited[i]) 
            {
                DFS(i);
            }
        }
    }
   
   void BFS(int node) 
   {
        visited[node] = true;
        cout << node << " ";
        BFSUtil(node);
    }

    void BFSUtil(int node) 
    {
        queue<int> q;
        for (int i : aList[node]) 
        {
            if (!visited[i]) 
            {
                visited[i] = true;
                q.push(i);
                cout << i << " ";
            }
        }
        while (!q.empty()) 
        {
            int nextNode = q.front();
            q.pop();
            BFSUtil(nextNode);
        }
    }    
};

int main() 
{
    Graph g;
    int n, src, dest;
    
    cout << "Enter the number of edges: ";
    cin >> n;

    cout << "Enter the edges (source destination):\n";
    for (int i = 0; i < n; i++) 
    {
        cin >> src >> dest;
        g.addEdge(src, dest);
    }

    int startNode;
    cout << "Enter the starting node: ";
    cin >> startNode;

    cout << "DFS traversal: ";
    g.DFS(startNode);
    cout << endl;

    cout << "BFS traversal: ";
    g.visited.clear();
    g.BFS(startNode);
    cout << endl;

    return 0;
}
