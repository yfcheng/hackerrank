#include <stack>
#include <limits>
#include <iostream>

using namespace std;

class MyStack{
private:
	stack<int> container;
	stack<int> max_container;
	stack<int> min_container;
	int max_peek;
	int min_peek;
public:
	MyStack();
	void push(int);
	int pop();
	int max();
	int min();	
};

MyStack::MyStack(){
	min_peek = numeric_limits<int>::max();
	max_peek = numeric_limits<int>::min();
}

void MyStack::push(int item){
	container.push(item);
	if(item > max_peek){
		max_peek = item;		
	}
	max_container.push(max_peek);
	if(item < min_peek){
		min_peek = item;		
	}
	min_container.push(min_peek);
}

int MyStack::pop(){
	if(container.empty()){
		min_peek = numeric_limits<int>::max();
		max_peek = numeric_limits<int>::min();
		return numeric_limits<int>::max();
	}

	max_container.pop();
	max_peek = max_container.top();
	min_container.pop();
	min_peek = min_container.top();

	int data = container.top();
	container.pop();
	return data;
}

int MyStack::max(){
	return max_peek;
}	

int MyStack::min(){
	return min_peek;
}

int main(){
	MyStack currStack;
	currStack.push(10);
	currStack.push(3);
	currStack.push(12);
	currStack.push(13);
	currStack.push(14);
	currStack.push(1);
	currStack.push(8);	
	cout << currStack.max() << endl;
	cout << currStack.min() << endl;
	cout << "----" << endl;

	int data;	
	//data = currStack.pop();
	//data = currStack.pop();
	data = currStack.pop();
	cout << data << endl;
	cout << currStack.max() << endl;
	cout << currStack.min() << endl;
	cout << "----" << endl;

	data = currStack.pop();
	cout << data << endl;
	cout << currStack.max() << endl;
	cout << currStack.min() << endl;
	cout << "----" << endl;

	data = currStack.pop();
	cout << data << endl;
	cout << currStack.max() << endl;
	cout << currStack.min() << endl;
	cout << "----" << endl;

	data = currStack.pop();
	cout << data << endl;
	cout << currStack.max() << endl;
	cout << currStack.min() << endl;
	cout << "----" << endl;

	return 0;
}