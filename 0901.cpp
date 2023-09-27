#include <vector>

using namespace std;

class StockSpanner {
public:
    vector<int> stocks;
    
    StockSpanner() {
    
    }
    
    int next(int price) {
        stocks.push_back(price);
        int i = stocks.size() - 1;
        int count = 0;
        while(i >= 0) {
            if(stocks[i] <= price) {
                count++;
            }else {
                break;
            }
            i--;
        }
        return count;
    }
};

/**
 * Your StockSpanner object will be instantiated and called as such:
 * StockSpanner* obj = new StockSpanner();
 * int param_1 = obj->next(price);
 */
