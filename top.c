#include <stdio.h>
#include <stdlib.h>
#include <strings.h>
#include <gc.h>
#include "uthash.h"

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
  } else {
    HASH_ADD_KEYPTR(hh, *table, v->key, strlen(v->key), v);
  }
}

char* mold_hash_get(struct hash_entry** table, char* key) {
  struct hash_entry* v = NULL;
  HASH_FIND_STR(*table, key, v);
  return v->val;
}

