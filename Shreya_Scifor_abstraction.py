#include <iostream>

class Shape {
public:
    virtual void draw() const = 0;

    void printMessage() const {
        cout << "This is a shape." << endl;
    }
};

class Circle : public Shape {
public:
    void draw() const override {
        cout << "circle" << endl;
    }
};

class Square : public Shape {
public:
    void draw() const override {
        cout << "square" << endl;
    }
};

int main() {
   
    Shape* shape1 = new Circle();
    Shape* shape2 = new Square();
    shape1->draw();
    shape1->printMessage();
    shape2->draw();
    shape2->printMessage();
    delete shape1;
    delete shape2;

    return 0;
}
