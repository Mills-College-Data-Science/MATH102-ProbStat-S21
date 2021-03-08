import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import ipywidgets as widgets
from ipywidgets import interact, interactive, fixed, interact_manual 
from IPython.display import Image, display

# simple function to generate heads and tails flips 
def flip_coins(trials):
    flips = np.random.randint(low=0, high=2, size=trials)
    
    events = {"Heads": 0, "Tails": 0}
        
    for n in range(trials):
        if(flips[n] == 0):
            events["Heads"] = events.get("Heads") + 1
        else:
            events["Tails"] = events.get("Tails") + 1

    keys = events.keys()
    values = events.values()
    plt.bar(keys, values, color = ["cyan","orange"])
    plt.ylabel("# of Flips")
    plt.ylim(0, int(trials))
    
    labels = [events.get("Heads"), events.get("Tails")]
    plt.text(x = -0.05, y = labels[0] + 0.4, s = labels[0], size = 20)
    plt.text(x = 0.90, y = labels[1] + 0.4, s = labels[1], size = 20)

# simple function to generate pairs of heads and tails flips
def flip_coins_pairs(trials):
    trials *= 2
    flips = np.random.randint(low=0, high=2, size=trials)
    
    events = {"HH": 0, "TH": 0, "HT": 0, "TT": 0}
    
    for n in range(0, trials, 2):
        if(flips[n] == 0 and flips[n + 1] == 0):
            events["HH"] = events.get("HH") + 1
        if(flips[n] == 1 and flips[n + 1] == 0):
            events["TH"] = events.get("TH") + 1
        if(flips[n] == 0 and flips[n + 1] == 1):
            events["HT"] = events.get("HT") + 1
        if(flips[n] == 1 and flips[n + 1] == 1):
            events["TT"] = events.get("TT") + 1

    keys = events.keys()
    values = events.values()
    plt.bar(keys, values, color = ["blue","yellow","green","red"])
    plt.ylabel("# of Flips")
    plt.ylim(0, int(trials))
    
    labels = [events.get("HH"), events.get("TH"), events.get("HT"),events.get("TT")]
    plt.text(x = -0.1, y = labels[0] + 0.4, s = labels[0], size = 20)
    plt.text(x = 0.90, y = labels[1] + 0.4, s = labels[1], size = 20)
    plt.text(x = 1.90, y = labels[2] + 0.4, s = labels[2], size = 20)
    plt.text(x = 2.90, y = labels[3] + 0.4, s = labels[3], size = 20)
    
# simple function to generate three heads and tails flips
def flip_coins_triples(trials):
    trials *= 3
    flips = np.random.randint(low=0, high=2, size=trials)
    
    events = {"HHH": 0, "THH": 0, "HTH": 0, "TTH": 0, "HHT": 0, "THT": 0, "HTT": 0, "TTT": 0}
    
    for n in range(0, trials, 3):
        if(flips[n] == 0 and flips[n + 1] == 0 and flips[n + 2] == 0):
            events["HHH"] = events.get("HHH") + 1
        if(flips[n] == 1 and flips[n + 1] == 0 and flips[n + 2] == 0):
            events["THH"] = events.get("THH") + 1
        if(flips[n] == 0 and flips[n + 1] == 1 and flips[n + 2] == 0):
            events["HTH"] = events.get("HTH") + 1
        if(flips[n] == 1 and flips[n + 1] == 1 and flips[n + 2] == 0):
            events["TTH"] = events.get("TTH") + 1
        if(flips[n] == 0 and flips[n + 1] == 0 and flips[n + 2] == 1):
            events["HHT"] = events.get("HHT") + 1
        if(flips[n] == 1 and flips[n + 1] == 0 and flips[n + 2] == 1):
            events["THT"] = events.get("THT") + 1
        if(flips[n] == 0 and flips[n + 1] == 1 and flips[n + 2] == 1):
            events["HTT"] = events.get("HTT") + 1
        if(flips[n] == 1 and flips[n + 1] == 1 and flips[n + 2] == 1):
            events["TTT"] = events.get("TTT") + 1

    keys = events.keys()
    values = events.values()
    plt.bar(keys, values, color = ["blue","yellow","green","red","purple","cyan","orange","violet"])
    plt.ylabel("# of Flips")
    plt.ylim(0, int(trials))
    
    labels = [events.get("HHH"), events.get("THH"), events.get("HTH"),events.get("TTH"),events.get("HHT"), events.get("THT"),events.get("HTT"),events.get("TTT")]
    plt.text(x = -0.1, y = labels[0] + 0.4, s = labels[0], size = 20)
    plt.text(x = 0.90, y = labels[1] + 0.4, s = labels[1], size = 20)
    plt.text(x = 1.90, y = labels[2] + 0.4, s = labels[2], size = 20)
    plt.text(x = 2.90, y = labels[3] + 0.4, s = labels[3], size = 20)
    plt.text(x = 3.9, y = labels[4] + 0.4, s = labels[4], size = 20)
    plt.text(x = 4.9, y = labels[5] + 0.4, s = labels[5], size = 20)
    plt.text(x = 5.9, y = labels[6] + 0.4, s = labels[6], size = 20)
    plt.text(x = 6.9, y = labels[7] + 0.4, s = labels[7], size = 20)
    

# simple function to generate heads and tails flips 
def flip_coins_biased(trials, heads_bias):
    flips = np.random.random(trials)
    events = {"Heads": 0, "Tails": 0}
        
    for n in range(trials):
        if(flips[n] < heads_bias):
            events["Heads"] = events.get("Heads") + 1
        else:
            events["Tails"] = events.get("Tails") + 1

    keys = events.keys()
    values = events.values()
    plt.bar(keys, values, color = ["cyan","orange"])
    plt.ylabel("# of Flips")
    plt.ylim(0, int(trials))
    
    labels = [events.get("Heads"), events.get("Tails")]
    plt.text(x = -0.05, y = labels[0] + 0.4, s = labels[0], size = 20)
    plt.text(x = 0.90, y = labels[1] + 0.4, s = labels[1], size = 20)