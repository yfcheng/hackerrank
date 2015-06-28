#include <iostream>
#include <stdio.h>
#include <stdlib.h>
#include <string>

using namespace std;

struct Node{
	int data;
	struct Node* next;
};

struct Node* CreateNode(int data)
{
	Node* newNode = new (struct Node);
	newNode->data = data;
	newNode->next = NULL;
	return newNode;
}

void printlinkedlist(struct Node* n,int cnt)
{
	cout << "\nStarting....\n";
	Node * prev1;
	prev1 = n;
	for (int i = 0; i < cnt; i++)
	{
		cout << prev1->data << endl;
		//cout << prev1->next << endl;
		prev1 = prev1->next;
	}
	cout << "End....\n\n\n";

}

void Reverse(Node*& p) { 
	if(p == NULL || p->next == NULL) return;	//this incase there is a empty linkedlist
	Node * rest = p->next;
  	Reverse(rest);	//go to nextNode
  	p->next->next = p;
  	p = rest; 
}
 

int main(){
	//	2->6->4->8->NULL
	Node* node1 = CreateNode(2);
	Node* node2 = CreateNode(6);
	Node* node3 = CreateNode(4);
	Node* node4 = CreateNode(8);	
	node1->next = node2;
	node2->next = node3;
	node3->next = node4;
	printlinkedlist(node1,4);
	Reverse(node1);	
	printlinkedlist(node1,4);
	return 0;
}