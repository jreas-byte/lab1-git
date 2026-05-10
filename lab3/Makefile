CXX = g++
CXXFLAGS = -std=c++17 -Wall -Wextra -O2
TARGET = app
SOURCES = main.cpp Product.cpp Store.cpp
OBJECTS = $(SOURCES:.cpp=.o)

all: $(TARGET)

$(TARGET): $(OBJECTS)
	$(CXX) $(CXXFLAGS) $(OBJECTS) -o $(TARGET)

main.o: main.cpp Product.h Store.h
	$(CXX) $(CXXFLAGS) -c main.cpp -o main.o

Product.o: Product.cpp Product.h
	$(CXX) $(CXXFLAGS) -c Product.cpp -o Product.o

Store.o: Store.cpp Store.h Product.h
	$(CXX) $(CXXFLAGS) -c Store.cpp -o Store.o

clean:
	rm -f $(OBJECTS) $(TARGET)

.PHONY: all clean
