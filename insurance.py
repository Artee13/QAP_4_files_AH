# Description: "ONE STOP INSURANCE COMPANY" program to calculate new insurance 
# Author: Artem Hanzha
# Date(s): 22 Mar 2024
 
 
# Define required libraries.
import datetime
import FormatValues as FV
import re

# Headings print 
print()
print("ONE STOP INSURANCE COMPANY")
print("===============================================")

# Default Values
POLICY_NUMBER = 1944
BASIC_PREMIUM = 869.00 
ADD_CAR_DISC = .25 
EXTRA_LIABILITY_COV = 130.00
GLASS_COV = 86.00 
LOANER_COV = 58.00 
HST = .15 
MONTHLY_PAY_FEE = 39.99
PROVINCES = ['AB', 'BC', 'MB', 'NB', 'NL', 'NS', 'NT', 'NU', 'ON', 'PE', 'QC', 'SK', 'YT']
PAYMENT_OPTIONS = ['Full', 'Monthly', 'Down Pay']



# Define program functions

# Function to validate province
def get_valid_province():
    Province = input("Enter province abbreviation (ex: NL): ").upper()
    while Province not in PROVINCES:
        print("Invalid province. Please enter a valid province.")
        Province = input("Enter province abbreviation (ex: NL): ").upper()
    return Province 

def get_payment_option():
    while True:
        PaymentOption = input("Payment Option (Full/Monthly/Down Pay): ").title()

        if PaymentOption not in PAYMENT_OPTIONS:
          print("Invalid payment option")
        else:
            return PaymentOption
        
def calculate_monthly_payment(TotalCost, DownPayment):
    if DownPayment > 0:
        TotalCost -= DownPayment
    MonthlyPayment = (TotalCost + MONTHLY_PAY_FEE) / 8
    return MonthlyPayment

def validate_down_payment(DownPayment):
    if not DownPayment.strip():  # Checks if input is empty or contains blankspace
        return False, "Input cannot be empty."
    
    if not DownPayment.replace('.', '', 2).isdigit():  # Check if the input is a number (allowing for two decimal point)
        return False, "Invalid input. Please enter a valid number for the down payment."
    
    DownPayment = float(DownPayment)
    if DownPayment >= 0:
        return True, DownPayment
    else:
        return False, "Down payment must be a positive number."

def validate_date(date_str):
    try:
        datetime.datetime.strptime(date_str, '%Y-%m-%d')
        return True
    except ValueError:
        return False
    
Claims = []

def get_claims(Claims):
    print()
    print("Enter previous claim data. Type '000' in the claim number input to end.")
    print()
    while True:
        ClaimNumber = input("Enter claim number: ")
        if ClaimNumber == "000":
            break
        elif not ClaimNumber.isdigit():
            print("Please enter a valid claim number.")
            continue

        while True:
            ClaimDate = input("Enter claim date (YYYY-MM-DD): ")
            if ClaimDate == "000":
                break
            try:
                datetime.datetime.strptime(ClaimDate, '%Y-%m-%d')
            except ValueError:
                print("Invalid date format. Please enter the date in (YYYY-MM-DD) format.")
                continue
            else:
                break

        if ClaimDate == "000":
            break
        
        while True:
            try:
                ClaimAmount = float(input("Enter claim amount: "))
                ClaimAmount = FV.FDollar2(ClaimAmount)
                break
            except ValueError:
                print("Please enter a valid number for claim amount.")
                continue

        # Check for duplicate claim number
        for claim in Claims:
            if claim['Claim Number'] == ClaimNumber:
                print("Please enter a different claim number.")
                break
        else:
            Claims.append({'Claim Number': ClaimNumber, 'Claim Date': ClaimDate, 'Claim Amount': ClaimAmount})
            print("Claim added successfully.")

    return Claims

# Main Program 


    #Inputs
     
