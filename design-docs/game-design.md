# Grim Reaply Game Design Document
This document is a work in progress to reflect the ongoing design process for Grim Reaply.

## Current document usage
QUESTION: a question that requires an answer e.g. through research or prototyping.
OPTIONS: as above but a choice is to be made from given options.
FALLBACK: backup feature should the intended feature prove too impractical or costly.
TODO: a task outside the document e.g. prototype a feature.
TOADD: something to add to the document e.g. examples or further explanation.

# Grim Reaply Overview
Grim Reaply is a single-player RPG with the grim reaper as the player's character.

## Story
The player travels the human world, meeting, talking to, and reaping the souls of the characters they meet. Grim answers to a boss, and is expected to reap souls grimly, unlike other reapers (e.g. the whimsical reaper).

## Themes
Death, mortality, time, preciousness of human life, duty, remorse, choices, inevitablity, disconnect.

## Tone and mood
Bleak, gothic, dark, slow, grimey. Sometimes cute, flamboyant.

## Core game mechanics
There are various navigable areas within the human and reapers' worlds. Grim can converse with characters, and choose when and how to reap a soul, e.g. by touch or by scythe. Grim can level up various attributes, and equip various items e.g. different scythes.
QUESTION: What effect would touch have vs. scythe? Does it affect levelling up, or hidden personality traits and future conversation options?
OPTIONS:
- Dialogue resembles combat. (Soul drains naturally through conversation - readiness to die increases. Touch is last resort or low readiness to die increases guilt.) 
- Dialogue is separate to combat.
- Combat is an option during dialogue.

## Endgame and player goals
QUESTION: Endgame and player goals unknown.
Grim may expect their soul to be reaped in the future. How they play may determine who reaps their soul and how, and where it ends up.
If Grim has the chance to befriend or romance humans and chooses not to reap their souls, their future may form an important part of the story, or a possible game end.
Grim could give up their job.

# Implementation and assets

## Engine
OPTIONS: RenPy, RPGMaker, Unity.
The current plan is to make prototypes in RenPy and see if this will work for the final product.
RenPy is a visual novel engine, and a lot can be done with background images, character sprites, text and dialogue options, custom interactive screens (e.g. inventory), and sound. If continuing with this style it may be worth switching to Unity to allow more customisation. 1st/3rd person 3D using Unity is an option but may be costly in time or if paying for assets.
Many aspects of the game such as dialogue, OOP classes, and inventory/attribute screens may be easily transferable between engines/languages.

## Art
The game may have a single art style, or two contrasting styles for the human and reapers' worlds.
OPTIONS:
Photography. Black and white, grainy. Option to hire actors/models for the characters.
Photography. Modeled miniature rooms etc.
Pixel art. Cute.
Pixel art. Dark / abstract.
Painting - hired artist.
Costly - learn digital art myself.

## Music
I will write and produce the music myself, most likely within Logic.
A lot of sparse sounds. Detachment.

# Research and references
The Seventh Seal - Bergman
Grim Adventures of Billy & Mandy
Hollow Knight
Mort - Terry Pratchett
The Scythe - Ray Bradbury
Grim Fandango