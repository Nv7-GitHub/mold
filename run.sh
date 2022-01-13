python3 main.py main.mold mold > mold.cpp
echo "Built from Python"
./mold examples/simple.mold out
echo "Built from mold"
./out