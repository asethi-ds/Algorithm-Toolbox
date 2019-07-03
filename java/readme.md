#### Variable Type
* Conversion of float to int is truncation `(int)1.99 == 2`
```java
// declare
int x;

// assign
x = 12;

int a = 5;

// double precision decimal
double b = 1.2;

boolean c = true;

// single quote for char
char letter = 'c';

// double quote for string
String sen = "hell";
```


#### Keyword
* `private`: keep private so that only method in same class can access.
* `static`: class property, not instance property.
* `final`: read-only.

#### Logical Operator
| Operator   | Meaning     |
| :--------- | :---------- |
| `&&`       | AND         |
| `||`       | OR          |
| `!`        | NOT         |

* Short-circuited evaluation: from left to right. If one fails, no need to proceed.
* De-morgan's Law: `!(q && p)` === `!q && !p`

#### Statement
* Simple statement: an expression followed by a semicolon.
* Compound statement (block): function
* Control statement:
  - conditionals
  - iterations
  - ? Operator: `condition ? expression_1 : expression_2`

```java
// single line if
if (condition) statement;

// multiple line if
if (condition) {

}

// if-elf
if (condition) {

} else {

}

// cascading
if (condition) {

} else if (condition2) {

} else {

}

switch (err) {
  case 0:
    statement;
    break;
  case 1:
    statement;
    break;
  default:
    statement;
    break;
}
```

#### Step-wise Refinement
* Begin by thinking about the program as a whole.
* Divide program into major components.
* At the end, have a set of individual tasks.
