%{
#include "y.tab.h"
#include <string.h>
%}

%%
"robot" | "Robot" | "ROBOT" | "Robin" { return ROBOT; }

"please" | "kindly" { return KIND; }

"rotate" | "turn" | "spin" | "revolve" { return VROTATION; }

"90" | "180" | "270" | "360" { return DEGQ; }

"to" { return TO; }

"the" { return THE; }

"right" | "left" { return ORI2; }

"clockwise" | "counterclockwise" | "right" | "left" { return ORI3; }

"move" | "go" | "travel" | "proceed" { return VMOVEMENT; }

[0-9]+ { yylval.num = atoi(yytext); return NUM; }

", " { return COMMA; }

"finally" | "lastly" | "last" | "and then" | "and finally" | "and lastly" | "and last" | "and" { return FCNCTR; }

"next" | "then" | "after that" | "afterwards" | "after" | "subsequently" | "successively" { return NEX; }

"degrees" { return DEGREES; }

"steps" | "units" { return UNIT; }

"front" | "back" { return ORI1; }

\n { return EOS; }

[ \t]+ ; // Ignore whitespace

. { /* Handle unrecognized tokens or error */ }

%%

int yywrap() {
    return 1;
}
