// personal.js

// Function to get personal information
function getPersonalInfo() {
  return {
    name: 'John Doe',
    age: 30,
    email: 'john.doe@example.com',
    address: {
      street: '123 Main St',
      city: 'Anytown',
      state: 'CA',
      zip: '12345',
    },
    phoneNumbers: [
      {
        type: 'home',
        number: '555-555-5555',
      },
      {
        type: 'work',
        number: '555-555-5556',
      },
    ],
    hobbies: ['reading', 'traveling', 'coding'],
  };
}

// Function to display personal information
function displayPersonalInfo(info) {
  console.log(`Name: ${info.name}`);
  console.log(`Age: ${info.age}`);
  console.log(`Email: ${info.email}`);
  console.log(
    `Address: ${info.address.street}, ${info.address.city}, ${info.address.state} ${info.address.zip}`,
  );
  info.phoneNumbers.forEach((phone) => {
    console.log(`Phone (${phone.type}): ${phone.number}`);
  });
  console.log(`Hobbies: ${info.hobbies.join(', ')}`);
}

// Main function to execute the script
function main() {
  const personalInfo = getPersonalInfo();
  displayPersonalInfo(personalInfo);
}

// Execute the main function
main();
