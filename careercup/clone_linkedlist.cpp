/* Clone a linked list */

#include <iostream>
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

Node* CloneLinkedList(Node* head)
{
	struct Node* temp = head;
	struct Node* newHead;
	struct Node* prev;
	int ctr = 0;
	while(temp != NULL){
		Node* nextNode = CreateNode(temp->data);
		//Node* nextNode = temp;
		if(ctr == 0){
			prev = nextNode;
			newHead = nextNode;
			ctr++;
		}
		else{
			prev->next = nextNode;
			prev = nextNode;
		}
		temp = temp->next;
	}
	return newHead;
}

int main()
{
	//	2->6->4->8->NULL
	Node* node1 = CreateNode(2);
	Node* node2 = CreateNode(6);
	Node* node3 = CreateNode(4);
	Node* node4 = CreateNode(8);
	
	node1->next = node2;
	node2->next = node3;
	node3->next = node4;
	
	Node* newNode = CloneLinkedList(node1);
	cout << newNode << " " << newNode->data << endl;
	cout << node1 << " " << node1->data << endl;
	return 0;
}