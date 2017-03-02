# Install MuticoreTSNE on windows
I used cmake3.7.1(cmake-gui)  (https://cmake.org/download/) for building MuticoreTSNE on windows. 
```
1. Clone or download source code. 
2. The CMakeLists.txt is ./multicore_tsne/CMakeLists.txt. 
3. Open ./multicore_tsne/Project.sln. 
4. Set configuration to Release and x64 
5. Press F7 to build.
6. The dll file is in ./multicore_tsne/Release/ after built. 
```

You move to windows directory and install it using following commands 
```
python setup.py install 
```
