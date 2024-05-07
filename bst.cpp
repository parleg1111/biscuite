/* 
----------Assignment No - 4----------

Beginning with an empty binary search tree, Construct binary search tree by inserting the values in the order
given. After constructing a binary tree - 

i. Insert new node, 

ii. Find number of nodes in longest path from root, 

iii. Minimum data value found in the tree, 

iv. Change a tree so / l the roles of the left and right pointers are swapped at every node, 

v. Search a value	*/

#include<iostream>
#include<stdio.h>
#include<stdlib.h>
using namespace std;

typedef struct node
{
    int a;
    struct node *left, *right;
} node;

class BST
{
private:
    int count;
    node *root;

public:
    BST()
    {
        count = 0;
        root = NULL;
    }
    node *create();
    void insert();
    int height(node *, int c);
    int findmin(node *);
    void swap(node *);
    void search(node *, int);
    void display(node *);
    node *getRoot() const { return root; }
};

int main()
{
    BST b;
    int x, m, c = 0, cnt, min;
    do
    {
        cout << "\n enter your choice";
        cout << "\n 1.insert";
        cout << "\n 2.No of nodes in longest path";
        cout << "\n 3.Minimum value";
        cout << "\n 4.Swap";
        cout << "\n 5.Search";
        cout << "\n 6.display";
        cout << "\n 7.exit";
        cin >> x;
        switch (x)
        {
        case 1:
            b.insert();
            break;
        case 2:
            cnt = b.height(b.getRoot(), c);
            cout << "\n No of nodes in longest path=" << cnt;
            break;
        case 3:
            min = b.findmin(b.getRoot());
            cout << "\n Minimum value = " << min;
            break;
        case 4:
            b.swap(b.getRoot());
            break;
        case 5:
            cout << "\n enter data to be searched";
            cin >> m;
            b.search(b.getRoot(), m);
            break;
        case 6:
            b.display(b.getRoot());
            break;
        case 7:
            exit(0);
        }
    } while (x != 7);
    return 0;
}

node *BST::create()
{
    node *p = new (node);
    p->left = NULL;
    p->right = NULL;
    cout << "\n enter the data";
    cin >> p->a;
    return p;
}

void BST::insert()
{
    node *temp = create();
    if (root == NULL)
    {
        root = temp;
    }
    else
    {
        node *t1 = root;
        node *s = NULL;
        while (t1 != NULL)
        {
            s = t1;
            if ((temp->a) > (t1->a))
            {
                t1 = t1->right;
            }
            else
            {
                t1 = t1->left;
            }
        }
        if ((temp->a) > (s->a))
        {
            s->right = temp;
        }
        else
        {
            s->left = temp;
        }
    }
}

int BST::height(node *q, int c)
{
    if (root == NULL)
    {
        cout << "\n tree not exist";
    }
    else
    {
        c++;
        if (q->left != NULL)
        {
            height(q->left, c);
        }
        if (q->right != NULL)
        {
            height(q->right, c);
        }
        if (count < c)
        {
            count = c;
        }
    }
    return count;
}

int BST::findmin(node *T)
{
    while (T->left != NULL)
    {
        T = T->left;
    }
    return T->a;
}

void BST::swap(node *q)
{
    if (q == NULL)
    {
        cout << "\n tree not exist";
    }
    else
    {
        if (q->left != NULL)
            swap(q->left);
        if (q->right != NULL)
            swap(q->right);
        node *t = q->left;
        q->left = q->right;
        q->right = t;
    }
}

void BST::search(node *root, int m)
{
    int f = 0; // Initialize flag to 0
    if (root != NULL)
    {
        if (root->a == m)
            f = 1;
        if (m > root->a)
            search(root->right, m);
        else
            search(root->left, m);
    }
    if (f == 1)
        cout << "\n"
             << m << " FOUND!!!";
}

void BST::display(node *q)
{
    if (q == NULL)
    {
        cout << "\n tree not exist";
    }
    else
    {
        cout << "\n*"
             << q->a;
        if (q->left != NULL)
        {
            display(q->left);
        }
        if (q->right != NULL)
        {
            display(q->right);
        }
    }
}
