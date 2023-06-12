%{
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
int yylex();
void yyerror(const char *s);
extern FILE *yyin;
%}

%token 
ROBOT 
KIND 
ROTATION 
NUM
DEG
TO 
THE 
FRONT_BACK 
RIGHT_LEFT 
MOVEMENT 
DEGREES 
UNIT 
COMMA 
FCNCTR 
NEX 
EOS

%%

program : sentence_list
        | program EOS program
        ;

sentence_list : ROBOT sentence
              | sentence_list sentence
              ;

sentence : action_list
         | KIND sentence
         ;

action_list : action                    
            | action FCNCTR action_list 
            | action NEX action_list 
            ;

action : rotation_action
       | movement_action
       ;

rotation_action : ROTATION distance DEGREES                           { printf("TURN, %d\n", $2); }
                | ROTATION distance DEGREES TO THE RIGHT_LEFT         { printf("TURN, %d\n", $2); }
                ;

movement_action : MOVEMENT distance UNIT                         { printf("MOV, %d\n", $2); }
                | MOVEMENT distance UNIT FRONT_BACK              { printf("MOV, %d\n", $2); }
                | MOVEMENT distance UNIT RIGHT_LEFT              { printf("MOV, %d\n", $2); }
                | MOVEMENT distance UNIT TO THE RIGHT_LEFT       { printf("MOV, %d\n", $2); }
                | MOVEMENT distance UNIT TO THE FRONT_BACK       { printf("MOV, %d\n", $2); }
                ;

distance : NUM  { $$ = $1; }
         | DEG  { $$ = $1; }
         ;
%%

int main(int argc, char **argv) {
    char *line = NULL;
    size_t len = 0;
    ssize_t read;

    if (argc > 1) {
        yyin = fopen(argv[1], "r");
        if (yyin == NULL) {
            perror(argv[1]);
            exit(1);
        }
    }
    yyparse();
}

void yyerror(const char *s) {
    printf("FAIL\n");
}
