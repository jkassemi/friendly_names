"""Noun word list for name generation"""

NOUNS = [
    "river", "mountain", "star", "cloud", "tree", "bird", "wind", "sun", "moon", "lake",
    "forest", "meadow", "ocean", "valley", "flower", "storm", "rain", "snow", "leaf",
    "brook", "stream", "hill", "peak", "cliff", "wave", "beach", "shore", "coast", "bay",
    "island", "desert", "canyon", "cave", "rock", "stone", "pebble", "crystal", "gem",
    "pearl", "coral", "shell", "sand", "dune", "glacier", "iceberg", "frost", "mist",
    "fog", "dawn", "dusk", "twilight", "night", "day", "sky", "horizon", "rainbow",
    "lightning", "thunder", "breeze", "gale", "hurricane", "tornado", "cyclone", "air",
    "earth", "fire", "water", "garden", "grove", "orchard", "jungle", "reef", "lagoon",
    "spring", "summer", "autumn", "winter", "seed", "root", "branch", "trunk", "twig",
    "blossom", "petal", "nectar", "honey", "pine", "oak", "maple", "willow", "birch",
    "cedar", "fern", "moss", "grass", "reed", "bamboo", "vine", "ivy", "rose", "lily",
    "daisy", "iris", "lotus", "orchid", "tulip", "sunflower", "poppy", "jasmine",
    "lavender", "sage", "mint", "thyme", "rosemary", "basil", "clover", "mushroom",
    "lichen", "algae", "seaweed", "kelp", "plankton", "coral", "anemone", "starfish",
    "dolphin", "whale", "seal", "otter", "fish", "shark", "ray", "turtle", "crab",
    "lobster", "shrimp", "oyster", "clam", "mussel", "eagle", "hawk", "falcon", "owl",
    "raven", "crow", "sparrow", "finch", "robin", "cardinal", "bluejay", "hummingbird",
    "swan", "goose", "duck", "loon", "penguin", "pelican", "crane", "heron", "stork",
    "flamingo", "peacock", "parrot", "dove", "pigeon", "swallow", "swift", "martin",
    "thrush", "warbler", "wren", "chickadee", "woodpecker", "kingfisher", "butterfly",
    "moth", "dragonfly", "bee", "wasp", "ant", "cricket", "grasshopper", "beetle",
    "ladybug", "firefly", "spider", "scorpion", "deer", "elk", "moose", "caribou",
    "antelope", "gazelle", "bison", "buffalo", "ox", "yak", "goat", "sheep", "ram",
    "wolf", "fox", "coyote", "jackal", "bear", "panda", "raccoon", "badger", "otter",
    "marten", "weasel", "mink", "ferret", "rabbit", "hare", "squirrel", "chipmunk",
    "beaver", "mouse", "rat", "vole", "mole", "hedgehog", "porcupine", "armadillo",
    "opossum", "kangaroo", "wallaby", "koala", "wombat", "platypus", "echidna",
    "lion", "tiger", "leopard", "jaguar", "cheetah", "lynx", "cougar", "panther",
    "elephant", "rhinoceros", "hippopotamus", "giraffe", "zebra", "horse", "donkey",
    "camel", "llama", "alpaca", "gorilla", "chimpanzee", "orangutan", "gibbon",
    "monkey", "lemur", "sloth", "anteater", "pangolin", "lizard", "snake", "turtle",
    "tortoise", "crocodile", "alligator", "iguana", "gecko", "chameleon", "salamander",
    "newt", "frog", "toad", "asteroid", "comet", "planet", "galaxy", "nebula", "quasar",
    "cosmos", "aurora", "meteor", "meteorite", "constellation", "zodiac", "orbit",
    "eclipse", "nova", "supernova", "pulsar", "equinox", "solstice", "atmosphere",
    "stratosphere", "troposphere", "ozone", "carbon", "nitrogen", "oxygen", "hydrogen",
    "helium", "neon", "crystal", "diamond", "ruby", "emerald", "sapphire", "topaz",
    "opal", "amber", "jade", "quartz", "granite", "marble", "slate", "limestone",
    "sandstone", "basalt", "obsidian", "geode", "fossil", "bone", "ivory", "horn",
    "antler", "feather", "scale", "shell", "cocoon", "web", "nest", "burrow", "den",
    "cave", "cavern", "grotto", "tunnel", "canyon", "gorge", "ravine", "cliff",
    "plateau", "mesa", "butte", "volcano", "crater", "geyser", "spring", "waterfall",
    "cascade", "rapid", "delta", "estuary", "strait", "channel", "sound", "harbor",
    "port", "pier", "dock", "wharf", "marina", "lighthouse", "beacon", "archipelago",
    "atoll", "peninsula", "isthmus", "cape", "promontory", "bluff", "dune", "oasis",
    "marsh", "swamp", "bog", "fen", "moor", "heath", "prairie", "plain", "steppe",
    "savanna", "tundra", "taiga", "fjord", "glade", "clearing", "thicket", "copse",
    "woodland", "rainforest", "mangrove", "banyan", "sequoia", "redwood", "spruce",
    "cypress", "eucalyptus", "baobab", "acacia", "palm", "coconut", "banana", "mango",
    "fig", "olive", "apple", "pear", "peach", "plum", "cherry", "lemon", "lime",
    "orange", "grapefruit", "pomegranate", "persimmon", "papaya", "guava", "lychee",
    "berry", "grape", "kiwi", "melon", "pineapple", "vanilla", "cinnamon", "pepper",
    "ginger", "turmeric", "saffron", "cardamom", "nutmeg", "clove", "anise", "fennel",
    "dill", "parsley", "cilantro", "chive", "garlic", "onion", "leek", "celery",
    "carrot", "potato", "yam", "cassava", "taro", "turnip", "radish", "beet", "corn",
    "wheat", "rice", "barley", "oat", "rye", "millet", "sorghum", "quinoa", "amaranth",
    "buckwheat", "flax", "cotton", "hemp", "jute", "silk", "wool", "leather", "rubber",
    "amber", "resin", "sap", "nectar", "pollen", "spore", "seed", "cone", "pod",
    "legume", "bean", "pea", "lentil", "chickpea", "soybean", "almond", "walnut",
    "pecan", "cashew", "pistachio", "chestnut", "hazelnut", "coconut", "macadamia",
    "pinyon", "acorn", "current", "tide", "wake", "ripple", "eddy", "whirlpool",
    "maelstrom", "tsunami", "flood", "drought", "avalanche", "landslide", "earthquake",
    "tremor", "ash", "smoke", "spark", "flame", "blaze", "inferno", "magma", "lava"
]
