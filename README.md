# Renpygame

**IMPORTANT**: This is a continuation of a project not mine, abandoned from 2008 [Renpygame](https://renpy.org/wiki/renpy/frameworks/Renpygame) (not working). Currently compared to 2008, it is not possible to directly use the [pygame_sdl2](https://github.com/renpy/pygame_sdl2) library, especially to "draw".

----

## TO DOWNLOAD THIS TEST PROJECT
```shell
# Basic command to download projects from git
git clone https://github.com/DRincs-Productions/Renpygame
# IMPORTANT -> Will add the libraries needed to run the program
cd Renpygame
git submodule update --init --recursive

```
----

Renpygame is a framework that allows pygame games to be integrated with Ren'Py. It's intended for people who are capable programmers.

The idea is to create a library that uses [pygame_sdl2](https://github.com/renpy/pygame_sdl2) and overrides functions that can be handled by the [renpy](https://github.com/renpy/renpy) library.

The big problem is that the mode for drawing is very different. The only way I found was to use [CDD](https://www.renpy.org/doc/html/cdd.html) and use that events to draw and update an element.

Use of events to draw limits a lot -> you can't create loops to update a renpy.Displayable -> that's why you can't copy and paste a game, but modify it slightly.

![ezgif com-video-to-gif](https://user-images.githubusercontent.com/67595890/236701292-d36a5f0f-d4e8-4e53-8671-a79fd903786b.gif)

## Other minigames

(Add topics `renpygame` to add it to the list)    
https://github.com/topics/renpygame

## Instructions

**[Wiki](https://github.com/DRincs-Productions/Renpygame/wiki)**

## Why use pygame-renpygame and not renpy-CDD?

pygame-renpygame's pros:

- You can use pygame and renpy functions
- huge number of minigames on github
- popularity (pygame is also often used in universities)
- typification (I am endeavouring to add the type everywhere)

renpy's pros:

- durability ([CDD](https://www.renpy.org/doc/html/cdd.html) is developed by the same developer as renpy)

## Performance

([in development](https://github.com/DRincs-Productions/Renpygame/issues/10))

(I don't made any tests for now) Renpygame use [CDD](https://www.renpy.org/doc/html/cdd.html) for draw and renpy for open a file, but I use a typification and is a external library. So, the performance is the same as renpy, excluding possible implementation errors.


## Insert Toolkit in your project

I recommend the following ways to include it in your project:

- [**Pull branch**](#pull-branch) (to **insert** it into your game and **update** it easily)
- [**Fork**](https://docs.github.com/en/get-started/quickstart/fork-a-repo) (to improve the repo or create a Toolkit based on mine)
- [Manually](https://github.com/DRincs-Productions/Renpygame/releases) (not recommended)

### Pull branch

To **insert** or **update** the Toolkit in your repo with Pull branch I recommend the following procedure:

(only if you want to insert the repo) Create a new empty branch, in the example I'll use **renpygame**

```shell
git checkout -b renpygame
git checkout renpygame
git config pull.rebase false
git pull https://github.com/DRincs-Productions/Renpygame.git tool-only --allow-unrelated-histories
git submodule update --remote

```

At the end make a merge inside the arm of the project.

## Supported Modules

A good number of functions should already work even if they have not yet been tested

- [ ] renpygame.color
- [x] renpygame.constants (Still to be tested, should already be working)
- [x] renpygame.cursors (Still to be tested, should already be working)
- [ ] renpygame.display (Incomplete)
- [x] renpygame.display.Surface
- [x] renpygame.draw
- [x] renpygame.event (Still to be tested, should already be working)
- [ ] renpygame.font
- [ ] renpygame.image (Incomplete)
- [ ] renpygame.joystick
- [ ] renpygame.key (Incomplete)
- [x] renpygame.locals (Still to be tested, should already be working)
- [ ] renpygame.mixer (Incomplete)
- [ ] renpygame.mixer.music (Incomplete)
- [x] renpygame.mouse (Still to be tested, should already be working)
- [x] renpygame.rect
- [ ] renpygame.sprite (Incomplete)
- [x] renpygame.time (Still to be tested, should already be working)
- [ ] renpygame.transform (Incomplete)
