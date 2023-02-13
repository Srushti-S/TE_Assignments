#include <iostream>
#include <list>
#include <map>
#include <queue>
using namespace std;

class GraphDFSBFS
{
public:
    map<int, list<int>> aList;
    map<int, bool> visited;
    queue<int> q;

    void Edge(int src, int dest)
    {
        aList[src].push_back(dest);
        aList[dest].push_back(src);
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

    void BFS()
    {
        if (q.empty())
        {
            return;
        }
        int node = q.front();
        q.pop();
        cout << node << " ";
        for (int i : aList[node])
        {
            if (!visited[i])
            {
                visited[i] = true;
                q.push(i);
            }
        }
        BFS();
    }
};

int main()
{
    GraphDFSBFS g;
    int n, s, d, ch;
    do
    {
        cout << "\n--------Menu----------";
        cout << "\n1. Create \n2. DFS \n3. BFS: \n4. Exit \nEnter your choice:";
        cin >> ch;
        if (ch == 1)
        {
            cout << "\nEnter total number of edges: ";
            cin >> n;
            for (int i = 0; i < n; i++)
            {
                cout << "\n\tEnter first vertex: ";
                cin >> s;
                cout << "\tEnter second vertex: ";
                cin >> d;
                g.Edge(s, d);
                g.Edge(d, s);
            }
        }
        else if (ch == 2)
        {
            cout << "\nDFS on the given graph is :";
            g.DFS(0);
        }
        else if (ch == 3)
        {
            cout << "\nBFS on the given graph is: ";
            g.q.push(0);
            g.visited[0] = true;
            g.BFS();
        }
        else
        {
            cout << "\nProgram exited successfully!";
        }
    } while (ch < 4);
    return 0;
}
