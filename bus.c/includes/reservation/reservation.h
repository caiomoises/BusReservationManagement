#include "../bus/bus.h"
typedef struct tickets Tickets;

Tickets *start();
Tickets *makeReservation(Tickets *l, Bus *b, int number, char *name);
Tickets *deleteReservation(Tickets *t, Bus *b, char *name);
void showReservation(Tickets *t, int number);
void searchReservation(Tickets *t, char *name);
void editReservation(Tickets *t, Bus *b, int number);
void writeFile(Tickets *t);
Tickets *readFile(Bus *b);
void freeTickets(Tickets *t);