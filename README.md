# The lift simulator

The simulator consists of the following classes
- Person
- Floor
- Lift
- Building
- Controller

## Person

The person class represents an individual waiting for a lift. It has the following methods.

* `location` will return the current location of the person. This will either be a `Floor` object, or a `Lift` object.
* `targetLocation` will return where the person wants to go. If this information is only available when the person is in a lift (i.e., they have to press a button), then this will return -1.
* `creationTime` will return when the person started their journey
* `enterLift(lift)` will allow the person to enter lift `lift`.
* `exitLift` will cause the person to exit the lift to the current floor they are on.

## Floor

This represents a floor of the building. It has the following methods
* `number` will return the floor number of the floor.
* `waitingPeople` will return a set of people waiting for a lift.

## Lift

This represents a lift. It has the following methods.

* `people` will return a set of Person objects in the lift.
* `location` will return an integer floor number if the lift is on some floor. It will return -1 otherwise.
* `capacity` returns the capacity of the lift (number of people that can be on it).
* `minFloor` and `maxFloor` are the first and last floors served by the lift.
* `doorOpen` is a boolean representing whether the door is open or not. Note that the door will remain open (after being told to close), until it is closed.
* `doorClosed` is a boolean representing whether the door is closed or not.
* `destination` captures the destination floor (as an int). Note that the door will remain closed (after being told to open), until it is open.
* The `openDoor` method will cause the doors to open, and the `closeDoor` method will cause them to close.
* `destination(floor)` will set the lift's destination to `floor` (an int), while `destination` will return the lift's current destination.

## Building

This represents the entire building. Methods available are `floors`, `lifts` and `time` which respectively return the list of floors on the building, the set of lifts, and the current time.

## Controller

Controller has a method `building(self,building)`, which will be passed the building object when the simulation starts. At every time instant, the controller will have its `tick` method invoked with the current time as a parameter. 
Then the lifts will move , and  people will enter/leave lifts (if the doors are open or closed) according to the controller setting.

# Using the simulator

The last two lines in the simulator file show how the simulator is run by repeatedly calling the `building.tick()` method. To use your own controller, just change the line that says `controller=Controller()` to your own controller class (and import that class at the top of your file). See the sample controller for details.

