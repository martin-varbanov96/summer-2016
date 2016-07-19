#include <iostream>

using namespace std;

class Fridge{
public:
    Fridge(int tmpSalad = 0, int tmpKuft = 0){
        salata = tmpSalad;
        kufteta = tmpKuft;
    }
    void checkFridge(){
        cout << " salata = " << salata << " kufteta =  " << kufteta << endl;
    }
private:
    int kufteta;
    int salata;
    friend class Vseqden;
};

class Vseqden{
public:
    Vseqden(){}
    void hapnal(Fridge& tmp){
        tmp.kufteta--;
        tmp.salata--;
    }
};

class Vegan{

};

int main()
{
    Fridge hladilnika(10, 20);
    hladilnika.checkFridge();
    Vseqden Goshko;
    Goshko.hapnal(hladilnika);
    hladilnika.checkFridge();


    return 0;
}
