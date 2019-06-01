# StJudeSouls
My event-editing setup for the mod made for LobosJr in May 2019. First serious use of my soulstruct package, which let 
me make this in just a couple of weeks. (Other mod files not provided, but you can find them on Nexus soon.)

You will need to install `soulstruct` before you can run the compiler or use Python intelli-sense.

Brief summary of my process:
* The vanilla EVS files were created by 'decompiling' the EMEVD files. In my case, these are actually decompiled
"Prepare to Die Edition" events, as I haven't fully mapped out all the extra DSR stuff they added (which is mostly
useless arena stuff anyway).
* I edited the EVS files. Some weren't changed at all (for maps never visited in the mod). Some of the changes are
pretty crude; you can see I just commented out the `RunEvent` instructions in the (pre-)constructor events in places.
I also didn't bother to rename any of the events I wasn't really interested in.
* Constants are defined in the `*_constants.py` files and imported into the EVS scripts. This is my recommended setup,
and it will allow you to use the best parts of `soulstruct`, such as simply writing `if FLAG.SolaireRecruited: ...` as
a shortcut for conditional instructions based on a flag being enabled.
* You can use the `Await(...)` instruction to halt the event until a condition is met, or use the built-in `await`
Python keyword, which I've hijacked in the EVS parser. (Note that the `await` keyword is low in the order of operations
and you'll need parentheses around multi-part conditions for valid syntax.) 
* EVS files are recompiled in the `compile_all_emevd.py` script, which detects the appropriate EMEVD file name to create
based on the `Map()` constants that come with `soulstruct`, and applies DCX compression for DSR. Running this script is
all you need to do to immediately update the game's active EMEVD files (once you set the DSR path variable to the 
appropriate directory). Just quit to the game menu and reload to see your changes.
* The compile script will also spit out numeric and verbose versions of your built scripts into the appropriate
directories. This was mostly useful for me to spot small bugs in the EVS parser, which I've now fixed, but you may want
to read the verbose version yourself (which is based on HotPocketRemix's original verbose template).
