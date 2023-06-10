import glob 
from pathlib import Path 
from output.utils import load_plug
import logging
from . import bot 


logging.basicConfig(format='[%(levelname) 5s/%(asctime)s] %(name)s: %(message)s', level=logging.WARNING)

path = "output/plugins/*.py"
files = glob.glob(path)

for name in files:
  with open(name) as a:
    pxt = Path(a.name)
    plugs = pxt.stem
    
    load_plug(plugs.replace(".py",""))
    
print("OUTPUT BOT STARTED & LOADED ALL PLUGINS")
 
if __name__ == "__main__":
  
  bot.run_until_disconnected()