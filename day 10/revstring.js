function revstring(str){
    let rev = ''
    for (let char = 0; char < str.length; char++ ){
        rev = str[char]+rev;
    }
    console.log("The reverse of the string is:", rev);
}
// Example usage
revstring("aditya"); // Output: "olleh"