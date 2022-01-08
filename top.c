#include <stdio.h>
#include <stdlib.h>
#include <strings.h>
#include <gc.h>
#include "uthash.h"
#include <stdbool.h>

void mold_strcat(char** dst, char* src) {
  char* oldDst = *dst;
  (*dst) = GC_MALLOC(strlen(oldDst) + strlen(src) + 1);
  strcpy(*dst, oldDst);
  strcat(*dst, src);
}

struct hash_entry {
  char* key;
  char* val;
  UT_hash_handle hh;
};

void mold_hash_set(struct hash_entry** table, char* key, char* value) {
  struct hash_entry* v = NULL;
  v = (struct hash_entry*) malloc(sizeof(*v));
  v->key = key;
  v->val = value;
  
  struct hash_entry* exists = NULL;
  HASH_FIND_STR(*table, key, exists);
  if (exists != NULL) {
    HASH_DEL(*table, exists);
    free(exists);
  }

  HASH_ADD_KEYPTR(hh, *table, v->key, strlen(v->key), v);
}

char* mold_hash_get(struct hash_entry** table, char* key) {
  struct hash_entry* v = NULL;
  HASH_FIND_STR(*table, key, v);
  if (v == NULL) {
    printf("runtime error: dictionary key not found: \"%s\"\n", key);
    exit(1);
  }
  return v->val;
}

char* mold_ftoa(float val) {
  int len = snprintf(NULL, 0, "%f", val);
  char* str = GC_MALLOC(len + 1);
  snprintf(str, len + 1, "%f", val);
  return str;
}

char* mold_itoa(float val) {
  int len = snprintf(NULL, 0, "%d", (int)val);
  char* str = GC_MALLOC(len + 1);
  snprintf(str, len + 1, "%d", (int)val);
  return str;
}

int argcnt = 0;
char** argval = NULL;

char* mold_arg(float index) {
  int ind = (int)index;
  if (ind < 0 || ind >= argcnt) {
    printf("runtime error: argument index out of range: %d\n", ind);
    exit(1);
  }
  return argval[ind];
}

