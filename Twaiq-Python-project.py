info = {
  "1212121212":"mohammed"
}
Input = input('Your Name Or Phone Number: ').lower()
print("Sorry That's Error" if Input not in info.keys() and Input not in info.values() else [i for i in info.keys() if info[i]==Input][0] if Input in info.values() else info[Input])