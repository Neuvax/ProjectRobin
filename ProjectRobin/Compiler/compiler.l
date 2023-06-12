%{
#include "y.tab.h"
#include <string.h>
extern int yylval;
%}

%%

"robot"        { return ROBOT; }
"Robot"        { return ROBOT; }
"ROBOT"        { return ROBOT; }
"Robin"        { return ROBOT; }

"please"       { return KIND; }
"kindly"       { return KIND; }

"rotate"       { return ROTATION; }
"turn"         { return ROTATION; }
"spin"         { return ROTATION; }

[0-9]          { yylval = atoi(yytext); return NUM; }
"90"           { yylval = atoi(yytext); return DEG; }
"180"          { yylval = atoi(yytext); return DEG; }
"270"          { yylval = atoi(yytext); return DEG; }
"360"          { yylval = atoi(yytext); return DEG; }

"to"           { return TO; }

"the"          { return THE; }

"front"        { return FRONT_BACK; }
"back"         { return FRONT_BACK; }

"right"        { return RIGHT_LEFT; }
"left"         { return RIGHT_LEFT; }

"move"         { return MOVEMENT; }
"go"           { return MOVEMENT; }
"travel"       { return MOVEMENT; }

"degrees"      { return DEGREES; }

"steps"        { return UNIT; }
"units"        { return UNIT; }

", "           { return COMMA; }

"finally"      { return FCNCTR; }
"lastly"       { return FCNCTR; }
"last"         { return FCNCTR; }
"and then"     { return FCNCTR; }
"and finally"  { return FCNCTR; }
"and lastly"   { return FCNCTR; }
"and last"     { return FCNCTR; }
"and"          { return FCNCTR; }

"next"         { return NEX; }
"then"         { return NEX; }
"after that"   { return NEX; }
"afterwards"   { return NEX; }
"after"        { return NEX; }
"subsequently" { return NEX; }
"successively" { return NEX; }

\n             { return EOS; }

[ \t]+         ; // Ignorar espacios en blanco

.              { printf("Caracter no reconocido: %c\n", yytext[0]); /* Manejar tokens no reconocidos o errores */ }

%%

int yywrap() {
    return 1;
}
