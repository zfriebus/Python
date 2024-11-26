def two_letter_combinations(char_list):
    for i in range(len(char_list)):  
        for j in range(len(char_list)): 
            yield char_list[i] + char_list[j] # turns code into generator 

# Main function to test the generator
def main():
    char_list = ['Z', 'A', 'C', 'H', 'F']
    
    # Call the generator function and print each combination
    print("Two-letter combinations:")
    for combination in two_letter_combinations(char_list):
        print(combination)

if __name__ == "__main__":
    main()