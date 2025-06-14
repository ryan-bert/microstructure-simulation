# Compiler and flags
CXX = g++
CXXFLAGS = -std=c++17 -Wall -Iinclude

# Automatically find all .cpp files in src/
SRC = $(wildcard src/*.cpp) main.cpp
OBJ = $(SRC:.cpp=.o)
TARGET = sim

# Default build rule
all: $(TARGET)

# Link object files into final binary
$(TARGET): $(OBJ)
	$(CXX) $(OBJ) -o $@

# Compile each .cpp into a .o
%.o: %.cpp
	$(CXX) $(CXXFLAGS) -c $< -o $@

# Run the program (depends on build)
run: $(TARGET)
	./$(TARGET)

# Clean build artifacts
clean:
	rm -f $(OBJ) $(TARGET)