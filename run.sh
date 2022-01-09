python3 main.py main.mold mold > mold.c
echo "Built from Python"
./mold examples/simple.mold out
echo "Built from mold"
./out