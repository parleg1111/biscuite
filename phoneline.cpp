/*
----------Assignment No - 8----------

You have a business with several offices; you want to lease phone lines to connect them up with each other; and the phone company charges different amounts of money to connect different pairs of cities. You want a set of lines that connects all your offices with minimum total cost. Solve the problem by suggesting appropriate data structures.
*/

#include <iostream>
using namespace std;

class tree
{
private:
    int a[20][20], v, e, visited[20];

public:
    void input();
    void display();
    void minimum();
};

void tree::input()
{
    cout << "Enter the no. of branches (max 20): ";
    cin >> v;
    if (v > 20 || v < 1)
    {
        cout << "Invalid number of branches. Exiting input process.";
        return;
    }
    for (int i = 0; i < v; i++)
    {
        visited[i] = 0;
        for (int j = 0; j < v; j++)
        {
            a[i][j] = 999;
        }
    }
    cout << "\nEnter the no. of connections (max " << v * (v - 1) / 2 << "): ";
    cin >> e;
    if (e > v * (v - 1) / 2 || e < 1)
    {
        cout << "Invalid number of connections. Exiting input process.";
        return;
    }
    for (int i = 0; i < e; i++)
    {
        int l, u, w;
        cout << "Enter the end branches of connection " << i + 1 << ": ";
        cin >> l >> u;
        if (l < 1 || l > v || u < 1 || u > v)
        {
            cout << "Invalid branch number. Exiting input process.";
            return;
        }
        cout << "Enter the phone company charges for this connection: ";
        cin >> w;
        a[l - 1][u - 1] = a[u - 1][l - 1] = w;
    }
}

void tree::display()
{
    cout << "\nAdjacency matrix:\n";
    for (int i = 0; i < v; i++)
    {
        for (int j = 0; j < v; j++)
        {
            cout << a[i][j] << "   ";
        }
        cout << endl;
    }
}

void tree::minimum()
{
    if (v == 0)
    {
        cout << "No data to process. Please input data first.\n";
        return;
    }
    int total = 0;
    visited[0] = 1;
    for (int count = 0; count < v - 1; count++)
    {
        int min = 999, p = 0, q = 0;
        for (int i = 0; i < v; i++)
        {
            if (visited[i] == 1)
            {
                for (int j = 0; j < v; j++)
                {
                    if (visited[j] != 1 && min > a[i][j])
                    {
                        min = a[i][j];
                        p = i;
                        q = j;
                    }
                }
            }
        }
        visited[p] = 1;
        visited[q] = 1;
        total += min;
        cout << "Minimum cost connection is " << p + 1 << " -> " << q + 1 << " with charge: " << min << endl;
    }
    cout << "The minimum total cost of connections of all branches is: " << total << endl;
}

int main()
{
    int ch;
    tree t;
    do
    {
        cout << "\n==========PRIM'S ALGORITHM=================\n";
        cout << "1. INPUT\n2. DISPLAY\n3. MINIMUM\n4. EXIT\n";
        cout << "Enter your choice: ";
        cin >> ch;
        switch (ch)
        {
        case 1:
            cout << "\n******* INPUT YOUR VALUES *******\n";
            t.input();
            break;
        case 2:
            cout << "\n******* DISPLAY THE CONTENTS ********\n";
            t.display();
            break;
        case 3:
            cout << "\n********* MINIMUM ************\n";
            t.minimum();
            break;
        case 4:
            cout << "Exiting program...\n";
            break;
        default:
            cout << "Invalid choice. Please try again.\n";
        }
    } while (ch != 4);
    return 0;
}