while True: 
    print()
    print("Enter customer information below:")
    print()

    while True:
        FirstName = input("Enter customer's first name: ").title()
        if FV.validate_name(FirstName):
            break
        else:
            print("Invalid input. Please enter a valid first name. Cannot contain special characters, digits or spaces. ")
    while True:
        LastName = input("Enter customer's last name: ").title()
        if FV.validate_name(LastName):
            break
        else:
            print("Invalid input. Please enter a valid last name. Cannot contain special characters, digits or spaces. ")
    while True:
        StAddress = input("Enter customers street address: ").title() #Address validation 
        if FV.validate_street_address(StAddress):
            break
        else:
            print("Invalid street address. Input valid street address Example '123 Freshwater Road/rd")
    
    while True:
        City = input("Enter customers City: ").title() #Validate a city format 
        if FV.validate_city(City):
            break
        else: 
            print("Invalid input. Please enter a valid city name. You're bein bad, you cannot include numbers or special characters.")


    Province = get_valid_province() 

    while True:
        PostalCode = input("Enter customers Postal Code: (X#X#X#) ").upper()  #Psotal code validation 
        if FV.validate_postal_code(PostalCode):
            break
        else:
            print("Enter a valid postal code ex:\"A1B2C3\"")

    while True:            
        PhoneNumber = input("Enter customers Phone Number: ") #Phone num validation (doesn't work)
        if FV.validate_phone_number(PhoneNumber):
            PhoneNumber = str(PhoneNumber)
            break
        else:
            print("Enter a valid phone number of 10 digits ex:\"7091112233\"")

    while True:
        NumCars = input("Enter customer's number of cars: ")
        if FV.is_integer(NumCars):
            NumCars = int(NumCars)
            break
        else:
            print("Please enter a valid integer.")

    while True:
        ExtraLiability = input("Enter if customer wants extra liability coverage (Y/N): ").upper()
        if ExtraLiability in ['Y', 'N']:
            break
        else:
            print("Invalid input. Please enter 'Y' or 'N'.")

    while True:
        GlassCoverage = input("Enter if customer wants Glass coverage (Y/N): ").upper()
        if GlassCoverage in ['Y', 'N']:
            break
        else:
            print("Invalid input. Please enter 'Y' or 'N'.")

    while True:
        LoanerCar = input("Enter if customer wants Loaner car (Y/N): ").upper()
        if GlassCoverage in ['Y', 'N']:
            break
        else:
            print("Invalid input. Please enter 'Y' or 'N'.")


     #Calculations
    Name = FirstName + " " + LastName    
    TotalCost = BASIC_PREMIUM + (int(NumCars) - 1) * (BASIC_PREMIUM * ADD_CAR_DISC)
    TotalExtraCost = 0
    if ExtraLiability == "Y":
        TotalCost += int(NumCars) * EXTRA_LIABILITY_COV
        TotalExtraCost += int(NumCars) * EXTRA_LIABILITY_COV
    if GlassCoverage == "Y":
        TotalCost += int(NumCars) * GLASS_COV
        TotalExtraCost += int(NumCars) * GLASS_COV
    if LoanerCar == "Y":
        TotalCost  += int(NumCars) * LOANER_COV
        TotalExtraCost  += int(NumCars) * LOANER_COV

    HST = TotalCost * HST
    TotalCost += HST
    PaymentOption = get_payment_option()
    while True:
        if PaymentOption == 'Down Pay':
            while True:
                try:
                    DownPayment = input("Enter customer's down payment amount: ")
                    ValidatedDownPayment = validate_down_payment(DownPayment)
                    if ValidatedDownPayment:
                        DownPayment = float(DownPayment)
                        break
                except ValueError:
                    print("Invalid input. Please enter a valid number for the down payment.")
            if DownPayment > TotalCost:
                print("Down payment can't be higher than total cost.")
            else:
                break
        else:
            DownPayment = 0
            break  
    InsurancePremium = TotalCost - HST
    if PaymentOption == 'Full':
        PaymentAmount = TotalCost
        MonthlyPayment = 0.0
    else:
        PaymentAmount = TotalCost + MONTHLY_PAY_FEE
        MonthlyPayment = calculate_monthly_payment(TotalCost, DownPayment)
    
    CurrentDate = datetime.datetime.now()
    InvoiceDate = CurrentDate.strftime("%Y-%m-%d")
    NextMonth = (CurrentDate + datetime.timedelta(days=31)).strftime("%Y-%m-%d")
    Year = CurrentDate.year + (CurrentDate.month // 12)
    Month = 1 if CurrentDate.month == 12 else CurrentDate.month + 1
    NextMonth = datetime.datetime(Year, Month, 1).strftime("%Y-%m-%d")
    FirstPaymentDate = NextMonth


    get_claims(Claims)
        
    
        #Set up displays if needed
    NumCarsDsp = str(NumCars)
    if ExtraLiability == "Y":
        ExtraLiabilityDSP = "Yes"
    else: 
        ExtraLiabilityDSP = "No"
    if GlassCoverage == "Y":
        GlassCoverageDSP = "Yes"
    else: 
        GlassCoverageDSP = "No"
    if LoanerCar == "Y":
        LoanerCarDSP = "Yes"
    else: 
        LoanerCarDSP = "No"
    if PaymentOption == 'Down Pay':
        PaymentOptionDsp = "Down Payment"
    elif PaymentOption == "Full":
        PaymentOptionDsp = "Full Payment"
    else:
        PaymentOptionDsp = "Monthly Payment"
     


#Display results
    print()
    print("======================================================================")
    print(f"                       The One Stop Insurance         Receipt#{POLICY_NUMBER:<5}")
    print("======================================================================")
    print(f"                        Customer Information:                       ")
    print("====================================================================")
    print(f"")
    print(f"                    Name                  : {Name:<20s}")
    print(f"                    Street Address        : {StAddress:<20s}")
    print(f"                    City                  : {City:<20s}")
    print(f"                    Province              : {Province:<2s}")
    print(f"                    Postal Code           : {PostalCode:<6s}")
    print(f"                    Phone Number          : {PhoneNumber:<10s}")
    print(f"")
    print("====================================================================")
    print("                              Extras:                               ")
    print("====================================================================")
    print(f"")
    print(f"                    Number of cars        : {NumCarsDsp:<4s}")
    print(f"                    Extra Liability       : {ExtraLiabilityDSP:<3s}")
    print(f"                    Glass Coverage        : {GlassCoverageDSP:<3s}")
    print(f"                    Loaner Car            : {LoanerCarDSP:<3s}")
    print(f"                    Payment Option        : {PaymentOptionDsp:<15s}")
    print(f"")
    print("====================================================================")
    print("                        Payment Information:                        ")
    print("====================================================================")
    print(f"")
    print(f"                    Down Payment Amount   : {FV.FDollar2(DownPayment):<10s}")
    print(f"                    Monthly Payment Amount: {FV.FDollar2(MonthlyPayment):<10s}")
    print(f"")
    print(f"                    Total Extra Cost      : {FV.FDollar2(TotalExtraCost):<10s}")
    print(f"")
    print(f"                    Insurance Premium     : {FV.FDollar2(InsurancePremium):<10s}")
    print(f"                    HST                   : {FV.FDollar2(HST):<10s}")
    print(f"                    Total Cost            : {FV.FDollar2(TotalCost):<10s}")   
    print(f"")
    print("====================================================================")
    print(f"                           Payment Dates:                           ")
    print("====================================================================")
    print(f"                                                                    ")
    print(f" Invoice Date: {InvoiceDate:<10s}            First Payment Date: {FirstPaymentDate:<10s} ")
    print(f"                                                                    ")
    print("====================================================================")
    print(f"                           Previous Claims                          ")
    print("====================================================================")
    print(f"        Claim Number:        Claim Date:          Amount:           ")
    print("====================================================================")
    for claim in Claims:
        print(f"           {claim['Claim Number']:>5}              {claim['Claim Date']:<10}          {claim['Claim Amount']:<10}")
    print("====================================================================") 
    print()
    print()
    print("Claim data successfully saved ...", end='\r')
    print()
    POLICY_NUMBER += 1
    print()
    if input("Do you want to enter another customer information? Enter 'Y' if you want to continue, or anything else if you want to stop.: ").upper() != 'Y':
        break
