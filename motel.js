// Reasonably complicated Object in JavaScript that contains attributes and methods for the Motelcustomer.

const MotelCustomer = { 
    //List for MotelCustomer 
    name: "Artem Hanzha",
    birthDate: new Date(2002, 7, 27), //Makes a date as 2002-7-27
    gender: "Male",
    roomPreference: ["Non-smoking", "Pets Allowed", "Room Size", "Number of Beds", "Price", "Close Amenities", "Safety and Security", "Room Condition", "Check-in/Check-out Times", "Reviews and Ratings", "Additional Services"], //List for room preference 
    paymentMethod: "Credit Card",
    mailingAddress: {
        street: "49 Howley Avenue Extension",
        city: "St John's", 
        province: "NL",
        country: "Canada",
        postalCode: "A1C2T6"
      },
    phoneNumber: "1-709-853-4449",
    checkInDate: new Date(2024, 6, 7), // Makes a new date (YEAR, MONTH, DAY)
    checkOutDate: new Date(2024, 6, 17), // Makes a new date (YEAR, MONTH, DAY)

    getAge: function() {
        const today = new Date(); // Creates a new Date object representing the current date, stored in the today variable.
        let age = today.getFullYear() - this.birthDate.getFullYear(); // Calculation to get age. uses today object and then minuses it by birthDate object
        return age; 
    },
//
    getDurationOfStay: function() {
        const millisecondsPerDay = 1000 * 60 * 60 * 24;
        const checkInTime = this.checkInDate.getTime();
        const checkOutTime = this.checkOutDate.getTime();
        const durationInMilliseconds = checkOutTime - checkInTime;
        return Math.ceil(durationInMilliseconds / millisecondsPerDay);
  }   

};
// The following list gets printed to the console. .join joins the roomPreference list together. Everything else is straight forward - calling functions. toDateString makes the date readable.  It returns a string in the format ddd MMM dd yyyy ddd = day of week | mmm = abbreviated month | dd day from 1-31 | yyyy - Take a guess. 
const customerDescription = `Name: ${MotelCustomer.name} 
Age: ${MotelCustomer.getAge()}
Gender: ${MotelCustomer.gender}
Room Preferences: ${MotelCustomer.roomPreference.join(', ')}
Payment Method: ${MotelCustomer.paymentMethod}
Mailing Address: ${MotelCustomer.mailingAddress.street}, ${MotelCustomer.mailingAddress.city}, ${MotelCustomer.mailingAddress.province}, ${MotelCustomer.mailingAddress.country}, ${MotelCustomer.mailingAddress.postalCode}
Phone Number: ${MotelCustomer.phoneNumber}
Check-In Date: ${MotelCustomer.checkInDate.toDateString()}
Check-Out Date: ${MotelCustomer.checkOutDate.toDateString()}
Duration of Stay: ${MotelCustomer.getDurationOfStay()} days`;


console.log(customerDescription); //sends to console
//Using values from my "roomPreference" list to create sentence abou room (elements 0-10 (11 elements))
let roomPreferenceSentence = `This luxurious hotel offers ${MotelCustomer.roomPreference[0]} with ${MotelCustomer.roomPreference[1]}, spacious ${MotelCustomer.roomPreference[2]}s, with a ${MotelCustomer.roomPreference[3]} options, competitive ${MotelCustomer.roomPreference[4]}s, ${MotelCustomer.roomPreference[5]}, top-notch ${MotelCustomer.roomPreference[6]}, impeccable ${MotelCustomer.roomPreference[7]}s, flexible ${MotelCustomer.roomPreference[8]}, stellar ${MotelCustomer.roomPreference[9]}, and a range of ${MotelCustomer.roomPreference[10]} to enhance your stay.`

console.log(roomPreferenceSentence); //sends to console