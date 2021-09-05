info = {
  "1212121212":"mohammed" # For Example
}
Input = input('Your Name Or Phone Number: ').lower()
print("Sorry, The number is not found" if Input not in info.keys() and Input not in info.values() else "This is invalid number" if len([i for i in Input if i in "0123456789"])!=len(Input) else [i for i in info.keys() if info[i]==Input][0] if Input in info.values() else info[Input])
