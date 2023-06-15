Probability Calculator

This project provides a probability calculator implemented in Python. It includes a Hat class and an experiment function for performing probability experiments with randomly drawn balls from a hat.
Hat Class

The Hat class represents a hat containing different colored balls. It has the following features:

    Initialization: The Hat class takes a variable number of arguments that specify the number of balls of each color in the hat. For example, a Hat object can be created as follows:

    python

    hat = Hat(yellow=3, blue=2, green=6)

    draw method: This method accepts an argument indicating the number of balls to draw from the hat. It removes balls at random from the hat's contents and returns those balls as a list of strings. The balls are drawn without replacement, meaning they won't go back into the hat during the draw. If the number of balls to draw exceeds the available quantity, all the balls are returned.

Experiment Function

The experiment function performs probability experiments using the Hat class. It accepts the following arguments:

    hat: A Hat object containing the initial set of balls.
    expected_balls: An object indicating the exact group of balls to attempt to draw from the hat for the experiment.
    num_balls_drawn: The number of balls to draw out of the hat in each experiment.
    num_experiments: The number of experiments to perform.

The experiment function calculates the probability of getting the expected set of balls by repeatedly drawing balls from the hat. The more experiments performed, the more accurate the approximate probability will be.

Here is an example of how to use the experiment function:

python

hat = Hat(black=6, red=4, green=3)
probability = experiment(hat=hat,
                         expected_balls={"red": 2, "green": 1},
                         num_balls_drawn=5,
                         num_experiments=2000)

Usage

To use the probability calculator, follow these steps:

    Create an instance of the Hat class by specifying the number of balls of each color in the hat.
    Call the experiment function, passing the Hat object, the expected set of balls, the number of balls to draw, and the number of experiments.
    Retrieve the calculated probability from the experiment function's return value.

Example

Here is an example that demonstrates the usage of the probability calculator:

python

hat = Hat(black=6, red=4, green=3)
probability = experiment(hat=hat,
                         expected_balls={"red": 2, "green": 1},
                         num_balls_drawn=5,
                         num_experiments=2000)
print(f"The probability is: {probability}")

Conclusion

The probability calculator provides a convenient way to estimate the probability of drawing specific combinations of balls from a hat. By utilizing the Hat class and the experiment function, you can perform numerous experiments and obtain approximate probabilities. Feel free to explore and use this tool to analyze different probability scenarios.

The unit tests for this project are available in the test_module.py file. Running the main.py will run all the tests automatically which can help ensure the correctness of the implemented functionality.

Please refer to the project files for further details and implementation specifics
