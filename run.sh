python3 main.py main.mold mold > mold.cpp # Python: Src => mold
echo "Built from Python"
./mold main.mold out # Mold: Src => out
echo "Built from mold"
./out main.mold out2 # Mold (self compiled): Src => out2
echo "Built from mold (self compiled)"