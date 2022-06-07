
class Dog {
    public String name;
    public int age;
    public String breed;

    public Dog(String name, int age, String breed) {
        this.name = name;
        this.age = age;
        this.breed = breed;
    }

    public void getInfo() {
        System.out.println(name);
        System.out.println(age);
        System.out.println(breed);
        System.out.println();
    }

    public void speak() {
        System.out.println(name + ": 'woof'");
    }
}

public class Classes {
    public static void main(String[] args) {
        Dog myDog = new Dog("Benji", 5, "Lab");
        myDog.speak();
        myDog.getInfo();
    }
}
