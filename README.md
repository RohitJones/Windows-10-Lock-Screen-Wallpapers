# Windows-10-Lock-Screen-Wallpapers
This is a python script to copy those amazing windows 10 lockscreen wallpapers into a location of your choice (preferences are pending).

I don't know if this is pointless, but I've implemented a hashing system which hashes every file in the directory.
if the file has been previously copied, by the hashing system, we will know that it has and it won't be copied over again.
also, along with the wallpapers, there were junk pictures as well like ads, 
they were mostly small in size so i decided that anything less than 400KB is most likely junk and eliminated them from copying.

there is scope for improvement.
1) not sure just how memory efficeint the whole program is especially the hash calculating part
2) Letting the user set the copy destination (something like preferences)
3) classifying pictures as portrait or landscape
4) something more prehaps......?

Explanation time:

CacheHashes(): This is used to, well, cache the hashes of the PREVIOUSLY copied pictures. this is done so i don't copy duplicates

UpdateHashes(): Not very sure why i made this one but, in case the user manually copies some pictures into the destination folder 
                and wants to add the hashes of the new pics, this is what he needs

RebuildHashes(): Suppose you made a mess of the destination folder, added many files, deleted many files, 
                  you are gonna have lots of outdated and useless hashes sitting about.
                  This wipes out the previously made hashlist and creates a new one from scratch and includes all pics in the destination
                  directory

CopyPictures(): The meat of my script. does pretty much everything else.

main(): ok, some people like having a GUI. (not me.......(mostly))
