#include<bits/stdc++.h>
using namespace std;

void permute(vector<int> &arr,int ind){
	if(0==ind){
		for(int j=1; j<arr.size(); j++){
			if(arr[j-1]>arr[j]){
				return;
			}
		}
		for(int j=0; j<arr.size(); j++){
			cout<<arr[j]<<" ";
		}
		cout<<endl;
	}
	for(int k=ind; k>=0; --k){
		swap(arr[k],arr[ind]);
		permute(arr,ind-1);
		swap(arr[k],arr[ind]);
	}
}
int main() {
	int n; // #elements
	cin>>n;
	vector<int> arr(n);
	for(int i=0; i<n; i++){
		cin>>arr[i];
	}
	permute(arr,n-1);
	return 0;
}