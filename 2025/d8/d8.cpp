#include<vector>
#include<fstream>
#include<sstream>
#include<algorithm>
#include<iostream>

using namespace std; 

vector<vector<int>> pts; 
    
struct DisjointSet{
    vector<int> parent;
    vector<int> f;

    DisjointSet(int n){
        parent.resize(n);
        f.resize(n);
        for(int i = 0; i < n; i++){
            parent[i] = i; f[i] = 1;
        }
    }

    int find(int x){
        if(parent[x] != x){
            parent[x] = find(parent[x]);
        }
        return parent[x];
    }

    void merge(int x, int y){
        int rootX = find(x);
        int rootY = find(y);
        if(rootX != rootY){
            if(f[rootX] > f[rootY]){
                f[rootX] += f[rootY];
                parent[rootY] = rootX;
            }
            else{
                f[rootY] += f[rootX];
                parent[rootX] = rootY;
            }
        }
    }
}; 

int part1(){
    vector<pair<long long, pair<int, int>>> v; 
    for (int i = 0; i < (int)pts.size(); i++){
        for (int j = i + 1; j < pts.size(); j++){
            long long dist_sq = 0; 
            for (int k = 0; k < 3; k++){
                dist_sq += 1LL *(pts[i][k] - pts[j][k]) * (pts[i][k] - pts[j][k]);
            }
            v.emplace_back(make_pair(dist_sq, make_pair(i, j)));
        }
    }

    std::sort(v.begin(), v.end());
    DisjointSet d(pts.size());
    for (int i = 0; i < 1000000;i++) {
        int x = v[i].second.first;
        int y = v[i].second.second;
        d.merge(x, y);
        if (d.f[d.find(x)] == pts.size() || d.f[d.find(y)] == pts.size()){
            cout << "Multiply of 2 X's coordinates: " << 1LL * pts[x][0] * pts[y][0] << endl;
            break;
        }
    }

    vector<int> sizes;
    for (int i = 0; i < pts.size(); i++){
        if (d.find(i) == i){
            sizes.push_back(d.f[i]);
        }
    }
    sort(sizes.begin(), sizes.end());
    return sizes[sizes.size() - 1] * sizes[sizes.size() - 2] * sizes[sizes.size() - 3];
}

int main(){
    std::ifstream file("input.txt");
    std::string line;
    while(std::getline(file, line)){
        std::stringstream ss(line);
        string token;
        vector<int> pt; 
        while(std::getline(ss, token, ',')){
            pt.push_back(stoi(token));
        }

        pts.push_back(pt);
    }

    std::cout << part1(); 

    return 0; 
}