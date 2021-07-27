# *BounceFX*

**Table of contents**
*   [Definition](#definition)
*   [Details](#details)
*   [Requirements](#requirements)
*   [Contact](#contact)
*   [Useless facts](#useless-facts)

----

## Definition

The *BounceFX* module allows printing a string with a bouncing effect from left to right.

:keyboard: If you are interested in a typewriter effect text printer module, you can find it [here](https://github.com/urbanware-org/typefx).

:arrows_clockwise: There also is a character flipping effect text printer module  [here](https://github.com/urbanware-org/flipfx).

[Top](#bouncefx)

## Details

The given string is printed on the left of the current line, moving to the right side column by column until the string reaches the end of the line. The length of the line can either be a given value (e.g. 80 characters) or automatically determined (depending on the terminal size). Then, the string bounces and moves left column by column again.

### Usage

First of all, the module must be imported.

```python
import bouncefx
```

#### Method

Notice that the delay must be given in milliseconds.

The method requires four arguments:

*   `string`
    *   The string that should be bounced in the line.
*   `line_length`
    *   The length in characters that should be used for bouncing. Setting this to `0` will automatically determine the length (columns) of the terminal line.
*   `delay`
    *   The delay between moving the string left or right.
*   `bounces`
    *   The number of bounces that should be done. Setting this to `0` results in unlimited bounces.

```python
bouncefx.bounce_line(string, line_length=80, delay=0.1, bounces=3)
```

#### Example

The following code

```python
import bouncefx
bouncefx.bounce_line("This is an example.", line_length=38, delay=0.1, bounces=0)
```

produces this output:

<img src="https://raw.githubusercontent.com/urbanware-org/bouncefx/master/gif/bouncefx.gif" alt="BounceFX sample output">

[Top](#bouncefx)

## Requirements

In order to use *BounceFX*, the *Python* 3.x framework (version 3.2 or higher is recommended) must be installed on the system.

There is no official version for *Python* 2.x, but if you need that for whatever reason, you can try refactoring the syntax from *Python* 3.x to version 2.x using the *[3to2](https://pypi.python.org/pypi/3to2)* tool.

[Top](#bouncefx)

## Contact

Any suggestions, questions, bugs to report or feedback to give?

You can contact me by sending an email to [dev@urbanware.org](mailto:dev@urbanware.org) or by opening a *GitHub* issue (which I would prefer if you have a *GitHub* account).

[Top](#bouncefx)

## Useless facts

*   The project name is an abbreviation for *Bounce Effects*.

[Top](#bouncefx)
