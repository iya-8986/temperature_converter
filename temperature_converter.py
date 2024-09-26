#author__uy_thea
#date__September_25_2024
#this program will convert temperature from Celcius to Fahrenheit

#this program will also ask the user to input a temperature
#this program will ask the user to select the conversion type: from Celcius to Fahrenheit or from Fahrenheit to Celcius
#and finally, the program will calculate the appropriate conversion then print the result 

#create a loop for the whole program 
while True:
    while True:
        try:
            temperature = float(input("Enter the temperature: ")) #ask the user for the temperature input
            rounded_num_of_value = round(temperature) #round the temperature input
            if isinstance(rounded_num_of_value,int):
                break
        except ValueError: 
            print("Invalid Input")
            continue
    print("\n")

    while True:
        try:
            temperature_conversion = input("Enter conversion type:\nC = Farenheit to Celcius \nF = Celcius to Farenheit\nC or F? ") #ask the user for the conversion type
            temperature_conversion = temperature_conversion.upper()
        except ValueError:
            print("Invalid Input")
            continue

        if temperature_conversion == "C": #this code will execute if the user wants to convert the temperature from Farenheit to Celcius
                temperature_result =  ((temperature-32)*5) / 9
                temperature_result = round(temperature_result,2)
                print(f"The temperature is {temperature_result} \u00B0C")
                break
        elif temperature_conversion == "F": #this code will execute if the user wants to convert from Celcius to Fahrenheit
                temperature_result = ((temperature*9)/5) +32
                temperature_result = round(temperature_result,2)
                print(f"The temperature is {temperature_result} \u00B0F")
                break    
    
#Ask user if he/she wants to try again
    while True:
        ans = str(input("Do you want to try again? Yes or No: "))
        upper_ans = ans.upper()
        if upper_ans == "YES":
            break
        elif upper_ans == "NO":
            print("\nThank you for using my program!")
            exit()
        else:
            print("Invalid Input")
    
#end of the program 

    

