//class
class Me(){
  String name;
  String phone;
  int age;
  String country;
  String hobby;
  bool graduatePLP;
}

//constructor
  me(this.name, this.phone, this.age, this.country, this.hobby){

//function for displaying the values
  void display(){
    print(`My name is :$name`);
    print('Phone number: $phone');
    print('I am $age years old');
    print("I live in $country");
    print('I love $hobby');
    print($graduatePLP)
}
}

//main function where the compilation starts

void main(){
  var obj=Me('Shaleen', '0711547663', 21, 'Kenya', 'Singing', false);
  obj.display();
}