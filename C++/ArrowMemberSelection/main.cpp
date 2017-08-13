#include <iostream>
#include <string>

using namespace std;

/* Book class */
class Books {
    private:
        int id;
        string title;
        string author;

    public:
        Books() {
            cout << "Constructor" << endl;
        }

        void setId(int x) {
            id = x;
        }

        void setTitle(string x) {
            title = x;
        }

        void setAuthor(string x) {
            author = x;
        }

        int getId()  {
            return id;
        }

        string getTitle() {
            return title;
        }

        string getAuthor() {
            return author;
        }
};


int main()
{
    Books x;

    /* Set pointer to memory address of book object.
    the pointer is required to use arrow member selection operator -> */
    Books *BookPointer = &x;

    /* Set book title */
    BookPointer->setTitle("Harry Potter");

    /* Print book title using book pointer */
    cout << BookPointer->getTitle() << endl;

    return 0;
}
