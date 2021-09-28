// Problem : https://practice.geeksforgeeks.org/problems/sort-a-stack/1

// References : https://www.geeksforgeeks.org/sort-stack-using-temporary-stack/

void SortedStack :: sort()
{
   //Your code here
   	stack<int> s1;
	s1.push(s.top());
	s.pop();

	while(!s.empty()){

		int temp =  s.top();
		s.pop();
		while(!s1.empty() && temp < s1.top()){  //sorting condition for ascending or descending
			s.push(s1.top());
			s1.pop();
		}
		s1.push(temp);
	}

		while(!s1.empty()){
			cout << s1.top() << " ";
			s1.pop();
		}
	
}