# Decorator Pattern - Starbuzz Coffee

## Pattern Overview

### Intent
Attach additional responsibilities to an object dynamically. Decorators provide a flexible alternative to subclassing for extending functionality.

### Applicability
- To add responsibilities to individual objects dynamically and transparently, without affecting other objects.
- For responsibilities that can be withdrawn.
- When extension by subclassing is impractical. Sometimes a large number of independent extensions are possible and would produce an explosion of subclasses to support every combination. Or a class definition may be hidden or otherwise unavailable for subclassing.

### Key Participants
- **Component**: Defines the interface for objects that can have responsibilities added to them dynamically.
- **ConcreteComponent**: Defines an object to which additional responsibilities can be attached.
- **Decorator**: Maintains a reference to a Component object and defines an interface that conforms to Component's interface.
- **ConcreteDecorator**: Adds responsibilities to the component.

## Example Scenario

This example uses the classic "Starbuzz Coffee" scenario:
- Different types of coffee (Espresso, HouseBlend) serve as base components.
- Different condiments (Milk, Mocha, Soy) serve as decorators.
- Coffee and condiments can be dynamically combined.

Correspondence:
- `Beverage` → Component (beverage component)
- `Espresso`, `HouseBlend` → ConcreteComponent (concrete beverages)
- `CondimentDecorator` → Decorator (condiment decorator)
- `Milk`, `Mocha`, `Soy` → ConcreteDecorator (concrete condiments)

## How to Run

### Requirements
- Python 3.10+

### Run the Code
```bash
python starbuzz_coffee.py
```

### Expected Output
```
=== 订单 1: 浓缩咖啡 ===
Espresso $1.99
=== 订单 2: 深焙咖啡，双倍摩卡，加奶 ===
House Blend Coffee, Mocha, Mocha, Milk $1.49
=== 订单 3: 综合咖啡，加豆浆，加摩卡，加奶泡 ===
House Blend Coffee, Soy, Mocha, Whip $1.34
```

## Screenshot
(Please add a screenshot of the running program)
