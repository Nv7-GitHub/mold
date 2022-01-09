#include <stdio.h>
#include <stdlib.h>
#include <stdbool.h>
#include <time.h>
#include <strings.h>
#include <gc.h>
#include "uthash.h"

// Strings
typedef struct string {
  char* val;
  int len;
  int capacity;
} string;

string* mold_newstring(char* val) {
  if (strlen(val) == 0) {
    string* s = GC_MALLOC(sizeof(string));
    char* v = GC_MALLOC(1);
    s->val = v;
    s->len = 0;
    s->capacity = 1;
    return s;
  }
  
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

// Dictionaries
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

// Number 2 string
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

// Command line args
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

// Rand
float mold_rand(float low, float high) {
  float random = ((float) rand()) / (float) RAND_MAX;
  return (random*(high-low)) + low;
}

float mold_irand(float l, float h) {
  int low = (int)l;
  int high = (int)h;
  return (float)((rand() % (high - low + 1)) + low);
}

// OS Interaction
string* mold_read(string* file) {
  FILE* f = fopen(mold_cstring(file), "r");
  if (f == NULL) {
    printf("runtime error: file not found: \"%s\"\n", mold_cstring(file));
    exit(1);
  }

  // Get len
  fseek(f, 0, SEEK_END);
  int len = ftell(f);
  rewind(f);

  // Read
  char* str = GC_MALLOC(len + 1);
  fread(str, 1, len, f);

  // Close
  fclose(f);

  return mold_newstring(str);
}

void mold_write(string* file, string* data) {
  FILE* f = fopen(mold_cstring(file), "w+");
  if (f == NULL) {
    printf("runtime error: file not found: \"%s\"\n", mold_cstring(file));
    exit(1);
  }

  fwrite(mold_cstring(data), 1, data->len, f);
  fclose(f);
}

void mold_remove(string* file) {
  remove(mold_cstring(file));
}

string* mold_system(string* cmd) {
  FILE* f = popen(mold_cstring(cmd), "r");
  if (f == NULL) {
    printf("runtime error: system command failed: \"%s\"\n", mold_cstring(cmd));
    exit(1);
  }

  // Get len
  fseek(f, 0, SEEK_END);
  int len = ftell(f);
  rewind(f);

  // Read
  char* str = GC_MALLOC(len + 1);
  fread(str, 1, len, f);

  // Close
  pclose(f);

  return mold_newstring(str);
}

// Switch-case (adapted from https://github.com/haipome/fnv)
#define FNV_32_PRIME 0x01000193
#define FNV1_32_INIT 0x811c9dc5

u_int32_t mold_fnv_32a_str(char *str) {
    u_int32_t hval = FNV1_32_INIT;
    unsigned char *s = (unsigned char *)str;	/* unsigned string */
    while (*s) {
      /* xor the bottom with the current octet */
      hval ^= (u_int32_t)*s++;

      /* multiply by the 32 bit FNV magic prime mod 2^32 */
      hval *= FNV_32_PRIME;
    }

    /* return our new hash value */
    return hval;
}

// Stacks
typedef struct mold_stack {
  string* val;
  struct mold_stack* next;
} mold_stack;

string* mold_stack_top(mold_stack** stack) {
  return (*stack)->val;
}

void mold_stack_push(mold_stack** stack, string* val) {
  if ((*stack)->val == NULL) {
    (*stack)->val = val;
    return;
  }
  mold_stack* s = (mold_stack*)GC_MALLOC(sizeof(mold_stack));
  s->val = val;
  s->next = *stack;
  *stack = s;
}

void mold_stack_pop(mold_stack** stack) {
  mold_stack* s = *stack;
  (*stack) = s->next;
}

mold_stack* mold_stack_new() {
  mold_stack* s = (mold_stack*)GC_MALLOC(sizeof(mold_stack));
  s->val = NULL;
  s->next = NULL;
  return s;
}
