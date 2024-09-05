"""
Game Name: Wordly
Description: Player guesses letters in a 5 letter word
Author: Zachary Coe
Date: 2024-09-04
"""


import random


WORDS_LIST = ["abbey", "about", "above", "abuse", "actor", "acute", "adapt", "admit", "adobe", "adopt",
    "adult", "after", "again", "agent", "aging", "agony", "agree", "ahead", "aisle", "alarm",
    "album", "alert", "alien", "align", "alike", "alive", "alley", "allow", "alloy", "alone",
    "along", "aloud", "alpha", "altar", "alter", "amber", "amend", "amino", "among", "ample",
    "angel", "anger", "angle", "angry", "ankle", "apart", "apple", "apply", "arena", "argue",
    "arise", "armor", "arose", "array", "arrow", "aside", "assay", "asset", "atlas", "audio",
    "audit", "avoid", "await", "awake", "award", "aware", "awful", "bacon", "badge", "badly",
    "baked", "baker", "baron", "bases", "basic", "basil", "basin", "basis", "batch", "beach",
    "beard", "beast", "began", "begin", "begun", "being", "belly", "below", "bench", "berry",
    "billy", "birth", "black", "blade", "blame", "blank", "blast", "blaze", "bleak", "blend",
    "blind", "block", "blood", "bloom", "blown", "blues", "blunt", "board", "boast", "bobby",
    "bonus", "boost", "booth", "borne", "bound", "bowel", "boxer", "brain", "brake", "brand",
    "brass", "brave", "bread", "break", "breed", "brent", "brick", "bride", "brief", "bring",
    "brink", "brisk", "broad", "broke", "brook", "brown", "brush", "buddy", "build", "built",
    "bunch", "burke", "burnt", "burst", "buyer", "cabin", "cable", "cache", "calif", "canal",
    "candy", "canon", "cargo", "carol", "carry", "catch", "cater", "cause", "cease", "chain",
    "chair", "chalk", "chaos", "charm", "chart", "chase", "cheap", "check", "cheek", "cheer",
    "chess", "chest", "chick", "chief", "child", "chile", "chill", "china", "choir", "chose",
    "chuck", "cisco", "civic", "civil", "claim", "clash", "class", "clean", "clear", "clerk",
    "click", "cliff", "climb", "clock", "close", "cloth", "cloud", "coach", "coast", "colon",
    "color", "comic", "condo", "coral", "corps", "costa", "couch", "cough", "could", "count",
    "court", "cover", "crack", "craft", "crane", "crash", "crazy", "cream", "creed", "creek",
    "crest", "cried", "cries", "crime", "crisp", "cross", "crowd", "crown", "crude", "cruel",
    "crush", "crust", "cubic", "curry", "curve", "cycle", "daddy", "daily", "dairy", "daisy",
    "dance", "dated", "dealt", "death", "debit", "debut", "decay", "decor", "delay", "delta",
    "dense", "depot", "depth", "derby", "deter", "devil", "diary", "digit", "dirty", "dodge",
    "doing", "donor", "doubt", "dozen", "draft", "drain", "drama", "drank", "drawn", "dream",
    "dress", "dried", "drift", "drill", "drink", "drive", "drove", "drunk", "dusty", "dying",
    "eager", "eagle", "early", "earth", "eaten", "eight", "elbow", "elder", "elect", "elite",
    "empty", "enemy", "enjoy", "enter", "entry", "equal", "error", "essay", "ethic", "event",
    "every", "exact", "excel", "exert", "exile", "exist", "extra", "faint", "fairy", "faith",
    "false", "famed", "fancy", "fatal", "fatty", "fault", "favor", "feast", "fence", "ferry",
    "fetch", "fever", "fiber", "fibre", "field", "fiery", "fifth", "fifty", "fight", "final",
    "first", "fitch", "fixed", "flame", "flash", "fleet", "flesh", "flies", "flint", "float",
    "flock", "flood", "floor", "flora", "flour", "flown", "fluid", "flung", "flush", "focal",
    "focus", "force", "forge", "forth", "forty", "forum", "found", "frame", "frank", "fraud",
    "fresh", "fried", "front", "frost", "fruit", "fully", "funny", "gamma", "gauge", "genre",
    "ghost", "giant", "given", "glass", "globe", "glory", "glove", "going", "grace", "grade",
    "grain", "grams", "grand", "grant", "graph", "grasp", "grass", "grave", "great", "greed",
    "green", "greet", "grief", "grill", "gross", "group", "grove", "grown", "guard", "guess",
    "guest", "guide", "guild", "guilt", "habit", "handy", "happy", "hardy", "harry", "harsh",
    "hatch", "haven", "heart", "heath", "heavy", "hedge", "hefty", "hello", "hence", "henry",
    "hobby", "holly", "homer", "honey", "honor", "horse", "hotel", "house", "human", "hurry",
    "ideal", "image", "imply", "incur", "index", "inner", "input", "intel", "inter", "irony",
    "issue", "ivory", "japan", "jenny", "jewel", "jimmy", "joint", "jones", "judge", "juice",
    "knife", "knock", "known", "label", "labor", "laden", "lance", "large", "laser", "later",
    "laugh", "layer", "learn", "lease", "least", "leave", "legal", "lemon", "level", "lever",
    "lewis", "light", "limit", "linen", "links", "liver", "lives", "lobby", "local", "lodge",
    "logic", "loose", "lotus", "lover", "lower", "loyal", "lucky", "lunch", "lying", "lynch",
    "magic", "major", "maker", "manor", "maple", "march", "maria", "marry", "marsh", "mason",
    "match", "maxim", "maybe", "mayor", "meant", "medal", "media", "mercy", "merge", "merit",
    "merry", "metal", "meter", "metre", "metro", "micro", "midst", "might", "minor", "minus",
    "mitch", "mixed", "model", "modem", "moist", "molly", "money", "monte", "month", "moody",
    "moral", "motif", "motor", "mound", "mount", "mouse", "mouth", "movie", "mummy", "music",
    "naive", "naked", "nancy", "nasty", "naval", "needs", "nerve", "never", "newly", "niche",
    "night", "ninth", "noble", "noise", "noisy", "north", "notch", "noted", "novel", "nurse",
    "nylon", "occur", "ocean", "offer", "often", "olive", "onion", "onset", "opera", "optic",
    "orbit", "order", "organ", "other", "ought", "ounce", "outer", "overt", "oxide", "ozone",
    "paint", "panel", "panic", "paper", "party", "pasta", "paste", "patch", "patio", "pause",
    "peace", "pearl", "peggy", "penny", "perry", "peter", "petty", "phase", "phone", "photo",
    "piano", "piece", "piles", "pilot", "pinch", "piper", "pitch", "pizza", "place", "plain",
    "plane", "plant", "plate", "plaza", "point", "polar", "pound", "power", "press", "price",
    "pride", "prime", "print", "prior", "prize", "probe", "prone", "proof", "prose", "proud",
    "prove", "proxy", "pulse", "punch", "pupil", "purse", "queen", "query", "quest", "queue",
    "quick", "quiet", "quite", "quota", "quote", "radar", "radio", "raise", "rally", "ralph",
    "ranch", "randy", "range", "rapid", "ratio", "reach", "react", "ready", "realm", "rebel",
    "refer", "rehab", "reign", "relax", "relay", "renal", "renew", "repay", "reply", "resin",
    "rider", "ridge", "rifle", "right", "rigid", "riley", "risky", "rival", "river", "roast",
    "robin", "robot", "rocky", "roger", "roman", "rouge", "rough", "round", "route", "rover",
    "royal", "ruler", "rural", "rusty", "saint", "salad", "sally", "salon", "sandy", "sauce",
    "scale", "scare", "scene", "scent", "scope", "score", "scout", "scrap", "screw", "seize",
    "sense", "serum", "serve", "setup", "seven", "shade", "shaft", "shake", "shaky", "shall",
    "shame", "shape", "share", "sharp", "sheep", "sheer", "sheet", "shelf", "shell", "shift",
    "shine", "shiny", "shirt", "shock", "shook", "shoot", "shore", "short", "shout", "shown",
    "sided", "siege", "sight", "sigma", "silly", "since", "sixth", "sixty", "sized", "skies",
    "skill", "skirt", "skull", "slate", "slave", "sleek", "sleep", "slept", "slice", "slide",
    "slope", "slump", "small", "smart", "smash", "smell", "smile", "smith", "smoke", "snack",
    "snake", "solar", "solid", "solve", "sorry", "sound", "south", "space", "spare", "spark",
    "speak", "speed", "spell", "spend", "spent", "spike", "spill", "spine", "spite", "split",
    "spoke", "spoon", "sport", "spray", "squad", "stack", "staff", "stage", "stake", "stall",
    "stamp", "stand", "stare", "stark", "start", "state", "steak", "steal", "steam", "steel",
    "steep", "steer", "stein", "stern", "stick", "stiff", "still", "sting", "stock", "stole",
    "stone", "stood", "stool", "store", "storm", "story", "straw", "strip", "stuck", "study",
    "stuff", "style", "sugar", "suite", "sunny", "super", "surge", "swear", "sweat", "sweep",
    "sweet", "swell", "swept", "swift", "swing", "sword", "sworn", "swung", "table", "taken",
    "tales", "taste", "taxes", "teach", "teddy", "teeth", "telco", "tense", "tenth", "terry",
    "texas", "thank", "theft", "their", "theme", "there", "these", "thick", "thief", "thigh",
    "thing", "think", "third", "those", "three", "threw", "throw", "thumb", "tiger", "tight",
    "times", "tired", "title", "toast", "today", "token", "tommy", "tonne", "tooth", "topic",
    "torch", "total", "touch", "tough", "towel", "tower", "toxic", "trace", "track", "tract",
    "trade", "trail", "train", "trash", "treat", "trend", "trial", "tribe", "trick", "tried",
    "tries", "troop", "trout", "truck", "truly", "trunk", "trust", "truth", "tutor", "twice",
    "twist", "tying", "ultra", "uncle", "under", "undue", "union", "unite", "unity", "until",
    "upper", "upset", "urban", "urine", "usage", "usual", "utter", "vague", "valid", "value",
    "valve", "vapor", "vault", "venue", "verge", "verse", "video", "villa", "vinyl", "viral",
    "virus", "visit", "vista", "vital", "vivid", "vocal", "voice", "voter", "wagon", "waist",
    "waste", "watch", "water", "weary", "weber", "weigh", "weird", "welsh", "wheat", "wheel",
    "where", "which", "while", "white", "whole", "whose", "widow", "width", "wired", "witch",
    "wives", "woman", "women", "world", "worry", "worse", "worst", "worth", "would", "wound",
    "woven", "wrist", "write", "wrong", "wrote", "yacht", "yield", "young", "yours", "youth"]


class Word_Game:
  #Title card at intro to game
  title_art = r"""
   __     __     ______     ______     _____     __         __  __    
  /\ \  _ \ \   /\  __ \   /\  == \   /\  __-.  /\ \       /\ \_\ \   
  \ \ \/ ".\ \  \ \ \/\ \  \ \  __<   \ \ \/\ \ \ \ \____  \ \____ \  
   \ \__/".~\_\  \ \_____\  \ \_\ \_\  \ \____-  \ \_____\  \/\_____\ 
    \/_/   \/_/   \/_____/   \/_/ /_/   \/____/   \/_____/   \/_____/                                                                     
  """                                                                  
  
  def __init__(self, words):
    #Sets word list and intros to game
    self.words = words
    print(f"\n                         Welcome to...{Word_Game.title_art}")
    print("\n      You are going to guess 5-letter words and be given hints\n               based on the letters that are correct!\n                            Have fun!")
  




def main():
  wordly = Word_Game(WORDS_LIST)



if __name__ == "__main__":
  main()