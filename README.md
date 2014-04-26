#Pantheon


###The Rebirth of a Desktop U.I.

This is a "rebirth" of the RetroArch Phoenix project that was deprecated.
This project provides RetroArch, and soon a new Libretro Api, with an all-in-one graphical interface that focuses on desktop use. This project draws heavy influence from the [OpenEmu](http://openemu.org/) frontend and so please show support for their hard work if you are running the Mac operting system. 
This project will provide a lot of the functionality that they have provided, which includes supporting shaders, configuring controllers, and playing games on your favorite emulator.

There will be two versions, one will be our frontend that will target the Libretro api, for tight integration with the latest Qt technology. The other version will be using RetroArch as a backend and will simply be a launcher. This frontend is free as in freedom and beer. If you wish to help with the frontend in any way, please feel free to contact me. This frontend is gets worked on almost daily and so features will soon be piling in.

This project is not officially supported by the Libretro Team and so please do not ask them questions about this frontend, I am happy to answer any questions that you may have.

The official version of RetroArch is located at this [site](http://www.libretro.com/). 

####How it works:

The frontend is built with [Qt 5.2.1](http://qt-project.org/downloads) and uses QML for designing the user interface and so, utilizes Javascript and C++. I use [pyotherside](http://thp.io/2011/pyotherside/) as an alternative to PyQt5 in order to provide scripting capabilities that are written in [Python 3.3](http://www.python.org/download/releases/3.3.3/). The frontend will work on Linux, OSX, and Windows; however these builds are tested almost exclusively on Windows, though I will periodically test them on Linux, OSX is currently unknown.

####Things that still need to be completed:

1. Rewrite Python functions in C++
2. Add controller mapping from within the frontend.
3. Make Rating system work.

####Meet The Developers:

My name is Lee and I am the creator of this project. I go by the name of Druage and you can contact me at Druage@gmx.com.

The other developer goes the name of TheCanadianBacon, and he is the reason for why this frontend is going to become it's own Libretro Api.
