#include <iostream>
#include <unordered_map>
#include <string>
#include <random>
#include <fstream>
#include <stack>
#include <filesystem>

void lib_mold_error(std::string e) {
  std::cerr << e << std::endl;
  exit(1);
}

// Command line args
int argcnt = 0;
char** argval = NULL;

std::string lib_mold_arg(float index) {
  if (index < 0 || index >= argcnt) {
    lib_mold_error("runtime error: index out of bounds");
  }
  return argval[(int)index];
}

// Random
float lib_mold_random(float min, float max) {
  static std::random_device rd;
  static std::mt19937 gen(rd());
  std::uniform_real_distribution<> dis(min, max);
  return dis(gen);
}

float lib_mold_randint(float min, float max) {
  static std::random_device rd;
  static std::mt19937 gen(rd());
  std::uniform_int_distribution<> dis((int)min, (int)max);
  return (float)dis(gen);
}

// OS
std::string lib_mold_read(std::string path) {
  constexpr std::size_t read_size = std::size_t(4096);
  std::ifstream stream = std::ifstream(path.data());
  stream.exceptions(std::ios_base::badbit);
  
  std::string out;
  std::string buf = std::string(read_size, '\0');
  while (stream.read(& buf[0], read_size)) {
    out.append(buf, 0, stream.gcount());
  }
  out.append(buf, 0, stream.gcount());
  return out;
}

void lib_mold_write(std::string path, std::string data) {
  std::ofstream stream = std::ofstream(path.data());
  stream.exceptions(std::ios_base::badbit);
  stream << data;
  stream.close();
}

// https://stackoverflow.com/a/12468109/11388343
std::string lib_mold_internal_random_string( size_t length ) {
  auto randchar = []() -> char {
    const char charset[] = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz";
    const size_t max_index = (sizeof(charset) - 1);
    return charset[ rand() % max_index ];
  };
  std::string str(length,0);
  std::generate_n(str.begin(), length, randchar);
  return str;
}

// https://stackoverflow.com/a/20617844/11388343 (modified to use my own unique file generator and lib_mold_read_file)
std::string lib_mold_system(std::string command) {
  std::string temp = std::filesystem::temp_directory_path().native() + lib_mold_internal_random_string(6);
  std::string cmd = command + " >> " + temp;
  std::system(cmd.c_str());

  std::ifstream file(temp, std::ios::in | std::ios::binary );
  std::string result = lib_mold_read(temp);
  std::remove(temp.c_str());

  return result;
}

void lib_mold_remove(std::string path) {
  int err = std::remove(path.c_str());
  if (err != 0) {
    lib_mold_error("runtime error: failed to remove file");
  }
}

// Switch-case
#define FNV_32_PRIME 0x01000193
#define FNV1_32_INIT 0x811c9dc5

u_int32_t lib_mold_fnv_32a(std::string str) {
  u_int32_t hash = FNV1_32_INIT;
  for (char c : str) {
    hash ^= c;
    hash *= FNV_32_PRIME;
  }
  return hash;
}

constexpr u_int32_t lib_mold_fnv_32a_const(const char* s) {
  u_int32_t hash = FNV1_32_INIT;
  while (*s) {
    hash ^= (u_int32_t)*s++;
    hash *= FNV_32_PRIME;
  }
  return hash;
}

// Strings
bool lib_mold_numeric(std::string str) {
  if (str.length() == 0) {
    return false;
  }
  
  for (char c : str) {
    if ((c < '0' || c > '9') && c != '.') {
      return false;
    }
  }
  return true;
}

