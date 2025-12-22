.PHONY: run create help

# Default day if not specified
DAY ?= 1

# Run the solution for a specific day
run:
	@if [ -f "d$(DAY)/d$(DAY).py" ]; then \
		cd d$(DAY) && python d$(DAY).py; \
	elif [ -f "d$(DAY)/d$(DAY).cpp" ]; then \
		if [ ! -f "d$(DAY)/solve" ] || [ "d$(DAY)/d$(DAY).cpp" -nt "d$(DAY)/solve" ]; then \
			echo "Compiling d$(DAY)/d$(DAY).cpp..."; \
			g++ -std=c++17 -o d$(DAY)/solve d$(DAY)/d$(DAY).cpp; \
		fi; \
		cd d$(DAY) && ./solve; \
	else \
		echo "Error: No solution file found for day $(DAY)"; \
		echo "Expected: d$(DAY)/d$(DAY).py or d$(DAY)/d$(DAY).cpp"; \
		exit 1; \
	fi

# Create a new day folder with template files
create:
	@if [ -z "$(DAY)" ] || [ "$(DAY)" = "1" ]; then \
		echo "Error: Please specify a day number using DAY=<number>"; \
		echo "Example: make create DAY=10"; \
		exit 1; \
	fi
	@if [ -d "d$(DAY)" ]; then \
		echo "Warning: Directory d$(DAY) already exists"; \
	else \
		mkdir -p d$(DAY); \
		echo "Created directory d$(DAY)"; \
	fi
	@if [ ! -f "d$(DAY)/d$(DAY).py" ]; then \
		echo "# Day $(DAY) solution" > d$(DAY)/d$(DAY).py; \
		echo "" >> d$(DAY)/d$(DAY).py; \
		echo "def part1():" >> d$(DAY)/d$(DAY).py; \
		echo "    with open('input.txt', 'r') as f:" >> d$(DAY)/d$(DAY).py; \
		echo "        pass" >> d$(DAY)/d$(DAY).py; \
		echo "" >> d$(DAY)/d$(DAY).py; \
		echo "def part2():" >> d$(DAY)/d$(DAY).py; \
		echo "    with open('input.txt', 'r') as f:" >> d$(DAY)/d$(DAY).py; \
		echo "        pass" >> d$(DAY)/d$(DAY).py; \
		echo "" >> d$(DAY)/d$(DAY).py; \
		echo "if __name__ == '__main__':" >> d$(DAY)/d$(DAY).py; \
		echo "    part1()" >> d$(DAY)/d$(DAY).py; \
		echo "    part2()" >> d$(DAY)/d$(DAY).py; \
		echo "Created d$(DAY)/d$(DAY).py"; \
	else \
		echo "Warning: d$(DAY)/d$(DAY).py already exists"; \
	fi
	@if [ ! -f "d$(DAY)/input.txt" ]; then \
		touch d$(DAY)/input.txt; \
		echo "Created d$(DAY)/input.txt"; \
	else \
		echo "Warning: d$(DAY)/input.txt already exists"; \
	fi

# Help target
help:
	@echo "Usage:"
	@echo "  make run DAY=<day_number>    - Run solution for a specific day"
	@echo "  make create DAY=<day_number> - Create new day folder with template files"
	@echo ""
	@echo "Examples:"
	@echo "  make run DAY=1"
	@echo "  make create DAY=10"
