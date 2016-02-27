echo You must install xcode command line tools, at the prompt click install
xcode-select --install
python3 check.py
echo Making Files..
(echo python3 main.py) > start.sh 
echo Configuring Files..
chmod +x start.command
echo Done!
exit