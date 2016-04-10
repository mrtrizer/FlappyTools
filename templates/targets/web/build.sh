mkdir build
cd build
emconfigure cmake
emmake make
emcc CMakeFiles/{!cmake.exec_name!}.dir/src/main.cpp.o modules/{!cmake.exec_name!}/libFlappyCxx.so modules/engine/libFlappyEngine.so --preload-file ./res/@/res/ --use-preload-plugins -o test.html
cd ..
