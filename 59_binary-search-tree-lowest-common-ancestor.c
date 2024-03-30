#include <stdio.h>
#include <string.h>
#include <math.h>
#include <stdlib.h>
// https://www.hackerrank.com/challenges/binary-search-tree-lowest-common-ancestor/problem

struct node {
    
    int data;
    struct node *left;
    struct node *right;
  
};

struct node* insert( struct node* root, int data ) {
		
	if(root == NULL) {
	
        struct node* node = (struct node*)malloc(sizeof(struct node));

        node->data = data;

        node->left = NULL;
        node->right = NULL;
        return node;
	  
	} else {
      
		struct node* cur;
		
		if(data <= root->data) {
            cur = insert(root->left, data);
            root->left = cur;
		} else {
            cur = insert(root->right, data);
            root->right = cur;
		}
	
		return root;
	}
}

// Solution start here
#include <stdbool.h>

// Procedure created to check if a subtree contains a node 
bool contains( struct node *root, int v1 ){
    if (root == NULL) {
        return false;
    }
    else if (root->data == v1) {
        return true;
    }
    else if (contains(root->left, v1) || contains(root->right, v1)) {
        return true;
    }
    else {
        return false;
    }
}

/* you only have to complete the function given below.  
node is defined as  

struct node {
    
    int data;
    struct node *left;
    struct node *right;
    
};

*/
struct node *lca( struct node *root, int v1, int v2 ) {
    // If v1 > v2, reverse (just for better management)
    if (v1 > v2) {
        int tmp = v1;
        v1 = v2;
        v2 = tmp;
    }
    // Case when left subtree contains both
    if (contains(root->left, v1) && contains(root->left, v2)){
        return (lca(root->left, v1, v2));
    }
    // Case when left subtree contains v1 and right subtree contains v2 => Returns current node
    if (contains(root->left, v1) && contains(root->right, v2)){
        return (root);
    }
    // Case when right subtree contains both
    if (contains(root->right, v1) && contains(root->right, v2)){
        return (lca(root->right, v1, v2));
    }
    // It should never reach this stage (added just for compilation purposes)
    return root;
}


int main() {
  
    struct node* root = NULL;
    
    int t;
    int data;

    scanf("%d", &t);

    while(t-- > 0) {
        scanf("%d", &data);
        root = insert(root, data);
    }
  	int v1;
  	int v2;
  
  	scanf("%d%d", &v1, &v2);
	struct node *ans = lca(root, v1, v2);
  	printf("%d", ans->data);
  	
    return 0;
}

