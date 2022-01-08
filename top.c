#include <stdio.h>
#include <stdlib.h>
#include <stdbool.h>
#include <time.h>
#include <strings.h>
#include <gc.h>
#include "uthash.h"

typedef struct string {
  char* val;
  int len;
  int capacity;
} string;

string* mold_newstring(char* val) {
  string* s = GC_MALLOC(sizeof(string));
  char* v = GC_MALLOC(strlen(val)*2); // Alloc with 2x capacity
  memcpy(v, val, strlen(val));
  s->val = v;
  s->len = strlen(val);
  s->capacity = s->len*2;
  return s;
}

char* mold_cstring(string* str) {
  char* out = GC_MALLOC(str->len + 1);
  memcpy(out, str->val, str->len);
  return out;
}

void mold_resize_string(string* s) {
  s->capacity *= 2;
  char* newVal = GC_MALLOC(s->capacity);
  memcpy(newVal, s->val, s->len);
  s->val = newVal;
}

void mold_strcat(string* dst, string* src) {
  if ((dst->len + src->len) > dst->capacity) {
    mold_resize_string(dst);
  }
  memcpy(dst->val + dst->len, src->val, src->len);
  dst->len += src->len;
}

struct hash_entry {
  char* key;
  char* val;
  UT_hash_handle hh;
};

void mold_hash_set(struct hash_entry** table, string* key, string* value) {
  struct hash_entry* v = NULL;
  v = (struct hash_entry*) malloc(sizeof(*v));
  v->key = mold_cstring(key);
  v->val = mold_cstring(value);
  
  struct hash_entry* exists = NULL;
  HASH_FIND_STR(*table, mold_cstring(key), exists);
  if (exists != NULL) {
    HASH_DEL(*table, exists);
    free(exists);
  }

  HASH_ADD_KEYPTR(hh, *table, v->key, strlen(v->key), v);
}

string* mold_hash_get(struct hash_entry** table, string* key) {
  struct hash_entry* v = NULL;
  HASH_FIND_STR(*table, mold_cstring(key), v);
  if (v == NULL) {
    printf("runtime error: dictionary key not found: \"%s\"\n", mold_cstring(key));
    exit(1);
  }
  return mold_newstring(v->val);
}

string* mold_ftoa(float val) {
  int len = snprintf(NULL, 0, "%f", val);
  char* str = GC_MALLOC(len + 1);
  snprintf(str, len + 1, "%f", val);
  return mold_newstring(str);
}

string* mold_itoa(float val) {
  int len = snprintf(NULL, 0, "%d", (int)val);
  char* str = GC_MALLOC(len + 1);
  snprintf(str, len + 1, "%d", (int)val);
  return mold_newstring(str);
}

int argcnt = 0;
char** argval = NULL;

string* mold_arg(float index) {
  int ind = (int)index;
  if (ind < 0 || ind >= argcnt) {
    printf("runtime error: argument index out of range: %d\n", ind);
    exit(1);
  }
  return mold_newstring(argval[ind]);
}

string* mold_strind(string* str, float index) {
  int ind = (int)index;
  if (ind < 0 || ind >= str->len) {
    printf("runtime error: string index out of range: %d\n", ind);
    exit(1);
  }
  char* out = GC_MALLOC(2);
  memcpy(out, str->val + ind, 1);

  string* s = GC_MALLOC(sizeof(string));
  s->val = out;
  s->len = 1;
  s->capacity = 2;
  return s;
}

float mold_rand(float low, float high) {
  float random = ((float) rand()) / (float) RAND_MAX;
  return (random*(high-low)) + low;
}

float mold_irand(float l, float h) {
  int low = (int)l;
  int high = (int)h;
  return (float)((rand() % (high - low + 1)) + low);
}

