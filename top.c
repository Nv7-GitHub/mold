#include <stdio.h>
#include <stdlib.h>
#include <strings.h>
#include <gc.h>

void mold_strcat(char** dst, char* src) {
  char* oldDst = *dst;
  (*dst) = GC_MALLOC(strlen(oldDst) + strlen(src) + 1);
  strcpy(*dst, oldDst);
  strcat(*dst, src);
}

