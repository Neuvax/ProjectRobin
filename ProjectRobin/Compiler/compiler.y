%{
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

FILE *asmFile; 
FILE *unitTest;

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

program : sentence_list                  { fprintf(unitTest, "PASS\n"); }
        | sentence_list EOS program      { fprintf(unitTest, "PASS\n"); }
        ;

sentence_list : ROBOT sentence
              | sentence_list sentence
              ;

sentence : KIND action_list
         ;

action_list : action                    
            | action FCNCTR action_list 
            | action NEX action_list 
            ;

action : rotation_action
       | movement_action
       ;

rotation_action : ROTATION distance DEGREES                           { fprintf(asmFile, "TURN,%d\n", $2); }
                | ROTATION distance DEGREES TO THE RIGHT_LEFT         { fprintf(asmFile, "TURN,%d\n", $2); }
                ;

movement_action : MOVEMENT distance UNIT                         { fprintf(asmFile, "MOV,%d\n", $2); }
                | MOVEMENT distance UNIT FRONT_BACK              { fprintf(asmFile, "MOV,%d\n", $2); }
                | MOVEMENT distance UNIT RIGHT_LEFT              { fprintf(asmFile, "MOV,%d\n", $2); }
                | MOVEMENT distance UNIT TO THE RIGHT_LEFT       { fprintf(asmFile, "MOV,%d\n", $2); }
                | MOVEMENT distance UNIT TO THE FRONT_BACK       { fprintf(asmFile, "MOV,%d\n", $2); }
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

    asmFile = fopen("instructions.asm", "w");
    if (asmFile == NULL) {
        perror("instructions.asm");
        exit(1);
    }

    unitTest = fopen("unitTest.asm", "w");
    if (unitTest == NULL) {
        perror("unitTest.asm");
        exit(1);
    }

    yyparse();

    fclose(asmFile);
    fclose(unitTest);

    return 0;
}

void yyerror(const char *s) {
    fprintf(unitTest, "FAIL\n");
}
