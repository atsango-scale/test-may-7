#include <iostream>
#include <map>
#include <vector>
#include <iomanip>
#include "csv.hpp"

struct ColumnStats {
    double sum = 0.0;
    int count = 0;
};

bool isNumeric(const std::string& str) {
    try {
        size_t pos;
        std::stod(str, &pos);
        return pos == str.length();
    } catch (...) {
        return false;
    }
}

int main(int argc, char* argv[]) {
    if (argc != 2) {
        std::cerr << "Usage: " << argv[0] << " <csv_file>" << std::endl;
        return 1;
    }

    std::string filename = argv[1];
    std::ifstream file(filename);
    
    if (!file.is_open()) {
        std::cerr << "Error: Could not open file '" << filename << "'" << std::endl;
        return 1;
    }

    std::vector<std::string> headers;
    std::map<size_t, ColumnStats> columnStats;
    bool isFirstRow = true;

    try {
        for (const auto& row : CSVRange(file)) {
            if (isFirstRow) {
                // Store headers
                for (size_t i = 0; i < row.size(); ++i) {
                    headers.push_back(row[i]);
                }
                isFirstRow = false;
                continue;
            }

            // Process data rows
            for (size_t i = 0; i < row.size(); ++i) {
                if (isNumeric(row[i])) {
                    double value = std::stod(row[i]);
                    columnStats[i].sum += value;
                    columnStats[i].count++;
                }
            }
        }

        // Print results
        std::cout << "\nMean values for each column:" << std::endl;
        std::cout << std::string(30, '-') << std::endl;
        
        for (size_t i = 0; i < headers.size(); ++i) {
            if (columnStats[i].count > 0) {
                double mean = columnStats[i].sum / columnStats[i].count;
                std::cout << headers[i] << ": " 
                         << std::fixed << std::setprecision(2) 
                         << mean << std::endl;
            }
        }

    } catch (const std::exception& e) {
        std::cerr << "An error occurred: " << e.what() << std::endl;
        return 1;
    }

    return 0;
} 