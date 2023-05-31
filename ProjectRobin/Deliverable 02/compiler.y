%{
#include <stdio.h>
#include <stdlib.h>
%}

%token ROBOT KIND VROTATION DEGQ CLOCK DIRECT VMOVEMENT NUM UNIT ORI1 ORI2 ORI3 COMMA FCNCTR NEX EOS

%%
program: ROBOT instruction EOS
       | ROBOT instruction FCNCTR program
       ;

instruction: KIND action
           | action
           ;

action: rotation
      | movement DIR
      | movement
      ;

rotation: VROTATION DEGQ "degrees" CLOCK
        | VROTATION DEGQ "degrees"
        | VROTATION DIRECT
        ;

movement: VMOVEMENT NUM UNIT
        ;

DIR: ORI1
   | "to the" ORI1
   ;

%%
int main() {
    yyparse();
    return 0;
}

int yyerror(const char* msg) {
    fprintf(stderr, "Error: %s\n", msg);
    return 1;
}
