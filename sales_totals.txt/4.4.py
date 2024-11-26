def main():
   with open('sales_totals', 'r') as file:
        line = file.readline()
        while line:
            print(line, end='')
            line = file.readline()
            total = 0.0 
            count = 0  
            
            print("Sales Totals:")
            for line in file:
                sale = float(line.strip())
                print(f"${sale:.2f}")  
                total += sale         
                count += 1            

            
            average = total / count if count > 0 else 0

           
            print("\nSummary:")
            print(f"Total Sales: ${total:.2f}")
            print(f"Number of Sales: {count}")
            print(f"Average Sale: ${average:.2f}")


main()