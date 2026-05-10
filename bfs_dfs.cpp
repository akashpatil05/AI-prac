#include <iostream>
#include <vector>
#include <queue>
using namespace std;

vector<int> graph[10];
bool visited[10];

// DFS
void DFS(int node)
{
    visited[node] = true;
    cout << node << " ";

    for (int i : graph[node])
    {
        if (!visited[i])
            DFS(i);
    }
}

// BFS
void BFS(int start)
{
    queue<int> q;
    q.push(start);
    visited[start] = true;

    while (!q.empty())
    {
        int node = q.front();
        q.pop();

        cout << node << " ";

        for (int i : graph[node])
        {
            if (!visited[i])
            {
                visited[i] = true;
                q.push(i);
            }
        }
    }
}

int main()
{
    // Undirected Graph
    graph[0].push_back(1);
    graph[1].push_back(0);

    graph[0].push_back(2);
    graph[2].push_back(0);

    graph[1].push_back(3);
    graph[3].push_back(1);

    cout << "DFS: ";
    DFS(0);

    // Reset visited array
    for (int i = 0; i < 10; i++)
        visited[i] = false;

    cout << "\nBFS: ";
    BFS(0);

    return 0;
}