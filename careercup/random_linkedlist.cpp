/* Clone a linked list which has random pointers*/
#include <map>
#include <iostream>
using namespace std;

struct Node{
	int data;
	struct Node* next;
	struct Node* random;
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
	map<Node*,Node*> mymap;	
	struct Node* temp = head;
	struct Node* newHead;
	struct Node* prev;
	int ctr = 0;
	while(temp != NULL){
		Node* nextNode = CreateNode(temp->data);
		mymap.insert (pair<Node*,Node*>(temp,nextNode));
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
	temp = head;
	prev = newHead;
	while(temp != NULL){
		Node* random = temp->random;
		if(random != NULL && mymap.find(random) != mymap.end()){
			prev->random = mymap.find(random)->second;
		}		
		temp = temp->next;
		prev = prev->next;
	}
	return newHead;
}

void PrintNodes(Node* head)
{
	cout << head << " " << head->data << " " << head->next << " " << head->random << endl;
}

int main()
{
	//	2->6->4->8->NULL
	Node* node1 = CreateNode(2);
	Node* node2 = CreateNode(6);
	Node* node3 = CreateNode(4);
	Node* node4 = CreateNode(8);
	Node* node5 = CreateNode(12);
	Node* node6 = CreateNode(10);
	node1->next = node2;	
	node2->next = node3;
	node3->next = node4;
	node4->next = node5;
	node5->next = node6;
	node1->random = node4;	
	node2->random = node5;
	node3->random = node6;
	node4->random = node6;
	node5->random = node3;
	Node* newNode = CloneLinkedList(node1);
	PrintNodes(node1);
	PrintNodes(newNode);
	return 0;
}