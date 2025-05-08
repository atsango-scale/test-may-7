CXX = g++
CXXFLAGS = -std=c++11 -Wall -Wextra

TARGET = calculate_means
SOURCES = calculate_means.cpp

$(TARGET): $(SOURCES)
	$(CXX) $(CXXFLAGS) -o $(TARGET) $(SOURCES)

.PHONY: clean
clean:
	rm -f $(TARGET) 