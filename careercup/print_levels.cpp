

#include <iostream>
#include <queue>

using namespace std;

struct Node
{
	int data;
	struct Node* left;
	struct Node* right;
};

void PrintLevels(Node* root)
{
	queue<Node*> level;
	queue<Node*> siblings;
	level.push(root);
	Node* temp;
	while(!level.empty()){
		temp = level.front();
		level.pop();
		if(temp){
			cout << temp->data << "   ";
			siblings.push(temp->left);
			siblings.push(temp->right);
		}
		if(level.empty()){
			cout << "\n\n";
			swap(siblings,level);
		}
	}
}

struct Node* NewNode(int data) {
	struct Node* node = new(struct Node); 
	node->data = data;
	node->left = NULL;
	node->right = NULL;
	return(node);
}

int main()
{
	Node* node1 = NewNode(20);
	Node* node2 = NewNode(23);
	Node* node3 = NewNode(15);
	Node* node4 = NewNode(32);
	Node* node5 = NewNode(28);
	Node* node6 = NewNode(40);
	Node* node7 = NewNode(56);
	Node* node8 = NewNode(52);
	Node* node9 = NewNode(29);
	Node* node10 = NewNode(14);
	Node* node11 = NewNode(18);
	
	node1->left = node2;
	node1->right = node3;

	node2->left = node4;
	
	node3->left = node5;
	node3->right = node6;
	node4->right = node7;
	node7->left = node10;
	node6->left = node8;
	node6->right = node9;
	
	node9->right = node11;
	PrintLevels(node1);
	return 0;
}

